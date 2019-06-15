import numpy as np
import re

class Congkak_algorithm:

    def __init__(self,player_score,oppo_score,player_name,oppo_name,current_player,num_hole,num_shell):
        self.player_score = player_score
        self.oppo_score = oppo_score

        self.player_name = player_name
        self.oppo_name = oppo_name

        #decides which player start first
        self.current_player = current_player

        self.num_hole = num_hole
        self.num_shell = num_shell
        self.algorithm()

    ##initialize variables not set by player
    def algorithm(self):
        self.board = np.zeros((2,self.num_hole),dtype=int)
        self.board[:,0:self.num_hole] = self.num_shell
        self.board[1,2] = 0
        self.board[0,0] =0
        no_zero = []



    def print_board(self):
        #prints the board
        print(self.board)



    def check_empty(self):
        ##check if game have ended or not
        ##if one side of hole were emptied out
        if all(element == 0 for element in self.board[0][0:self.num_hole]):
            print("Game ended on player side")
            return False
        elif all(element == 0 for element in self.board[1][0:self.num_hole]):
            print("Game ended on opponent side")
            return False
        else:
            return True



    def spill_seed(self,row,col):
        ##add seeds for each hole
        self.board[row][col]+=1



    def has_available_move(self,row):
        ## show player available moves they can make
        non_zero= []
        counter =0
        for col in self.board[row,:]:
            if col != 0 :
                non_zero.append(counter)
            counter+=1
        return  non_zero



    ## function to allow how shells were allocated
    def hole_moves(self,inputMove,moves,row):
        print ("")
        #move to row below
        if inputMove <=-1:
            inputMove = 0
            row =1

        #move to row above
        if inputMove >= self.num_hole:
            inputMove=self.num_hole-1
            row =0

        if row == 0:
            self.spill_seed(row,inputMove)
            print("Hole filled",inputMove)

            ## prevent adding inputMove even if no moves made
            if not moves == 1:
                print("Moves:",moves)
                inputMove -= 1

        elif row == 1:
            self.spill_seed(row,inputMove)
            print("Hole filled",inputMove)
            print(self.board)

            ## prevent adding inputMove even if no moves made
            if not moves == 1:
                print("Moves:",moves)
                inputMove += 1

        print(inputMove)



    def grab_seeds_same_row(self,row,inputMove):
        self.player_score += self.board[row,inputMove]
        ##grabbed all the seeds, leaving it empty
        self.board[row,inputMove] = 0
        ##now its opponent turn
        print("Player score:",self.player_score)

    # absolute of row required to remove negative,
    # as row in second row will be applied negatively
    def grab_seeds_next_row(self,row,inputMove):
        self.player_score += self.board[abs(1+row),inputMove]
        ##grabbed all the seeds, leaving it empty
        self.board[abs(row)-1,inputMove] = 0
        ##now its opponent turn
        current_player=1
        print("Player score:",self.player_score)


    def play_move(self,inputMove,row,num_of_loops):
        ##dictates how the hole allocation works

        ## start with players first
        ## iterate no of times based on shells on selected hole
        for moves in range(num_of_loops,0,-1):

            ##self.hole_moves(inputMove,moves,row)
            print ("")
            #move to row below
            if inputMove <=-1:
                inputMove = 0
                row =1

            #move to row above
            if inputMove >= self.num_hole:
                inputMove=self.num_hole-1
                row =0

            if row == 0:
                self.spill_seed(row,inputMove)
                print("Hole filled",inputMove)

                ## prevent adding inputMove even if no moves made
                if not moves <= 1:
                    print("Moves:",moves)
                    inputMove -= 1

            elif row == 1:
                self.spill_seed(row,inputMove)
                print("Hole filled",inputMove)
                print(self.board)

                ## prevent adding inputMove even if no moves made
                if not moves <= 1:
                    print("Moves:",moves)
                    inputMove += 1

            print("Moves:",moves)
            print("Input:",inputMove)

            ## get all seeds in hole after the empty hole
            if moves == 1 and row==0 and self.current_player ==0:
                #make sure it doesnt grab -1 hole shells, to prevent index error
                if inputMove>1  and self.board[row,inputMove-1] == 0:
                    ##self.player_score +=self.board[row,inputMove-2]
                    ##grabbed all the shells, leaving it empty
                    ##self.board[row,inputMove-2] = 0
                    ##now its opponent turn
                    ##current_player=1
                    ##print("Player score:",self.player_score)
                    self.grab_seeds_same_row(row,inputMove-2)

                if inputMove == 1 and self.board[row,inputMove-1] == 0:
                    ##go to next line
                    inputMove = 0
                    #self.player_score += self.board[row+1,inputMove]
                    ###grabbed all the seeds, leaving it empty
                    #self.board[row-1,inputMove] = 0
                    ###now its opponent turn
                    #current_player=1
                    #print("Player score:",self.player_score)
                    self.grab_seeds_next_row(row,inputMove)

            elif moves==1 and row ==1 and self.current_player ==0:
                #make sure it doesnt grab 7 hole seeds, to prevent index error
                if inputMove<self.num_hole-1 and self.board[row,inputMove] == 0:
                    print("YES")

                    ##self.player_score +=self.board[row,inputMove+1]
                    ##grabbed all the shells, leaving it emty
                    ##self.board[row,inputMove+1] = 0
                    ##now its opponent turn
                    ##current_player=1
                    ##print("Player score:",self.player_score)
                    self.grab_seeds_same_row(row,inputMove+1)

                if inputMove == self.num_hole-2 and self.board[row,inputMove+1] == 0:
                    inputMove=self.num_hole-1
                    self.grab_seeds_next_row(-row,inputMove)

            ## get all seeds in hole after the empty hole
            if moves == 1 and row==0 and self.current_player ==1:
                if inputMove>1  and self.board[row,inputMove] == 0:
                    self.oppo_score +=self.board[row,inputMove-1]
                    ##grabbed all the shells, leaving it empty
                    self.board[row,inputMove-1] = 0
                    ##now its player turn
                    print("Opponent score:",self.oppo_score)

            elif moves==1 and row ==1 and self.current_player == 1:
                if inputMove<self.num_hole-2 and self.board[row,inputMove] == 0:
                    self.oppo_score +=self.board[row,inputMove+1]
                    ##grabbed all the seeds, leaving it empty
                    self.board[row,inputMove+1] = 0
                    ##now its player turn
                    print("Opponent score:",self.oppo_score)

    def get_shell(self):
        print('gg')



    # when player start playing
    def player_play_game(self):
            # player always start at row 0
            row = 0
            print("Available moves:",self.has_available_move(row))
            self.print_board()

            ## allow player to choose where to place shells
            inputMsg = self.player_name+' enter '+str(self.has_available_move(row))+':'
            inputMove = input(inputMsg)

            #ensure player doesnt select non-existant holes
            while not inputMove \
                    or re.search("[a-zA-Z\W]+", inputMove) \
                    or not 0<=int(inputMove)<self.num_hole:
                inputMove = input(inputMsg)

            # ensure nholes with no shells cant be selected
            if self.board[row][int(inputMove)] == 0:
                while not inputMove \
                        or re.search("[a-zA-Z\W]+", inputMove) \
                        or not 0<=int(inputMove)<self.num_hole \
                        or self.board[row][int(inputMove)] ==0 :
                    inputMsg = self.player_name+',please select valid and non-zero hole '+str(self.has_available_move(row))+':'
                    inputMove = input(inputMsg)

            #inputMove(str) converted to (int)
            convertedMove = int(inputMove)

            ## create copy so before shells in hole got emptied
            no_times_loop = self.board[row,convertedMove]

            ## empty out the selected hole
            self.board[row,convertedMove]=0
            self.play_move(convertedMove-1,row,no_times_loop)
            self.current_player = 1



    # where opponent start playing
    def opponent_play_game(self):
            #opponent always start at row 1
            row=1
            print("Available moves:",self.has_available_move(row))
            self.print_board()
            ## allow player to choose where to place shells
            inputMsg = self.oppo_name+' enter '+str(self.has_available_move(row))+':'
            inputMove = input(inputMsg)

            #ensure player doesnt select non-existant holes
            while not inputMove \
                    or re.search("[a-zA-Z\W]+", inputMove) \
                    or not 0<=int(inputMove)<self.num_hole:
                        inputMove = input(inputMsg)

            if self.board[row][int(inputMove)] == 0:
                while not inputMove \
                        or re.search("[a-zA-Z\W]+", inputMove) \
                        or not 0<=int(inputMove)<self.num_hole \
                        or self.board[row][int(inputMove)] == 0 :
                            inputMsg = self.oppo_name+',please select valid and non-zero hole '+str(self.has_available_move(row))+':'
                            inputMove = input(inputMsg)

            #inputMove(str) converted to (int)
            convertedMove = int(inputMove)

            ## create copy so before shells in hole got emptied
            no_times_loop = self.board[row,convertedMove]

            ## empty out the selected hole
            self.board[row,convertedMove]=0
            self.play_move(convertedMove+1,row,no_times_loop)
            self.current_player = 0



    def main_game(self):
        while self.check_empty():
            if self.current_player == 0:
                self.player_play_game()
            elif self.current_player == 1:
                self.opponent_play_game()

        print('Player score:',self.player_score)
        print('Opponent score:',self.oppo_score)





