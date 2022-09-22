class Board:
    def __init__(self, board) -> None:
        self.current_board = board


class BoardValidator:
    def __init__(self, board: Board) -> None:
        self.board = board

    
    def valid_row_digits(self):
        return True


    def valid_row_input(self):
        return True
