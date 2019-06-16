from Congkak_algorithm import Congkak_algorithm
from random import randint
import copy

class Ai_player:

    def __init__(self,available_move,board,holes,seeds):
        self.initialize()
        self.available_move=available_move
        self.board = board
        self.holes = holes
        self.seeds = seeds

    def initialize(self):
        self.ai_row = 0

    # ai select moves by random
    def low_level_algorithm(self):
        random_col = randint(0,len(self.available_move)-1)
        avail_move = self.available_move
        return self.available_move[random_col]

    # ai detect winning move through boyer moore pattern matching
    def normal_level_algorithm(self):

        # create new copy of board to not affect main one
        ai_congkak = Congkak_algorithm(0,0,"Player 1","Player 2",0,self.holes,self.seeds)

        # keep updated with current changes to main board
        # for move in self.available_move:
        copy_ai_board = copy.deepcopy(self.board)

        #used to evaluate priority of each move
        priority = 0

        # show all possible move outcome of the ai
        for move in self.available_move:
            # reset the board after previous move changed the board
            copy_ai_board = copy.deepcopy(self.board)
            ai_congkak.set_board(copy_ai_board)


            ##number of moves list based on seeds collected
            move_list = []
            print("Hole shells:",ai_congkak.get_board()[1,2])
            for no_move in range(ai_congkak.get_board()[1][move]):
                move_list.append(1)

            move_list.append(0)
            num_move_list = len(move_list)

            # ai starts allocating seeds
            ai_congkak.ai_play_game(move)

            print("Move:",move)
            print(ai_congkak.get_board())

            ## merge both row lists into 1 for pattern matching
            first_half = ai_congkak.get_board()[0]
            second_half = ai_congkak.get_board()[1]
            merge_board = [*second_half ,*first_half]

            print(merge_board)
            print("Move lists ",move_list)

            # determines max seeds a hole can hold
            possibleMoves = self.holes*self.seeds*2
            print("Possible moves:",possibleMoves)

            for end_move in range(1,possibleMoves+1):
                if len(move_list)> num_move_list:
                    # use stack like behaviour, Last in first out
                    # replace top of list with new element
                    move_list.pop()
                    move_list.append(end_move)
                else:
                    move_list.append(end_move)
                print(merge_board)
                print(move_list)

            m = len(merge_board)
            n = len(move_list)

            if m>n:
                break








# def main():
#     ai = Ai_player()
#     print(ai.low_level_algorithm())
#
# if __name__ == '__main__':
#     main()

