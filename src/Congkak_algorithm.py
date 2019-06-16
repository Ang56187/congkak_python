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
        self.board[1,0] = 0
        #self.board[0,4] = 0
        #self.board[0,2] = 7
        no_zero = []

    def set_board(self,board):
        self.board = board

    def get_board(self):
        return self.board

    def get_player_score(self):
        return self.player_score

    def get_oppo_score(self):
        return self.oppo_score



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



    ##add seeds for each hole
    def spill_seed(self,row,col):
        self.board[row][col]+=1



    ## show player available moves they can make
    def has_available_move(self,row):
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
            ## prevent adding inputMove even if no moves made
            if not moves == 1:
                inputMove -= 1

        elif row == 1:
            self.spill_seed(row,inputMove)
            ## prevent adding inputMove even if no moves made
            if not moves == 1:
                inputMove += 1



    # grab_seeds_next_row used to grab holes in the opposite row
    def grab_seeds_same_row(self,player,row,inputMove):

        if player == 0:
            self.player_score += self.board[row,inputMove]
        elif player == 1:
            self.oppo_score += self.board[row,inputMove]
        ##grab all the seeds, leaving it empty
        self.board[row,inputMove] = 0

    # grab_seeds_next_row used to grab holes in the opposite row



    # absolute of row required to remove negative,
    # as row in second row will be applied negatively
    def grab_seeds_next_row(self,player,row,inputMove):
        if player == 0:
            self.player_score += self.board[abs(1+row),inputMove]
        elif player == 1:
            self.oppo_score += self.board[abs(1+row),inputMove]
        ##grabbed all the seeds, leaving it empty
        self.board[abs(row)-1,inputMove] = 0


    ##dictates how the seeds allocation works
    def play_move(self,inputMove,row,num_of_loops):

        ## start with players first
        ## iterate no of times based on shells on selected hole
        for moves in range(num_of_loops,0,-1):

            print ("")
            #move to row below
            if inputMove <=-1 and row== 0:
                inputMove = 0
                row =1

            #move to row above
            if inputMove >= self.num_hole and row == 1:
                inputMove=self.num_hole-1
                row =0

            if row == 0:
                self.spill_seed(row,inputMove)
                ## prevent adding inputMove even if no moves made
                if not moves <= 1:
                    inputMove -= 1

            elif row == 1:
                self.spill_seed(row,inputMove)
                ## prevent adding inputMove even if no moves made
                if not moves <= 1:
                    inputMove += 1

            ## part where it dictates how or when shells in holes are grabbed
            ## check if its at its last move and if its on first row
            if moves == 1 and row==0:
                #grabs shells if end before empty shells
                # 1011
                # 1111
                if inputMove>1  and self.board[row,inputMove-1] == 0:
                    self.grab_seeds_same_row(self.current_player,row,inputMove-2)

                #grabs shells in next row if zero at end, such as
                # 0111
                # 1111
                if inputMove == 1 and self.board[row,inputMove-1] == 0:
                    self.grab_seeds_next_row(self.current_player,row,inputMove-1)

                #grabs shells in next row if zero at next row, such as
                # 1111
                # 0111
                if inputMove == 0 and self.board[row+1,inputMove] == 0:
                    self.grab_seeds_next_row(self.current_player,row,inputMove+1)

            #check if its on its last move and if its on the second row
            elif moves==1 and row ==1:
                #grabs shells if end before empty shells,such as
                # 1111
                # 1011
                if inputMove<self.num_hole-2 and self.board[row,inputMove+1] == 0:
                    print("input:",inputMove)
                    print("A")
                    self.grab_seeds_same_row(self.current_player,row,inputMove+2)

                #grabs shells in next row if zero at end, such as
                # 1111
                # 1110
                if inputMove == self.num_hole-2 and self.board[row,inputMove+1] == 0:
                    inputMove=self.num_hole-1
                    print("input:",inputMove)
                    print("T")
                    self.grab_seeds_next_row(self.current_player,-row,inputMove)

                #grabs shells in next row if zero at next row, such as
                # 1110
                # 1111
                if inputMove == self.num_hole-1 and self.board[row-1,inputMove] == 0 and not self.board[row][inputMove] == 0:
                    print("input:",inputMove)
                    print("E")
                    self.grab_seeds_next_row(self.current_player,-row,inputMove-1)

            print(self.board)
            if self.current_player == 0:
                print("Player score:",self.player_score)
            elif self.current_player == 1:
                print("Opponent score:",self.oppo_score)



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



    # where ai play game, no input needed
    def ai_play_game(self,inputMove):

        row = 1
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





