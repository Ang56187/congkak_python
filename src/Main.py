from Congkak_algorithm import Congkak_algorithm
from Ai_player import Ai_player
import copy

def main():

    holes = 5
    seeds = 3
    ai_row = 1

    congkak = Congkak_algorithm(0,0,"Noobmaster","Thor",0,holes,seeds)

    #create copy of object to not affect the main board for AI purposes
    copy_board = copy.deepcopy(congkak.get_board())

    ai = Ai_player(congkak.has_available_move(ai_row),copy_board,holes,seeds)

    ai.normal_level_algorithm()

    congkak.main_game()


if __name__ == '__main__':
    main()
