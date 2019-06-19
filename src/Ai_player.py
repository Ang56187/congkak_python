from Congkak_algorithm import Congkak_algorithm
from Boyer_moore import boyer
from random import randint
from Boyer_moore import check_next_row
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
        priority_list = []
        priority_move_list = []

        # show all possible move outcome of the ai
        for move in self.available_move:
            # reset the board after previous move changed the board
            copy_ai_board = copy.deepcopy(self.board)
            ai_congkak.set_board(copy_ai_board)

            ##number of moves list based on seeds collected
            move_list = []

            ## element value in index added by 1 to account for first hole where seeds were grabbed
            for no_move in range(ai_congkak.get_board()[1][move]+1):
                move_list.append(1)

            move_list.append(0)
            num_move_list = len(move_list)

            ## merge both row lists into 1 for pattern matching
            first_half = ai_congkak.get_board()[0]
            ## reverse first row, as opponent move differently in first row
            first_half = first_half[::-1]
            second_half = ai_congkak.get_board()[1]
            merge_board = [*second_half ,*first_half]

            ## create copy in case merge_board need to combine 2 board lists
            copy_merge_board = [*second_half ,*first_half,*merge_board]


            # determines max seeds a hole can hold in current board
            possibleMoves = max(merge_board)

            # check if the move reaches hole with empty seeds
            # with boyer moore pattern matching
            # allocating 2 seed it will be like move_list[11102]
            # first index = hole to grab seeds
            # second - third index = hole allocated with seeds
            # third = hole with empty seeds
            # fouth = check if any seeds exist or not, depends on max seeds in hole
            # it will then match with the board list

            for end_move in range(1,possibleMoves+1):
                if len(move_list)> num_move_list:
                    # use stack like behaviour, Last in first out
                    # replace top of list with new element
                    move_list.pop()
                    move_list.append(end_move)
                else:
                    # removes it after all were added
                    move_list.append(end_move)

                ## if theres too many seeds that it allocates throughout whole board
                ## it cant find any more 0 hole gaps, so it is auto filtered out
                if len(move_list) <= len(merge_board):
                    p = boyer(merge_board,move_list,move,10)

                    if p  != -1:
                        priority_list.append(p)
                        priority_move_list.append(move)

            #remove 0 and number at end of list
            move_list.pop()
            move_list.pop()
            # check if seeds will be allocated to next row, priority of 2 or 5 or 6
            p = check_next_row(merge_board,move_list,move)

            if p  != -1:
                priority_list.append(p)
                priority_move_list.append(move)

            #insert normal moves with priority of 1
            p = 1
            priority_list.append(p)
            priority_move_list.append(move)

        #compare priority of each move, highest one gets selected
        best_priority = 0
        best_move = 0
        for i in range(0,len(priority_move_list)-1):
            if priority_list[i] > best_priority:
                best_priority = priority_list[i]
                best_move = priority_move_list[i]
        print("best",best_move,"priority",best_priority)
        print("priority list",priority_list)
        print(" move priority list",priority_move_list)

        return best_move

# def main():
#     ai = Ai_player()
#     print(ai.low_level_algorithm())
#
# if __name__ == '__main__':
#     main()

