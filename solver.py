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
        """Calls get_possile_digits method and inputs correct digits in cells
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
        inserted: bool = False

        for i in range(len(self._solving._board)):
            for j, cell in enumerate(self._solving._board[i]):
                if len(cell.possible) == 1:
                    self._solving._board[i][j] = cell.possible[0]

                    if not self._validator.valid_board(self._solving._board):
                        self._revert_solving_board()
                        continue

                    self._update_current_board()
                    inserted = True

        return inserted

    def _alone_in_possible_row(self) -> None:
        """Checks if there are single digits in possible row to input
        and updates the solving board."""
        pass

    def _alone_in_possible_col(self) -> None:
        """Checks if there are single digits in possible column to input
        and updates the solving board."""
        pass

    def _calculate_possible_digits(self) -> None:
        """Calculates possible digits for each empty cell."""
        for i in range(len(self._solving._board)):
            for j, cell in self._solving._board[i]:
                if cell.digit:
                    continue

                row_digits = self._solving.get_nth_row_digits(i)
                col_digits = self._solving.get_nth_col_digits(j)
                box_digits = self._solving.get_box_digits(i, j)
                possible = set(list(digits)[1:]) - row_digits - col_digits - box_digits

                self._solving._board[i][j].set_possible_digits(possible)
                self._update_current_board()

    def _eliminate_possible_digits(self) -> None:
        """Remove from possible digits that don't fit in the cell
         - there are better options."""

    def solve(self) -> None:
        self._calculate_possible_digits()
        pass
