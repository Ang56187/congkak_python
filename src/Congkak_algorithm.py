import numpy as np

class Congkak_algorithm:

    def __init__(self,player_score,oppo_score):
        self.player_score = player_score
        self.oppo_score = oppo_score
        self.algorithm()

    def algorithm(self):
        self.board = np.zeros((2,7),dtype=int)
        self.board[:,0:7] = 13
        ## 0 is player, 1 is opponent
        self.current_player = 0

    def print_board(self):
        print(self.board)

    def check_empty(self):
        ##check if game have ended or not
        ##if one side of hole were emptied out

        for j in range(len(self.board[0])):
            if self.board[0][j] > 0:
                print("Not empty on player side")
                return True
            elif self.board[1][j] > 0:
                print("Not empty on apponent side")
                return True
        return False

    def spill_seed(self,row,col):
        ##add seeds for each hole
        self.board[row][col-1]+=1

    def move(self,i,j):
        if self.board[0,7] + self.board[1,7] == 98:
            return True
        return False

    def has_available_move(self,i):
        if np.any(self.board[i,0:5]!=0):
            return True
        return False

    def play_move(self,inputMove):
        ## create copy so before shells in hole got emptied
        no_times_loop = self.board[0,inputMove]

        ## empty out the selected hole
        self.board[0,inputMove]=0

        ##set row where player starts
        row = 0

        ## start with players first
        ## iterate no of times based on shells on selected hole
        for moves in range(no_times_loop,0,-1):
            print ("")
            print("Moves left:",moves)
            print("column:",row)

            if inputMove<=0:
                row =1
                inputMove = 1

            if inputMove >=8:
                row =0
                inputMove=7

            if row == 0:
                self.spill_seed(row,inputMove)
                self.print_board()
                print("Hole read",inputMove)
                inputMove -= 1

            elif row == 1:
                self.spill_seed(row,inputMove)
                self.print_board()
                print("Hole filled",inputMove)
                inputMove+=1

            ## get all shells in hole after the empty hole
            if moves == 1 and row==0 and self.current_player ==0:
                self.player_score +=self.board[row,inputMove-2]
                ##grabbed all the shells, leaving it empty
                self.board[row,inputMove-2] = 0
                ##now its opponent turn
                current_player=1
                print("Player score:",self.player_score)

            elif moves==1 and row ==1 and self.current_player ==0:
                self.player_score +=self.board[row,inputMove+2]
                ##grabbed all the shells, leaving it emty
                self.board[row,inputMove-2] = 0
                ##now its opponent turn
                current_player=1
                print("Player score:",self.player_score)

            ## get all shells in hole after the empty hole
            if moves == 1 and row==0 and self.current_player ==1:
                self.oppo_score +=self.board[row,inputMove-2]
                ##grabbed all the shells, leaving it empty
                self.board[row,inputMove-2] = 0
                ##now its player turn
                current_player=0
                print("Opponent score:",self.oppo_score)

            elif moves==1 and row ==1 and self.current_player == 1:
                self.oppo_score +=self.board[row,inputMove+2]
                ##grabbed all the shells, leaving it empty
                self.board[row,inputMove-2] = 0
                ##now its player turn
                current_player=0
                print("Player score:",self.oppo_score)


    #where the game starts playing
    def player_play_game(self):
        while self.check_empty():
            self.print_board()
            ## allow player to choose where to place shells
            inputMove = int(input("Enter 0-6:"))
            while not 0<=inputMove<7:
                    inputMove = int(input("Please enter 0-6:"))

            while self.board[0][inputMove] == 0:
                inputMove = int(input("Please select valid and non-zero hole:"))
            print("Input in")
            self.play_move(inputMove)





