from config import *


class Board:
    def __init__(self):

        self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0]]

        self.board[3][4] = BLACK
        self.board[4][3] = BLACK
        self.board[3][3] = WHITE
        self.board[4][4] = WHITE
        self.valid_moves = []

    def __getitem__(self, i, j):
        return self.board[i][j]


    def print_board(self):
        for i in range(8):
            print(i, ' |', end=' ')
            for j in range(8):
                if self.board[i][j] == BLACK:
                    print('B', end=' ')
                elif self.board[i][j] == WHITE:
                    print('W', end=' ')
                else:
                    print(' ', end=' ')
                print('|', end=' ')
            print()


    def count_stones(self):
        """ Returns the number of white pieces, black pieces and empty squares, in
        this order.
        """
        whites = 0
        blacks = 0
        empty = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == WHITE:
                    whites += 1
                elif self.board[i][j] == BLACK:
                    blacks += 1
                else:
                    empty += 1
        return whites, blacks, empty