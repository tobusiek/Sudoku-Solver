from abc import ABC, abstractmethod
from copy import copy
from string import digits
from board import Cell, Board, BoardValidator


class BoardSolver(ABC):
    """Abstract class for board solvers."""

    def __init__(self, board: Board, validator: BoardValidator) -> None:
        self._cur_board = board
        self._solving = copy(board)
        self._validator = validator

    def _update_current_board(self) -> None:
        """Updating the current board with solved one."""
        self._cur_board._board = copy(self._solving._board)

    def _revert_solving_board(self) -> None:
        """Updating the solving board with current one."""
        self._solving._board = copy(self._cur_board._board)

    def _solved(self) -> bool:
        """Checks if board is solved - no zeros in cells."""
        for i in range(len(self._solving.current_board)):
            if not all(c.digit != 0 for c in self._solving.current_board[i]):
                return False
        return True

    @property
    def board(self) -> Board:
        """Returns current board."""
        return self._cur_board

    @abstractmethod
    def _calculate_possible_digits(self) -> list[list[Cell]]:
        """Calculating and returning possible digits for each empty cell."""
        pass

    @abstractmethod
    def solve(self) -> None:
        """Calls calculate_possile_digits method and inputs correct digits in cells
        if board is valid, until the board is solved. After that, it updates
        the current board with solved one."""
        pass


class BasicSolver(BoardSolver):
    """Basic solver method for sudoku board."""

    def __init__(self, board: Board, validator: BoardValidator) -> None:
        super().__init__(board, validator)

    def _search_single_candidates(self) -> bool:
        """Checks if there are single candidates to input and updates
         the solving board. If at least one digit was inserted to a cell,
         it returns True, as the board was updated and new single
         candidates can be found."""
        inserted = False

        for row in range(len(self._solving.current_board)):
            for cell in self._solving.current_board[row]:
                if cell.digit:
                    continue

                if len(cell.possible) == 1:
                    cell.digit = cell.possible.pop()

                    if not self._validator.valid_board(self._solving):
                        self._revert_solving_board()
                        continue

                    self._update_current_board()
                    inserted = True

        return inserted

    def _alone_candidates_in_rows(self) -> bool:
        """Checks if there are single candidates in row to input
        and updates the solving board."""
        inserted = False

        for row in range(len(self._solving.current_board)):
            possible_digits_occurances = dict(
                zip([n + 1 for n in range(9)], [0 for _ in range(9)])
            )

            for cell in self._solving.current_board[row]:
                if cell.digit:
                    continue

                for possible_digit in cell.possible:
                    possible_digits_occurances[possible_digit] += 1

            one_occurance = [k for k, v in possible_digits_occurances.items() if v == 1]
            for cell in self._solving.current_board[row]:
                if cell.digit:
                    continue

                for possible_digit in cell.possible:
                    if possible_digit in one_occurance:
                        cell.digit = possible_digit

                        if not self._validator.valid_board(self._solving):
                            self._revert_solving_board()
                            continue

                        self._update_current_board()
                        inserted = True

        return inserted

    def _alone_candidates_in_cols(self) -> bool:
        """Checks if there are single candidates in column to input
        and updates the solving board."""
        inserted = False

        boardT = self._solving.transpose()
        for row in range(len(boardT)):
            possible_digits_occurances = dict(
                zip([n + 1 for n in range(9)], [0 for _ in range(9)])
            )

            for cell in boardT[row]:
                if cell.digit:
                    continue

                for possible_digit in cell.possible:
                    possible_digits_occurances[possible_digit] += 1

            one_occurance = [k for k, v in possible_digits_occurances.items() if v == 1]
            for cell in boardT[row]:
                if cell.digit:
                    continue

                for possible_digit in cell.possible:
                    if possible_digit in one_occurance:
                        cell.digit = possible_digit

                        if not self._validator.valid_board(self._solving):
                            self._revert_solving_board()
                            continue

                        self._update_current_board()
                        inserted = True

        return inserted

    def _calculate_possible_digits(self) -> None:
        """Calculates possible digits for each empty cell."""
        for i in range(len(self._solving.current_board)):
            for j, cell in enumerate(self._solving.current_board[i]):
                if cell.digit:
                    continue

                row_digits = self._solving.get_nth_row_digits(i)
                col_digits = self._solving.get_nth_col_digits(j)
                box_digits = self._solving.get_box_digits(i, j)
                possible = (
                    {int(d) for d in list(digits[1:])}
                    - row_digits
                    - col_digits
                    - box_digits
                )
                cell.set_possible_digits(possible)
                self._update_current_board()

    def _eliminate_possible_digits(self) -> None:
        """Remove from possible digits that don't fit in the cell
         - there are better options."""
        # TODO
        pass

    def solve(self) -> None:
        while not self._solved():
            self._calculate_possible_digits()
            # self._eliminate_possible_digits()

            if self._search_single_candidates():
                continue

            if self._alone_candidates_in_rows():
                continue

            if self._alone_candidates_in_cols():
                continue
