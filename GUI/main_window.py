# Used to layout and describe main window
# Also used to handle events from widgets, etc.
from tkinter import *
from tkinter import ttk

class MainWindow:
    def __init__(self, root: Tk):
        # Main window
        root.title("Chess")
        root.geometry("500x300")
        root.rowconfigure(0, weight= 1)
        root.columnconfigure(0, weight = 1)

        mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # Mainframe layout
        mainframe.rowconfigure(0, weight= 1)
        mainframe.columnconfigure(0, weight=1)

        # Chess table
        # Canvas
        canvas_width = 550
        canvas_height = 500
        self.board_rows = 8
        self.board_cols = 8
        self.canvas = Canvas(mainframe, width=canvas_width, height=canvas_height, bg="white")
        self.canvas.grid(column= 0, row = 0, columnspan= 8, sticky = (N, W, E, S))

        # rows = [
        #     ("\u265C", "\u265E", "\u265D", "\u265B", "\u265A", "\u265D", "\u265E", "\u265C"),
        #     ("\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F"),
        #     ("", "", "", "", "", "", "", ""),
        #     ("", "", "", "", "", "", "", ""),
        #     ("", "", "", "", "", "", "", ""),
        #     ("", "", "", "", "", "", "", ""),
        #     ("\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659"),
        #     ("\u2656", "\u2658", "\u2657", "\u2655", "\u2654", "\u2657", "\u2658", "\u2656")
        # ]

        