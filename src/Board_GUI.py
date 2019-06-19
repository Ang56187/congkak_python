import tkinter as tk
import numpy as np
from Congkak_algorithm import Congkak_algorithm


root = tk.Tk()

def allOne():
    print("TED")

class Board_GUI(tk.Frame):

    counter = 0

    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        self.createBoard(root)

    def createBoard(self,root):

        congkak = Congkak_algorithm(0,0,"Noobmaster","Thor",1,5,5)

        for row in range(2):
            for col in range(len(congkak.get_board()[row,:])-1):
                label = tk.Label(root, text = self.counter ,borderwidth=1 )
                label.grid(row=row,column=col)


        input_msg = tk.StringVar()
        input_msg.set("hey")

        another_label = tk.Label(root,text = "placeholder",borderwidth =1)

        def update():
            self.counter+=1
            print(self.counter)
            list = []
            self.list = [[5,5,5,5],[5,5,5,5]]
            congkak.set_board(list)

        def update_all():
            root.after(100,update_all)

        button_test = tk.Button(root, text = "submit",command=update)

        another_label.grid(row = 3,column = 0 ,columnspan = 4)
        button_test.grid(row =4, column =0,columnspan = 4)

        root.update_idletasks()
        root.mainloop()


            #
            # list = []
            # self.list = np.zeros((2,5),dtype=int)
            # congkak.set_board(list)

def main():
    board = Board_GUI(root)
    board.createBoard()

main()
