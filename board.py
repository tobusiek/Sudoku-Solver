class Cell:
    """Class for single cell, its digit and possible digits if empty."""

    def __init__(self, digit: int = 0) -> None:
        self.digit = digit
        self._possible = set()

    @property
    def possible(self) -> set:
        """"""
        return self._possible

    def add_possible_digit(self, possible: int) -> None:
        """TODO"""
        self._possible.add(possible)

    def set_possible_digits(self, possible: set[int]) -> None:
        """TODO"""
        self._possible = possible

    def remove_from_possible(self, not_possible: int) -> None:
        """TODO"""
        self._possible.remove(not_possible)

    def __str__(self) -> str:
        return str(self.digit)


class Board:
    """Class for sudoku board with 81 cells."""

    def __init__(self, cells: list[list[Cell]]) -> None:
        self._board = cells

    @property
    def current_board(self) -> list[list[Cell]]:
        """TODO"""
        return self._board

    def transpose(self) -> list[list[Cell]]:
        """TODO"""
        return list(map(list, zip(*self._board)))

    def get_nth_row_digits(self, n: int) -> set[int]:
        """TODO"""
        return {c.digit for c in self.current_board[n] if c.digit != 0}

    def get_nth_col_digits(self, n: int) -> set[int]:
        """TODO"""
        return {c.digit for c in self.transpose()[n] if c.digit != 0}

    def get_box_digits(self, row: int, col: int) -> set[int]:
        """TODO"""
        start_row = row - row % 3
        start_col = col - col % 3

        return {
            self.current_board[i][j].digit
            for j in range(start_col, start_col + 3)
            for i in range(start_row, start_row + 3)
            if self.current_board[i][j].digit != 0
        }

    def __str__(self) -> str:
        """TODO"""

        if not self._board:
            raise ValueError('No board presented')

        board_str = '\nCurrent board:\n'
        for i in range(9):
            for j in range(9):
                board_str += str(self._board[i][j]) + ' '
                if (j + 1) % 3 == 0 and j != 8:
                    board_str += '| '

            board_str = board_str[:-1] + '\n'
            if (i + 1) % 3 == 0 and i != 8:
                board_str += '---------------------\n'

        return board_str


class BoardValidator:
    """TODO"""

    def _valid_rows_digits(self, board: Board) -> bool:
        """TODO"""
        for i in range(9):
            row_digits = [c.digit for c in board.current_board[i] if c.digit != 0]
            if len(row_digits) != len(set(row_digits)):
                print(f'Some digits are not unique in row {i+1}')
                return False
        return True

    def _valid_cols_digits(self, board: Board) -> bool:
        """TODO"""
        boardT = board.transpose()
        for i in range(9):
            col_digits = [c.digit for c in boardT[i] if c.digit != 0]
            if len(col_digits) != len(set(col_digits)):
                print(f'Some digits are not unique in column {i+1}')
                return False
        return True

    def _valid_squares_digits(self, board: Board) -> bool:
        """TODO"""
        boxes = [
            [
                board.current_board[3 * i + k][3 * j + l].digit
                for k in range(3)
                for l in range(3)
                if board.current_board[3 * i + k][3 * j + l].digit != 0
            ]
            for i in range(3)
            for j in range(3)
        ]

        for i, box in enumerate(boxes):
            if len(box) != len(set(box)):
                print(f'Some digits are not unique in box {i+1}')
                return False
        return True

    def valid_board(self, board: Board) -> bool:
        """Checks if given board is valid."""

        if not self._valid_rows_digits(board):
            return False

        if not self._valid_cols_digits(board):
            return False

        if not self._valid_squares_digits(board):
            return False

        return True
