import tkinter as tk
import numpy as np


root = tk.Tk()

def allOne():
    print("TED")

class Board_GUI(tk.Frame):

    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        self.createBoard(root)

    def createBoard(self,root):

        def test():
            grid =np.zeros((2,7),dtype=int)
            grid[:,0:7] = 12
            frame_grid.config(text="123")

        ## way to show the gui
        root.title("Congkak")
        root.resizable(width=100,height=100)
        labelfont = (20) # applies to every font in the game

        board = np.zeros((2,7),dtype= int)
        board[:,0:7] = 7
        board[1,1] = 1


        simple_label = tk.Label(root,text="Congkak game")
        simple_label.config(font = labelfont)
        closing_btn=tk.Button(root,text="Close",command=test)

        simple_label.grid(row=0,columnspan = 7)
        closing_btn.grid(row=6,columnspan=7)

        ##for row in range(1,3):
            ##for column in range(7):
        global frame_grid
        ##currentValue = board[row-1,column-1]
        frame_grid = tk.Label(root,fg="black",text="HEY")
        frame_grid.config(height=3, width=5)
        frame_grid.config(font=labelfont)
        ##frame_grid.grid(row=row,column=column)
        frame_grid.grid(row=2)


def main():
    board = Board_GUI(root)
    root.mainloop()

main()
