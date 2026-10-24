# Generates moves for pawns, knights, and kings
# Save to JSON file

import json

from state import GameState

FILE_A = 0x8080808080808080
FILE_H = 0x0101010101010101

FILE_AB = FILE_A | (FILE_A >> 1)
FILE_GH = FILE_H | (FILE_H << 1)

RANK_2 = 0x000000000000FF00
RANK_7 = 0x00FF000000000000

# Start with pawns

white_pawns_move = {}
white_pawns_attack = {}

black_pawns_move = {}
black_pawns_attack = {}

king_move = {}

knight_move = {}

for cell_index in range(0, 64):
    start_state = 1 << cell_index # ...010... bitboard for cell

    # White pawns
    # Right now doesn't handle invalid row
    # North one row, two if at starting position
    # TODO: Promotion, en passent?
    white_pawns_move[cell_index] = start_state << 8 | ((start_state & RANK_2) << 16)
    white_pawns_attack[cell_index] = ((start_state & ~FILE_A) << 9) | ((start_state & ~FILE_H) << 7)

    black_pawns_move[cell_index] = start_state >> 8 | ((start_state & RANK_7) >> 16)
    black_pawns_attack[cell_index] = ((start_state & ~FILE_A ) >> 7) | ((start_state & ~FILE_H) >> 9)

    # King movements
    king_move[cell_index] = (((start_state & ~FILE_A) << 9) | (start_state << 8) | ((start_state & ~FILE_H) << 7)
                             | ((start_state & ~FILE_A) << 1) | ((start_state & ~FILE_H) >> 1)  
                             | ((start_state & ~FILE_A) >> 7) | (start_state >> 8) | (start_state & ~FILE_H) >> 9)

    # Knight movements
    knight_move[cell_index] = ( ((start_state & ~FILE_A) << 17) | ((start_state & ~FILE_H) << 15) 
                              | ((start_state & ~FILE_AB) << 10) | ((start_state & ~FILE_GH) << 6)
                              | ((start_state & ~FILE_AB) >> 6) | ((start_state & ~FILE_GH) >> 10)
                              | ((start_state & ~FILE_A) >> 15) | ((start_state & ~FILE_H) >> 17))


# Save to JSON file
main_dict = {}
main_dict["white_pawns_move"] = white_pawns_move
main_dict["white_pawns_attack"] = white_pawns_attack
main_dict["black_pawns_move"] = black_pawns_move
main_dict["black_pawns_attack"] = black_pawns_attack
main_dict["king_move"] = king_move
main_dict["knight_move"] = knight_move

with open("non_sliding_tables.json", 'w') as file:
    json.dump(main_dict, file)