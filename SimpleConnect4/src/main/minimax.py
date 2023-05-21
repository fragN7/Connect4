import math
import random


class MiniMax:

    @staticmethod
    def evaluate_window(window, turn):
        score = 0
        opp_piece = 1
        if turn == 1:
            opp_piece = 2
        if window.count(turn) == 4:
            score += 100
        elif window.count(turn) == 3 and window.count(0) == 1:
            score += 5
        elif window.count(turn) == 2 and window.count(0) == 2:
            score += 2
        if window.count(opp_piece) == 3 and window.count(0) == 1:
            score -= 4

        return score

    def score_position(self, board, turn):
        score = 0

        center_array = [int(i) for i in list(board[:, 7 // 2])]
        center_count = center_array.count(turn)
        score += center_count * 3

        for r in range(6):
            row_array = [int(i) for i in list(board[r, :])]
            for c in range(4):
                window = row_array[c:c + 4]
                score += self.evaluate_window(window, turn)

        for c in range(7):
            col_array = [int(i) for i in list(board[:, c])]
            for r in range(3):
                window = col_array[r:r + 4]
                score += self.evaluate_window(window, turn)

        for r in range(3):
            for c in range(4):
                window = [board[r + i][c + i] for i in range(3)]
                score += self.evaluate_window(window, turn)

        for r in range(3):
            for c in range(4):
                window = [board[r + 3 - i][c + i] for i in range(3)]
                score += self.evaluate_window(window, turn)

        return score

    def is_terminal_node(self, board):
        return self.winning_move(board, 1) or self.winning_move(board, 2) or \
               not len(self.get_valid_locations(board))

    @staticmethod
    def winning_move(board, turn):
        for c in range(4):
            for r in range(6):
                if board[r][c] == turn and board[r][c+1] == turn and \
                        board[r][c+2] == turn and board[r][c+3] == turn:
                    return True

        for c in range(7):
            for r in range(3):
                if board[r][c] == turn and board[r+1][c] == turn and \
                        board[r+2][c] == turn and board[r+3][c] == turn:
                    return True

        for c in range(4):
            for r in range(3):
                if board[r][c] == turn and board[r+1][c+1] == turn and \
                        board[r+2][c+2] == turn and board[r+3][c+3] == turn:
                    return True

        for c in range(4):
            for r in range(3, 6):
                if board[r][c] == turn and board[r-1][c+1] == turn and \
                        board[r-2][c+2] == turn and board[r-3][c+3] == turn:
                    return True
        return False

    @staticmethod
    def update_board(board, row, move, turn):
        board[row][move] = turn

    @staticmethod
    def is_valid(board, move):
        return board[5][move] == 0

    def get_valid_locations(self, board):
        valid_locations = []
        for move in range(7):
            if self.is_valid(board, move):
                valid_locations.append(move)
        return valid_locations

    @staticmethod
    def get_row(board, move):
        for i in range(6):
            if board[i][move] == 0:
                return i

    def algorithm(self, board, depth, alpha, beta, ai):
        valid_locations = self.get_valid_locations(board)
        is_terminal = self.is_terminal_node(board)
        if depth == 0 or is_terminal:
            if is_terminal:
                if self.winning_move(board, 2):
                    return None, 100000000000000
                elif self.winning_move(board, 1):
                    return None, -10000000000000
                else:
                    return None, 0
            else:
                return None, self.score_position(board, 2)
        if ai:
            value = -math.inf
            column = random.choice(valid_locations)
            for c in valid_locations:
                r = self.get_row(board, c)
                board_copy = board.copy()
                self.update_board(board_copy, r, c, 2)
                new_score = self.algorithm(board_copy, depth - 1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = c
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value
        else:
            value = math.inf
            column = random.choice(valid_locations)
            for c in valid_locations:
                r = self.get_row(board, c)
                board_copy = board.copy()
                self.update_board(board_copy, r, c, 1)
                new_score = self.algorithm(board_copy, depth - 1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = c
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value
