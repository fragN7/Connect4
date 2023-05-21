from src.main.board import Board
from src.main.move import Move
from src.main.validation import Validation
from src.main.ui import UserInterface
from src.main.minimax import MiniMax


if __name__ == '__main__':
    board = Board()
    validation = Validation(board)
    move = Move(board, validation)
    minimax = MiniMax()
    us = UserInterface(board, move, minimax)
    us.run()
