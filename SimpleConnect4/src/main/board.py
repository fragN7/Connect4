import numpy


class Board:

    def __init__(self):
        self.board = numpy.zeros((6, 7))

    def update_board(self, move, turn):
        for i in range(6):
            if self.board[i][move] == 0:
                self.board[i][move] = turn
                return

    def get_board(self):
        return self.board[:]

    def set_board(self, other_board):
        self.board = other_board[:]

    def get_row(self, column):
        for i in range(6):
            if self.board[i][column] == 0:
                return i

    def get_element(self, row, column):
        return self.board[row][column]

    def print_board(self):
        print(numpy.flip(self.board, 0))
