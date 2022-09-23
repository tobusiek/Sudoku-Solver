class Board:
    def __init__(self, board: list[list[int]]) -> None:
        self._current_board = board
    

    def __str__(self) -> str:
        if not self._current_board:
            raise ValueError('No board presented')

        board_str = '\nCurrent board:\n'
        for row in range(9):
            for col in range(9):
                board_str += str(self._current_board[row][col]) + ' '
                if (col+1) % 3 == 0 and col != 8:
                    board_str += '| '

            board_str = board_str[:-1] + '\n'
            if (row+1) % 3 == 0 and row != 8:
                board_str += '---------------------\n'
        
        return board_str


class BoardValidator:
    def __init__(self, board: Board) -> None:
        self._board = board

    
    def _valid_rows_digits(self) -> bool:
        for i in range(9):
            row_digits = [digit for digit in self._board[i] if digit != 0]
            if len(row_digits) != len(set(row_digits)):
                print(f'Some digits are not unique in row {i+1}')
                return False

        return True
    

    def _valid_cols_digits(self) -> bool:
        boardT = list(map(list, zip(*self._board)))

        for i in range(9):
            row_digits = [digit for digit in boardT[i] if digit != 0]
            if len(row_digits) != len(set(row_digits)):
                print(f'Some digits are not unique in column {i+1}')
                return False
        
        return True

    
    def _valid_squares_digits(self) -> bool:
        return True

    
    def valid_board(self) -> bool:
        if not self._valid_rows_digits():
            return False
        
        if not self._valid_cols_digits():
            return False
        
        if not self._valid_squares_digits():
            return False
        
        return True
