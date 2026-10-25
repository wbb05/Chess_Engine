# Class for a game state
# Set of bitboards for each piece and player
# TODO: Right now just pawns

# Board:
# 63 62 61 60 59 58 57 56
# 55 ...
# ...
# 7 6 5 4 3 2 1 0

from enum import Enum

class Player(Enum):
    WHITE = 0
    BLACK = 1

class GameState:
    def __init__(self):
        self.white_pawns = 0x000000000000FF00
        self.black_pawns = 0x00FF000000000000

        self.current_player = Player.WHITE

    @staticmethod
    def print_state(bitboard):
        FILE_H = 0x0101010101010101
        cell = 1 << 63
        while cell:
            if bitboard & cell:
                print("1", end= " ")
            else:
                print("0", end=" ")

            if cell & FILE_H:
                print()

            cell = cell >> 1