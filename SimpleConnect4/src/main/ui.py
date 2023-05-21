import random
import math
from src.main.errors import ValidError


class UserInterface:

    def __init__(self, board, move, minimax):
        self.board = board
        self.service_move = move
        self.minimax = minimax

    def read_move(self, turn):
        move = int(input("Please enter a number 1-7")) - 1
        self.service_move.enter_move(move, turn)
        if self.service_move.winning_move(turn):
            return True
        return False

    def run(self):
        turn = random.randint(1, 2)
        self.board.print_board()
        while True:
            try:
                if turn == 1:
                    if self.read_move(turn):
                        self.board.print_board()
                        print(f"Player {turn} has won")
                        return
                    if self.service_move.is_draw():
                        print("Draw")
                        return
                    turn = 2
                    self.board.print_board()
                else:
                    save_board = self.board.get_board()
                    move = self.minimax.algorithm(save_board, 5, -math.inf, math.inf, True)[0]
                    self.service_move.enter_move(move, turn)
                    if self.service_move.winning_move(turn):
                        self.board.print_board()
                        print(f"Player {turn} has won")
                        return
                    if self.service_move.is_draw():
                        print("Draw")
                        return
                    turn = 1
                    self.board.print_board()
            except ValidError as ve:
                print(ve)
            except ValueError:
                print("Invalid input")
