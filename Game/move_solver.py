# This module calculates a set of move actions for a given bitboard
# Pawn attack is defined as generic attacks without enemy pieces and specific attacks with enemy pieces

# Constants
FILE_A = 0x8080808080808080
FILE_H = 0x0101010101010101

FILE_AB = FILE_A | (FILE_A >> 1)
FILE_GH = FILE_H | (FILE_H << 1)

RANK_2 = 0x000000000000FF00
RANK_7 = 0x00FF000000000000

# Class
class MoveSolver:
    @staticmethod
    def white_pawn_move(bitboard):
        return bitboard << 8 | ((bitboard & RANK_2) << 16)

    @staticmethod
    def white_pawn_attack(bitboard, enemy_bitboard= 0xFFFFFFFFFFFFFFFF):
        return (((bitboard & ~FILE_A) << 9) | ((bitboard & ~FILE_H) << 7)) & enemy_bitboard

    @staticmethod
    def black_pawn_move(bitboard):
        return bitboard >> 8 | ((bitboard & RANK_7) >> 16)

    @staticmethod
    def black_pawn_attack(bitboard, enemy_bitboard= 0xFFFFFFFFFFFFFFFF):
        return (((bitboard & ~FILE_A ) >> 7) | ((bitboard & ~FILE_H) >> 9)) & enemy_bitboard

    @staticmethod
    def knight_move(bitboard):
        return ( ((bitboard & ~FILE_A) << 17) | ((bitboard & ~FILE_H) << 15) 
                              | ((bitboard & ~FILE_AB) << 10) | ((bitboard & ~FILE_GH) << 6)
                              | ((bitboard & ~FILE_AB) >> 6) | ((bitboard & ~FILE_GH) >> 10)
                              | ((bitboard & ~FILE_A) >> 15) | ((bitboard & ~FILE_H) >> 17))

    @staticmethod
    def king_move(bitboard):
        return (((bitboard & ~FILE_A) << 9) | (bitboard << 8) | ((bitboard & ~FILE_H) << 7)
                             | ((bitboard & ~FILE_A) << 1) | ((bitboard & ~FILE_H) >> 1)  
                             | ((bitboard & ~FILE_A) >> 7) | (bitboard >> 8) | (bitboard & ~FILE_H) >> 9)
