from __future__ import print_function
import re
import sys
import time
from itertools import count
from collections import namedtuple
from pprint import pprint


start_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"


# Lists of possible moves for each piece type.
N, E, S, W = -10, 1, 10, -1
directions = {
    'P': (N, N + N, N + W, N + E),
    'N': (N + N + E, E + N + E, E + S + E, S + S + E, S + S + W, W + S + W, W + N + W, N + N + W),
    'B': (N + E, S + E, S + W, N + W),
    'R': (N, E, S, W),
    'Q': (N, E, S, W, N + E, S + E, S + W, N + W),
    'K': (N, E, S, W, N + E, S + E, S + W, N + W)
}


board = (
    '         \n'  # 0 -  9
    '         \n'  # 10 - 19
    ' rnbqkbnr\n'  # 20 - 29
    ' pppppppp\n'  # 30 - 39
    ' ........\n'  # 40 - 49
    ' ........\n'  # 50 - 59
    ' ........\n'  # 60 - 69
    ' ........\n'  # 70 - 79
    ' PPPPPPPP\n'  # 80 - 89
    ' RNBQKBNR\n'  # 90 - 99
    '         \n'  # 100 -109
    '         \n'  # 110 -119
)


class move:

    def __init__(self, board):
        self.board = board

    def fen_to_board(self, fen):
        board = []
        for row in fen.split('/'):
            # print(row)
            board_row = []
            for ch in row:
                # print(ch)
                if ch in '123456789':
                    board_row.extend('-' * int(ch))
                else:
                    board_row.append(ch)
            board.append(board_row)
        return board

    def move_pawn(self, fen, board):
        for i in enumerate(board):
        	
                # print(i[0])
            if i[0] == 'P':

                for j in directions[i]:

                    if j % 10 != 0 and board[j].islower:
                        print(i)
                        print(j)
                        yield(i[0], j)
                    elif board[j] == '.':
                        print(i)
                        print(j)
                        yield(i[0], j)

    # def main():
    # print(move_pawn(start_fen, board))


# ob = move([])
# pprint(ob.fen_to_board(start_fen))
if __name__ == "__main__":
    ob = move([])

    lis = ob.move_pawn(start_fen, board)
    for it in lis:
        print(it)
