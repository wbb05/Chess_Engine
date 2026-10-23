# Used to layout and describe main window
# Also used to handle events from widgets, etc.
from tkinter import *
from tkinter import ttk
from math import floor
from enum import Enum

# Player enum
# TODO: For now, GUI doesn't handle turns
class Player(Enum):
    NONE = 0
    WHITE = 1
    BLACK = 2
    

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

        # Create chessboard
        self.init_canvas(mainframe)

        self.init_player_fsm()

        # Bind button click on canvas to selected in region
        self.canvas.bind("<ButtonPress-1>", self.cell_selected)

    # Creates chessboard
    def init_canvas(self, mainframe):
        # Chess table
        # Canvas
        self.canvas_width = 500
        self.canvas_height = 500
        self.board_rows = 8
        self.board_cols = 8
        self.canvas = Canvas(mainframe, width=self.canvas_width, height=self.canvas_height, bg="white")
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

        # Dict mapping location to text at that location
        self.canvas_text = {}
        color_square = False
        offset = self.canvas_width / self.board_cols / 2 # Should be same for rows and cols
        x = offset
        y = offset
        for row_i,row in enumerate(chess_pieces):
            for piece in row:
                # Color square
                if not color_square: self.canvas.create_rectangle(x - offset, y - offset, x + offset, y + offset, fill= "green")
                color_square = not color_square

                # Place chess piece
                # Also store text id and type of piece
                text_id = self.canvas.create_text(x, y, text= piece, font= ("Arial", 30))

                if row_i < 2: player = Player.BLACK
                elif row_i > 5: player = Player.WHITE
                else: player = Player.NONE
                self.canvas_text[(x,y)] = (text_id, player)

                x += self.canvas_width / self.board_cols
                
            y += self.canvas_height / self.board_rows
            x = offset
            color_square = not color_square

    # Starts game FSM, where players take turns
    def init_player_fsm(self):
        self.is_piece_selected = False # Whether player is actively moving a piece
        self.piece_selected_pos = (0,0) # Selected piece

    def cell_selected(self, event):
        # Find text location from event location
        offset = self.canvas_width / self.board_cols
        text_x = floor(event.x / offset) * (offset) + offset/2
        text_y = floor(event.y / offset) * (offset) + offset/2

        # Call FSM to determine action
        self.player_move(text_x, text_y)

        
    def player_move(self, x, y):
        # Find text at location
        text_id, player = self.canvas_text[(x, y)]

        # If actively moving, move there
        if self.is_piece_selected:

            # Find old piece info
            old_text_id, old_player = self.canvas_text[self.piece_selected_pos]
            piece = self.canvas.itemcget(old_text_id, 'text')

            # Remove from old pos
            self.canvas.itemconfigure(old_text_id, text= "")
            self.canvas_text[self.piece_selected_pos] = (old_text_id, Player.NONE)

            # Add to new pos
            self.canvas.itemconfigure(text_id, text= piece)
            self.canvas_text[(x,y)] = (text_id, old_player)

            # Reset for next move
            self.is_piece_selected = False

        # Else if not actively moving, choose selected piece
        elif not self.is_piece_selected and player != Player.NONE:
            self.piece_selected_pos = (x,y)
            self.is_piece_selected = True

        # Else, invalid move, no action taken
        
        

        