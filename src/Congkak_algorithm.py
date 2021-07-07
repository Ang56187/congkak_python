import numpy as np
import re

class Congkak_algorithm:

    def __init__(self,player_score,oppo_score,player_name,oppo_name,oppo_player,num_hole,num_seed):
        self.player_score = player_score
        self.oppo_score = oppo_score

        self.player_name = player_name
        self.oppo_name = oppo_name

        #decides which player start first
        self.oppo_player = oppo_player

        self.num_hole = num_hole
        self.num_seed = num_seed
        self.algorithm()

    ##initialize variables not set by player
    def algorithm(self):
        self.row = 0
        self.board = np.zeros((2,self.num_hole),dtype=int)
        self.board[:,0:self.num_hole] = self.num_seed
        self.current_player = 0
        self.inputMsg = ""
        no_zero = []

    #getters
    def set_board(self,board):
        self.board = board

    def get_board(self):
        return self.board

    def get_player_score(self):
        return self.player_score

    def get_oppo_score(self):
        return self.oppo_score

    def get_player_name(self):
            return self.player_name

    def get_oppo_name(self):
        return self.oppo_name

    def get_inputMsg(self):
        return self.inputMsg

    def get_row(self):
        return self.row

    def get_current_player(self):
        return self.current_player



    #prints the board
    def print_board(self):
        print(self.board)



    ##check if game have ended or not
    ##if one side of hole were emptied out
    def check_empty(self):

        if all(element == 0 for element in self.board[0][0:self.num_hole]):
            print("Game ended on player 1 side.")
            return False
        elif all(element == 0 for element in self.board[1][0:self.num_hole]):
            print("Game ended on player 2 side.")
            return False
        else:
            return True



    #check which palyer got the most score
    def check_winner(self):
        if self.player_score > self.oppo_score:
            print("(Player 1)",self.player_name," have won!")
        elif self.player_score < self.oppo_score:
            print("(Player 2)",self.oppo_name,"have won!")
        else:
            print("Its a tie!")



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



    # grab_seeds_next_row used to grab holes in the opposite row
    def grab_seeds_same_row(self,player,row,inputMove):

        if player == 0:
            self.player_score += self.board[row,inputMove]
        elif player >= 1:
            self.oppo_score += self.board[row,inputMove]
        ##grab all the seeds, leaving it empty
        self.board[row,inputMove] = 0

    # grab_seeds_next_row used to grab holes in the opposite row



    # absolute of row required to remove negative,
    # as row in second row will be applied negatively
    # from 0 to 1,row = 0
    # (1+(row))=1
    # (row-1) = abs(-1) = 1

    # from 1 to 0,row =1
    # (1+row) = 0
    # (row -1) = 0
    def grab_seeds_next_row(self,player,row,inputMove):
        if player == 0:
            self.player_score += self.board[abs(1+row),inputMove]
        elif player >= 1:
            self.oppo_score += self.board[abs(1+row),inputMove]
        ##grabbed all the seeds, leaving it empty
        self.board[abs(row)-1,inputMove] = 0


    ##dictates how the seeds allocation works
    def play_move(self,inputMove,row,num_of_loops):

        ## start with players first
        ## iterate no of times based on shells on selected hole
        for moves in range(num_of_loops,0,-1):
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
                    self.grab_seeds_same_row(self.current_player,row,inputMove+2)

                #grabs shells in next row if zero at end, such as
                # 1111
                # 1110
                if inputMove == self.num_hole-2 and self.board[row,inputMove+1] == 0:
                    inputMove=self.num_hole-1
                    self.grab_seeds_next_row(self.current_player,-row,inputMove)

                #grabs shells in next row if zero at next row, such as
                # 1110
                # 1111
                if inputMove == self.num_hole-1 and self.board[row-1,inputMove] == 0 and not self.board[row][inputMove] == 0:
                    self.grab_seeds_next_row(self.current_player,-row,inputMove-1)

            print("Move:",num_of_loops-moves+1)
            self.print_board()
            print("")



    # when player start playing
    def player_play_game(self,move = None):

            # player always start at row 0
            self.row = 0

            print("")
            print("Available moves:",self.has_available_move(self.row))
            self.print_board()

            if move == None:
                ## allow player to choose where to place shells
                self.inputMsg = "(Player 1)"+self.player_name+' enter '+str(self.has_available_move(self.row))+':'
                inputMove = input(self.inputMsg)

                #ensure player doesnt select non-existant holes
                while not inputMove \
                        or re.search("[a-zA-Z\W]+", inputMove) \
                        or not 0<=int(inputMove)<self.num_hole:
                    inputMove = input(self.inputMsg)

                # ensure nholes with no shells cant be selected
                if self.board[self.row][int(inputMove)] == 0:
                    while not inputMove \
                            or re.search("[a-zA-Z\W]+", inputMove) \
                            or not 0<=int(inputMove)<self.num_hole \
                            or self.board[self.row][int(inputMove)] ==0 :
                        self.inputMsg = "(Player 1)"+self.player_name+',please select valid and non-zero hole '+str(self.has_available_move(self.row))+':'
                        inputMove = input(self.inputMsg)

                #inputMove(str) converted to (int)
                convertedMove = int(inputMove)

            else:
                convertedMove = int(move)
                print("move selected:",move)

            ## create copy so before shells in hole got emptied
            no_times_loop = self.board[self.row,convertedMove]

            ## empty out the selected hole
            self.board[self.row,convertedMove]=0
            self.play_move(convertedMove-1,self.row,no_times_loop)

            self.current_player = self.oppo_player
            self.row = 1



    # where opponent start playing
    def opponent_play_game(self,move = None):
            #opponent always start at row 1
            self.row=1

            print("")
            print("Available moves:",self.has_available_move(self.row))
            self.print_board()

            convertedMove = 0

            if move == None :
                ## allow player to choose where to place shells
                self.inputMsg = "(Player 2)"+self.oppo_name+' enter '+str(self.has_available_move(self.row))+':'
                inputMove = input(self.inputMsg)

                #ensure player doesnt select non-existent holes
                while not inputMove \
                        or re.search("[a-zA-Z\W]+", inputMove) \
                        or not 0<=int(inputMove)<self.num_hole:
                            inputMove = input(self.inputMsg)

                if self.board[self.row][int(inputMove)] == 0:
                    while not inputMove \
                            or re.search("[a-zA-Z\W]+", inputMove) \
                            or not 0<=int(inputMove)<self.num_hole \
                            or self.board[self.row][int(inputMove)] == 0 :
                                self.inputMsg = "(Player 2)"+self.oppo_name+',please select valid and non-zero hole '+str(self.has_available_move(self.row))+':'
                                inputMove = input(self.inputMsg)

                #inputMove(str) converted to (int)
                convertedMove = int(inputMove)

            #if parameter move is assigned with value
            else:
                convertedMove = int(move)
                print("move selected:",move)

            ## create copy so before shells in hole got emptied
            no_times_loop = self.board[self.row,convertedMove]

            ## empty out the selected hole
            self.board[self.row,convertedMove]=0
            self.play_move(convertedMove+1,self.row,no_times_loop)
            self.current_player = 0
            self.row = 0


    # ## function to allow how shells were allocated
    # def hole_moves(self,inputMove,moves,row):
    #     print ("")
    #     #move to row below
    #     if inputMove <=-1:
    #         inputMove = 0
    #         row =1
    #
    #     #move to row above
    #     if inputMove >= self.num_hole:
    #         inputMove=self.num_hole-1
    #         row =0
    #
    #     if row == 0:
    #         self.spill_seed(row,inputMove)
    #         ## prevent adding inputMove even if no moves made
    #         if not moves == 1:
    #             inputMove -= 1
    #
    #     elif row == 1:
    #         self.spill_seed(row,inputMove)
    #         ## prevent adding inputMove even if no moves made
    #         if not moves == 1:
    #             inputMove += 1









