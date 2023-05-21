import unittest
import numpy
from src.main.board import Board
from src.main.validation import Validation
from src.main.move import Move
from src.main.errors import ValidError


class TestsMove(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.validation = Validation(self.board)
        self.move = Move(self.board, self.validation)

    def testEnterMove(self):
        move = 4
        turn = 1
        self.move.enter_move(move, turn)

        element = self.board.get_element(0, move)
        self.assertEqual(element, turn)

    def testIsDraw(self):

        board = self.board.get_board()
        print(board)

        result = self.move.is_draw()
        self.assertEqual(result, False)

        for i in range(6):
            for j in range(7):
                board[i][j] = 3

        result = self.move.is_draw()
        self.assertEqual(result, True)

    def testWinningMove(self):
        board = self.board.get_board()
        turn = 1

        result = self.move.winning_move(turn)
        self.assertEqual(result, False)

        for j in range(4):
            board[0][j] = turn

        result = self.move.winning_move(turn)
        self.assertEqual(result, True)

        for j in range(4):
            board[0][j] = 0

        for i in range(4):
            board[i][0] = turn

        result = self.move.winning_move(turn)
        self.assertEqual(result, True)

        for i in range(4):
            board[i][0] = 0

        for i in range(4):
            board[i][i] = turn

        result = self.move.winning_move(turn)
        self.assertEqual(result, True)

        for i in range(4):
            board[i][i] = 0

        board[0][6] = turn
        board[1][5] = turn
        board[2][4] = turn
        board[3][3] = turn

        result = self.move.winning_move(turn)
        self.assertEqual(result, True)


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def testSetBoard(self):
        some_board = numpy.zeros((6, 7))
        self.board.set_board(some_board)

        self.assertEqual(self.board.get_board().all(), some_board.all())

    def testGetRow(self):
        board = self.board.get_board()
        board[0][0] = 1
        board[1][0] = 1

        result = self.board.get_row(0)
        self.assertEqual(result, 2)


class TestValidation(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.valid = Validation(self.board)

    def testCheck(self):
        move = 9
        with self.assertRaises(ValidError) as ve:
            self.valid.check(move)
        self.assertEqual(str(ve.exception), "Not a valid column")


if __name__ == '__main__':
    unittest.main()
