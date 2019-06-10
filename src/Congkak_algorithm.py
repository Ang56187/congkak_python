import numpy as np

class Congkak_algorithm:

    def __init__(self):
        self.algorithm()

    def algorithm(self):
        self.board = np.zeros((2,8),dtype=int)
        self.board[:,0:7] = 0
        self.current_player=0

    def print_board(self):
        print(self.board)

    def check_end(self):
        ##check if game have ended or not
        ##if all holes were emptied out
        
        for i in range(len(self.board)):
            for j in  range(len(self.board[i])):
                if self.board[i][j] >0:
                    print("Yes")
                    return False
        print("No")

    def play_move(self,i,j):
        if self.board[0,7] + self.board[1,7] == 98:
            return True
        return False

    def has_available_move(self,i):
        if np.any(self.board[i,0:5]!=0):
            return True
        return False

    def play_game(self):
        self.check_end()

            ##self.print_board()
            ##inputMove = int(input("Enter 0-7"))
            ##if inputMove>=0 and inputMove<7:
                ##print("SURE")
            ##else:
                ##print("Only 0-7 allowed")


