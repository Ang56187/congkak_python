from Congkak_algorithm import Congkak_algorithm
from Ai_player import Ai_player
import copy

def main():

    holes = 5
    seeds = 12
    ai_row = 1

    #choose if opponent is human, or ai
    # 1 = human
    # 2 = low level ai
    # 3 = normal level ai
    oppo_player = 3

    congkak = Congkak_algorithm(0,0,"Noobmaster","Thor",oppo_player,holes,seeds)

    while congkak.check_empty():

        ai = Ai_player(congkak.has_available_move(ai_row),congkak.get_board(),holes,seeds)

        if congkak.current_player == 0:
            print("--------------",congkak.get_player_name()," turn:-----------------------")
            congkak.player_play_game()

        # other manual player
        elif congkak.current_player == 1:
            print("--------------",congkak.get_oppo_name()," turn:-----------------------")
            congkak.opponent_play_game()

        # low level ai
        elif congkak.current_player == 2:
            row = 1
            print("--------------",congkak.get_oppo_name()," turn:-----------------------")
            generated_move = ai.low_level_algorithm()
            print("move selected:",generated_move)
            congkak.opponent_play_game(generated_move)
            print("move selected:",generated_move)

    # high level ai
        elif congkak.current_player ==3:
            row = 1
            print("--------------",congkak.get_oppo_name()," turn:-----------------------")
            generated_move = ai.normal_level_algorithm()
            print("move selected:",generated_move)
            congkak.opponent_play_game(generated_move)
            print("move selected:",generated_move)

        else:
            print("Invalid opponent.")
            break

        print('Player score:',congkak.get_player_score())
        print('Opponent score:',congkak.get_oppo_score())

    congkak.check_winner()



if __name__ == '__main__':
    main()
