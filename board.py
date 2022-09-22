class Board:
    def __init__(self, board) -> None:
        self.current_board = board
    

    def __str__(self) -> str:
        if not self.current_board:
            raise ValueError('No board presented')

        board_str = '\nCurrent board:\n'
        for row in range(9):
            for col in range(9):
                board_str += str(self.current_board[row][col]) + ' '
            board_str += '\n'
        return board_str


class BoardValidator:
    def __init__(self, board: Board) -> None:
        self.board = board

    
    def valid_row_digits(self):
        return True


    def valid_row_input(self):
        return True
