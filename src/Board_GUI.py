import tkinter as tk
import numpy as np
from Congkak_algorithm import Congkak_algorithm
import re
from Ai_player import Ai_player

root = tk.Tk()

root.title("Congkak")
root.geometry("700x500")

class Board_GUI(tk.Frame):

    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        self.parent = parent

        root.title("Congkak")

        lbl = tk.Label(root, text="Welcome To congkak", font=("Arial Bold", 10))
        lbl.grid(row=0,columnspan=20)

        ## Input Name
        def game_start():
            if e1.get() and e2.get():
                print("Player 1's Name: %s\nPlayer 2's Name: %s" % (e1.get(), e2.get()))
                print(hole_no.get()+"\n"+seed_no.get()+"\n"+ oppo_option.get())

                oppo_no = 0
                hole_num = int(hole_no.get())
                seed_num = int(seed_no.get())

                print(type(oppo_option.get()))

                if re.search('Human',oppo_option.get()):
                    oppo_no = 1
                elif re.search('Low Level AI',oppo_option.get()):
                    oppo_no = 2
                elif re.search('Normal Level AI',oppo_option.get()):
                    oppo_no = 3

                print("AI:",oppo_no)


                self.createBoard(e1.get(),e2.get(),oppo_no,hole_num,seed_num)
                e1.delete(0, tk.END)
                e2.delete(0, tk.END)
                play_btn.config(state = "disabled")

                lbl.grid_forget()
                e1.grid_forget()
                e2.grid_forget()
                label1.grid_forget()
                label2.grid_forget()
                label3.grid_forget()
                label4.grid_forget()
                oppo_drop.grid_forget()
                hole_drop.grid_forget()
                seed_drop.grid_forget()
                play_btn.grid_forget()

        label1 = tk.Label(root, text="Player 1's Name")
        label1.grid(row=1,column = 0)
        label2 = tk.Label(root, text="Player 2's Name")
        label2.grid(row=2,column = 0)
        label3 = tk.Label(root, text="Number of Shells")
        label3.grid(row=3,column = 0)
        label4 = tk.Label(root, text="Number of Holes")
        label4.grid(row=4,column = 0)

        e1 = tk.Entry(root)
        e2 = tk.Entry(root)
        e1.insert(10, "")
        e2.insert(10, "")

        e1.grid(row=1, column=1)
        e2.grid(row=2, column=1)


        play_btn = tk.Button(root, text='PLAY', command=game_start)
        play_btn.grid(row=7,column=1,sticky=tk.W,pady=4)

        ##Number of holes
        OPTIONS=[]
        for i in range(2,30):
            OPTIONS.append(i)

        hole_no = tk.StringVar(root)
        hole_no.set(OPTIONS[0]) # default value

        hole_drop = tk.OptionMenu(root, hole_no, *OPTIONS)
        hole_drop.grid(row=4,column=1)

        ##number of seeds
        OPTIONS = []
        for i in range(1,30):
            OPTIONS.append(i)

        seed_no = tk.StringVar(root)
        seed_no.set(OPTIONS[0]) # default value

        seed_drop = tk.OptionMenu(root, seed_no, *OPTIONS)
        seed_drop.grid(row=3,column=1)

        #second player option
        OPTIONS = [
            "Human",
            "Low Level AI",
            "Normal Level AI"
        ] #etc

        oppo_option = tk.StringVar(root)
        oppo_option.set(OPTIONS[0]) # default value

        oppo_drop = tk.OptionMenu(root, oppo_option, *OPTIONS)
        oppo_drop.grid(row=2,column = 2)

        root.mainloop()

