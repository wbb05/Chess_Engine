# Used to layout and describe main window
# Also used to handle events from widgets, etc.
from tkinter import *
from tkinter import ttk

class MainWindow:
    def __init__(self, root: Tk):
        # Main window
        root.title("Chess")
        root.geometry("500x500")
        root.rowconfigure(0, weight= 1)
        root.columnconfigure(0, weight = 1)

        mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # Mainframe layout
        mainframe.rowconfigure(0, weight= 1)
        mainframe.columnconfigure(0, weight=1)

        # Chess table
        # Canvas
        canvas_width = 500
        canvas_height = 500
        self.board_rows = 8
        self.board_cols = 8
        self.canvas = Canvas(mainframe, width=canvas_width, height=canvas_height, bg="white")
        self.canvas.grid(column= 0, row = 0, columnspan= 8, sticky = (N, W, E, S))

        # Add chess pieces and color squares
        chess_pieces = [
            ("\u265C", "\u265E", "\u265D", "\u265B", "\u265A", "\u265D", "\u265E", "\u265C"),
            ("\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F"),
            ("", "", "", "", "", "", "", ""),
            ("", "", "", "", "", "", "", ""),
            ("", "", "", "", "", "", "", ""),
            ("", "", "", "", "", "", "", ""),
            ("\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659"),
            ("\u2656", "\u2658", "\u2657", "\u2655", "\u2654", "\u2657", "\u2658", "\u2656")
        ]

        color_square = False


        offset = canvas_width / self.board_cols / 2 # Should be same for rows and cols
        x = offset
        y = offset
        for row in chess_pieces:
            for piece in row:
                # Color square
                if not color_square: self.canvas.create_rectangle(x - offset, y - offset, x + offset, y + offset, fill= "green")
                color_square = not color_square

                # Place chess piece
                self.canvas.create_text(x, y, text= piece, font= ("Arial", 30))

                x += canvas_width / self.board_cols
                print(color_square, x, y) # DEBUG
                
            y += canvas_height / self.board_rows
            x = offset
            color_square = not color_square

        