class Board:
    def __init__(self, board: list[list[int]]) -> None:
        self._cur_board = board
    

    @property
    def current_board(self) -> list[list[int]]:
        return self._cur_board


    def __str__(self) -> str:
        if not self._cur_board:
            raise ValueError('No board presented')

        board_str = '\nCurrent board:\n'
        for row in range(9):
            for col in range(9):
                board_str += str(self._cur_board[row][col]) + ' '
                if (col+1) % 3 == 0 and col != 8:
                    board_str += '| '

            board_str = board_str[:-1] + '\n'
            if (row+1) % 3 == 0 and row != 8:
                board_str += '---------------------\n'
        
        return board_str


class BoardValidator:
    def _valid_rows_digits(self, board: list[list[int]]) -> bool:
        for i in range(9):
            row_digits = [d for d in board[i] if d != 0]

            if len(row_digits) != len(set(row_digits)):
                print(f'Some digits are not unique in row {i+1}')
                return False

        return True
    

    def _valid_cols_digits(self, board: list[list[int]]) -> bool:
        boardT = list(map(list, zip(*board)))

        for i in range(9):
            row_digits = [d for d in boardT[i] if d != 0]
            if len(row_digits) != len(set(row_digits)):
                print(f'Some digits are not unique in column {i+1}')
                return False
        
        return True

    
    def _valid_squares_digits(self, board: list[list[int]]) -> bool:
        boxes = [[board[3*i+k][3*j+l]
            for k in range(3) for l in range(3)
            if board[3*i+k][3*j+l] != 0]
            for i in range(3) for j in range(3)]
        
        for i, box in enumerate(boxes):
            if len(box) != len(set(box)):
                print(f'Some digits are not unique in box {i+1}')
                return False

        return True

    
    def valid_board(self, board: list[list[int]]) -> bool:
        if not self._valid_rows_digits(board):
            return False
        
        if not self._valid_cols_digits(board):
            return False
        
        if not self._valid_squares_digits(board):
            return False
        
        return True
