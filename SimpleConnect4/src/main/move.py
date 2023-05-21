class Move:

    def __init__(self, the_board, valid_move):
        self.board = the_board
        self.valid_move = valid_move

    def enter_move(self, move, turn):
        """
        Validates the move and if it is valid, updates the board by putting it in
        """
        if self.valid_move.check(move):
            self.board.update_board(move, turn)

    def is_draw(self):
        """
        If no valid locations occur, means that the board is full and no one
        won(everytime we check for a move we check if is a winning move)
        """
        valid_locations = self.valid_move.get_valid_locations()
        if valid_locations:
            return False
        return True

    def winning_move(self, turn):
        """
        Checks for win on columns
        """
        for c in range(4):
            for r in range(6):
                if self.board.get_element(r, c) == turn and self.board.get_element(r, c + 1) == turn and \
                        self.board.get_element(r, c + 2) == turn and self.board.get_element(r, c + 3) == turn:
                    return True

        """
        Checks for win on rows
        """

        for c in range(7):
            for r in range(3):
                if self.board.get_element(r, c) == turn and self.board.get_element(r + 1, c) == turn and \
                        self.board.get_element(r + 2, c) == turn and self.board.get_element(r + 3, c) == turn:
                    return True

        """
        Checks for win on primary diagonals
        """

        for c in range(4):
            for r in range(3):
                if self.board.get_element(r, c) == turn and self.board.get_element(r + 1, c + 1) == turn and \
                        self.board.get_element(r + 2, c + 2) == turn and self.board.get_element(r + 3, c + 3) == turn:
                    return True

        """
        Checks for win on secondary diagonals
        """

        for c in range(4):
            for r in range(3, 6):
                if self.board.get_element(r, c) == turn and self.board.get_element(r - 1, c + 1) == turn and \
                        self.board.get_element(r - 2, c + 2) == turn and self.board.get_element(r - 3, c + 3) == turn:
                    return True
        return False