#######################################################################
    def createBoard(self,player_name,oppo_name,oppo_player,holes,seeds):

        #choose if opponent is human, or ai
        # 1 = human
        # 2 = low level ai
        # 3 = normal level ai

        congkak = Congkak_algorithm(0,0,player_name,oppo_name,oppo_player,holes,seeds)
        board_length = len(congkak.get_board()[1][:])

        label_list = [[] for i in range(2)]

        for row in range(2):
            for col in range(len(congkak.get_board()[row,:])):
                label = tk.Label(root, text = congkak.get_board()[row][col] ,
                                 font = 50,borderwidth =1)
                label.grid(row=row+2,column=col)
                label_list[row].append(label)

        #print(label_list[1])


        # can update board and label
        def update_all():

            ai = Ai_player(congkak.has_available_move(1),congkak.get_board(),holes,seeds)
            inputMove = text_box.get()
            input_msg = ""

            if not inputMove \
            or re.search("[a-zA-Z\W]+", inputMove) \
            or not 0<=int(inputMove)< board_length :
                if congkak.get_current_player() == 0:
                    input_msg = str("(Player 1)"+congkak.get_player_name()+',please enter '+str(congkak.has_available_move(0))+':')
                elif congkak.get_current_player() == 1:
                    input_msg = str("(Player 2)"+ congkak.get_oppo_name()+',please enter '+str(congkak.has_available_move(1))+':')
                another_label.config(text = input_msg,foreground ="red")

            # check select hole not 0
            elif congkak.get_board()[congkak.get_row(),int(inputMove)] == 0:
                if congkak.get_current_player() == 0:
                    input_msg = str("(Player 1)"+congkak.get_player_name()+',please select valid and non-zero hole '+ str(congkak.has_available_move(0))+':')
                elif congkak.get_current_player() == 1:
                    input_msg = str("(Player 2)"+congkak.get_oppo_name()+',please select valid and non-zero hole '+ str(congkak.has_available_move(1))+':')
                another_label.config(text=input_msg,foreground = "red")

            else:
                move = int(inputMove)

                # player 1
                if congkak.get_current_player()== 0:
                    print("--------------",congkak.get_player_name()," turn:-----------------------")
                    congkak.player_play_game(move)

                # other manual player
                elif congkak.get_current_player() == 1:
                    print("--------------",congkak.get_oppo_name()," turn:-----------------------")
                    congkak.opponent_play_game(move)

                if congkak.get_current_player() == 0:
                    input_msg = str("(Player 1)"+congkak.get_player_name()+',please enter '+str(congkak.has_available_move(congkak.get_row()))+':')
                elif congkak.get_current_player() == 1:
                    input_msg = str("(Player 2)"+congkak.get_oppo_name()+',please enter '+str(congkak.has_available_move(congkak.get_row()))+':')
                another_label.config(text = input_msg,foreground = "black")

            ## ai part
            # low level ai
            if congkak.get_current_player() == 2:
                row = 1
                print("--------------",congkak.get_oppo_name()," turn:-----------------------")
                generated_move = ai.low_level_algorithm()
                print("move selected:",generated_move)
                congkak.opponent_play_game(generated_move)
                print("move selected:",generated_move)
            # high level ai
            elif congkak.get_current_player() == 3:
                row = 1
                print("--------------",congkak.get_oppo_name()," turn:-----------------------")
                generated_move = ai.normal_level_algorithm()
                print("move selected:",generated_move)
                congkak.opponent_play_game(generated_move)
                print("move selected:",generated_move)

            # update the row
            for row in range(2):
                for col in range(len(congkak.get_board()[row][:])):
                    label_list[row][col].config(text = congkak.get_board()[row][col])


            ## where we start updating labels
            update_player_score_msg = str("(Player 1)"+congkak.get_player_name()+" score:" + str(congkak.get_player_score()))
            update_oppo_score_msg = str("(Player 2)"+congkak.get_oppo_name()+" score:"+ str(congkak.get_oppo_score()))

            if congkak.get_current_player() == 0:
                input_msg = str("(Player 1)"+congkak.get_player_name()+',please enter '+str(congkak.has_available_move(congkak.get_row()))+':')
            elif congkak.get_current_player() == 1:
                input_msg = str("(Player 2)"+congkak.get_oppo_name()+',please enter '+str(congkak.has_available_move(congkak.get_row()))+':')
            another_label.config(text = input_msg)

            player_1_label.config(text = update_player_score_msg)
            player_2_label.config(text = update_oppo_score_msg)

            ##empty textbox after it have been submitted
            text_box.delete(0, tk.END)

            ##check if game ended or not
            if not congkak.check_empty():
                if congkak.get_player_score() > congkak.get_oppo_score():
                    winner_msg = ("(Player 1)"+str(congkak.get_player_name())+" have won!")
                elif congkak.get_player_score() < congkak.get_oppo_score():
                    winner_msg = ("(Player 2)"+str(congkak.get_oppo_name())+" have won!")
                else:
                    winner_msg = "Its a tie"
                another_label.config(text=winner_msg)
                submit_btn.config(state='disable')
                return



        input_msg = str("(Player 1)"+congkak.get_player_name()+',please enter '+str(congkak.has_available_move(congkak.get_row()))+':')
        player_score_msg = str("(Player 1)"+congkak.get_player_name()+" score:" + str(congkak.get_player_score()))
        oppo_score_msg = str("(Player 2)"+congkak.get_oppo_name()+" score:"+ str(congkak.get_oppo_score()))
        oppo_type_msg = ""

        player1_row = tk.Label(root,text = "<---"+congkak.get_player_name()+"`s row---",font = 5)
        player2_row = tk.Label(root,text = "---"+congkak.get_oppo_name()+"`s row--->",font = 5)
        another_label = tk.Label(root,text = input_msg,font = 6,height = 3,borderwidth =2,padx = 2)

        if oppo_player == 1:
            oppo_type_msg = "Human"
        elif oppo_player == 2:
            oppo_type_msg = "Low Level AI"
        elif oppo_player == 3:
            oppo_type_msg = "Normal Level AI"

        player_type = tk.Label(root,text = "Playing with player 2: "+oppo_type_msg,font = 5)
        player_1_label = tk.Label(root,text = player_score_msg , font = 5)
        player_2_label = tk.Label(root, text = oppo_score_msg,font = 5)

        text_box = tk.Entry(root,bd = 5)
        submit_btn = tk.Button(root, text = "submit",command=update_all)

        player1_row.grid(row = 1,columnspan = board_length)
        player2_row.grid(row =4,columnspan =board_length)

        another_label.grid(row = 5,column = 0 ,columnspan = 30)
        text_box.grid(row = 6,column = 0 ,columnspan = 30)
        submit_btn.grid(row =7, column =0,columnspan = 30)
        player_1_label.grid(row = 8,column = 0,columnspan = 30)
        player_2_label.grid(row = 9,column = 0 , columnspan = 30)
        player_type.grid(row = 10,column =0,columnspan = 30)

def main():
    board = Board_GUI(root)

main()
