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
        root.columnconfigure(0, weight= 1)

        mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.rowconfigure(0, weight= 1)
        mainframe.columnconfigure(0, weight = 1)

        # Chess table
        columns = ("A", "B", "C", "D", "E", "F", "G", "H")
        table = ttk.Treeview(mainframe, columns=columns, show="headings", height=8)
        table.grid(column = 0, row = 0, sticky = (N,S,E,W))

        # Table headings TODO
        for heading in columns:
            table.heading(heading, text= heading)

        rows = [
            ("\u265C", "\u265E", "\u265D", "\u265B", "\u265A", "\u265D", "\u265E", "\u265C"),
            ("\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F"),
            ("", "", "", "", "", "", "", ""),
            ("", "", "", "", "", "", "", ""),
            ("", "", "", "", "", "", "", ""),
            ("", "", "", "", "", "", "", ""),
            ("\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659"),
            ("\u2656", "\u2658", "\u2657", "\u2655", "\u2654", "\u2657", "\u2658", "\u2656")
        ]
        for row in rows:
            table.insert("", "end", values=row)

        