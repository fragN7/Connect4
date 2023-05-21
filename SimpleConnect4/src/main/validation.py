from src.main.errors import ValidError


class Validation:

    def __init__(self, board):
        self.board = board

    def check(self, move):
        err = ""
        if move not in range(0, 7):
            err = "Not a valid column"
        if err == "":
            if self.board.get_element(5, move):
                err = "Column already full"
        if len(err) > 0:
            raise ValidError(err)
        return True

    def get_valid_locations(self):
        valid_locations = []
        for i in range(7):
            try:
                if self.check(i):
                    valid_locations.append(i)
            except ValidError:
                continue
        return valid_locations
