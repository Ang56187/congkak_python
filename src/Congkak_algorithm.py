import numpy as np

class Congkak_algorithm:

    def __init__(self):
        self.algorithm()

    def algorithm(self):
        self.board = np.zeros((2,7),dtype=int)
        self.board[:,0:7] = 7
        self.current_player = 1

    def print_board(self):
        print(self.board)

    def check_empty(self):
        ##check if game have ended or not
        ##if one side of hole were emptied out

        for j in range(len(self.board[0])):
            if self.board[0][j] >0:
                print("Not empty on player side")
                return True
            elif self.board[1][j] > 0:
                print("Not empty on apponent side")
                return True

    def spill_seed(self,col,row):
        ##add seeds for each hole
        self.board[col][row-1]+=1

    def move(self,i,j):
        if self.board[0,7] + self.board[1,7] == 98:
            return True
        return False

    def has_available_move(self,i):
        if np.any(self.board[i,0:5]!=0):
            return True
        return False

    #where the game starts playing
    def play_game(self):
        while self.check_empty():
            self.print_board()

            ## allow player to choose where to place shells
            inputMove = int(input("Enter 0-6:"))
            while not 0<=inputMove<7:
                    inputMove = int(input("Please enter 0-6:"))

            while self.board[0][inputMove] == 0:
                inputMove = int(input("Please select valid and non-zero hole:"))
            print("Input in")


            ## create copy so before shells in hole got emptied, and shells grabbed into hand
            no_times_loop = self.board[0,inputMove]

            ## empty out the selected hole
            self.board[0,inputMove]=0

            col = 0

            ## start with players first
            ## iterate no of times based on shells on selected hole
            for moves in range(no_times_loop,-1,-1):
                print("column:",col)

                if inputMove<=0:
                    col=1


                if col == 0:
                    self.print_board()
                    self.spill_seed(col,inputMove)
                    print(inputMove)
                    inputMove -= 1
                elif col == 1:
                    self.print_board()
                    self.spill_seed(col,inputMove)
                    print(inputMove)
                    inputMove+=1




