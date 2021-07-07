from Congkak_algorithm import Congkak_algorithm
from Ai_player import Ai_player
import re
import copy

###for playing the game through compiler
def main(move = None):

    player1_name = input("(1)Please enter player 1 name:")
    while not player1_name:
        player1_name = input("(1)Please enter player 1 name:")

    player2_name = input("(2)Please enter player 2 name:")
    while not player2_name:
        player2_name = input("(1)Please enter player 2 name:")


    ## up to 99 holes can be created on board
    holes = input("(3)Please enter number of holes on board[2-99]:")
    while not holes \
            or re.search("[a-zA-Z\W]+",holes) \
            or not 2<=int(holes)<= 99:
        holes = input("(3)Please enter correct number of holes[2-99]:")

    # up to 99 seeds can be assigned to a hole
    seeds = input("(4)Please enter shells for each holes[1-99]:")
    while not seeds \
            or re.search("[a-zA-Z\W]+",seeds) \
            or not 1<=int(seeds)<= 99:
        seeds = input("(4)Please enter correct number of shells[1-99]:")

    #choose if opponent is human, or ai
    # 1 = human
    # 2 = low level ai
    # 3 = normal level ai
    oppo_player = input("(5)Select opponent type.\n 1=Human\n 2=Low level ai \n3=Normal level ai: ")
    while not oppo_player \
            or re.search("[a-zA-Z\W]+",oppo_player) \
            or not 1<=int(oppo_player)<= 3:
        oppo_player = input("(5)Please enter player type:\n 1=Human\n 2=Low level ai \n 3=Normal level ai:\n")

    ai_row = 1

    holes = int(holes)
    seeds = int(seeds)
    oppo_player = int(oppo_player)

    congkak = Congkak_algorithm(0,0,player1_name,player2_name,oppo_player,holes,seeds)

    while congkak.check_empty():

        ai = Ai_player(congkak.has_available_move(ai_row),congkak.get_board(),holes,seeds)

        #player
        if congkak.current_player == 0:
            print("--------------",congkak.get_player_name()," turn:-----------------------")
            if move == None:
                congkak.player_play_game()
            else:
                congkak.player_play_game(move)

        # other manual player
        elif congkak.current_player == 1:
            print("--------------",congkak.get_oppo_name()," turn:-----------------------")
            if move == None:
                congkak.opponent_play_game()
            else:
                congkak.opponent_play_game(move)
        # low level ai
        elif congkak.current_player == 2:
            print("--------------",congkak.get_oppo_name()," turn:-----------------------")
            generated_move = ai.low_level_algorithm()
            print("\nmove selected:",generated_move)
            congkak.opponent_play_game(generated_move)
            print("move selected:",generated_move)

    # high level ai
        elif congkak.current_player ==3:
            print("--------------",congkak.get_oppo_name()," turn:-----------------------")
            generated_move = ai.normal_level_algorithm()
            print("\nmove selected:",generated_move)
            congkak.opponent_play_game(generated_move)
            print("move selected:",generated_move)

        else:
            print("Invalid opponent.")
            break

        print('Player 1 score:',congkak.get_player_score())
        print('Player 2 score:',congkak.get_oppo_score())

    congkak.check_winner()

if __name__ == '__main__':
    main()
