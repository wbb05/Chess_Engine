"""
GUI:
Have chess board

Header with info
[] [] [] [] ...
[] [] [] [] ...
[] ...
.
.
Footer with Reset/Exit

Select box, can move piece
Backend, move piece, show if move is illegal
Show possible moves?

Game:
Need states, possible actions, resulting state from actions, reward of taking action from s to s'

Chess Engine:
Start MCTS, prob need to do RL

"""
from tkinter import Tk
from GUI import MainWindow

if __name__ == "__main__":
    # Start GUI
    root = Tk()
    MainWindow(root)
    root.mainloop()