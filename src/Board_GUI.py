import tkinter as tk
import numpy as np


root = tk.Tk()

def allOne():
    print("TED")

class Board_GUI(tk.Frame):

    return_move = 0

    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        self.createBoard(root)

    def createBoard(self,root):

        inputMove = tk.StringVar(root)

        def test():
            returnMove = int(inputMove.get())

        ## way to show the gui
        root.title("Congkak")
        root.resizable(width=100,height=100)
        labelfont = (20) # applies to every font in the game


        text_box = tk.Entry(root,textvariable = inputMove)


        simple_label = tk.Label(root,text="Congkak game")
        simple_label.config(font = labelfont)

        closing_btn=tk.Button(root,text="Close",command = test)

        simple_label.grid(row=0,columnspan = 7)
        text_box.grid(row = 1,columnspan=7)
        closing_btn.grid(row=6,columnspan=7)


def main():
    board = Board_GUI(root)
    root.mainloop()
    print(board.get_move())

main()
