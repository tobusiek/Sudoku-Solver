from abc import ABC, abstractmethod
from board import Board, BoardValidator


class BoardSolver(ABC):
    """Abstract class for board solvers."""
    def __init__(self, board: Board, validator: BoardValidator) -> None:
        self._current_board = board
        self._solving_board = board
        self._validator = validator
    

    def _update_current_board(self) -> None:
        """Updating the current board with solved one."""
        self._current_board = self._solving_board

    
    @property
    def board(self) -> Board:
        """Returns current board."""
        return self._current_board

    
    @abstractmethod
    def _get_possible_digits(self) -> list[list[list[int]]]:
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
    

    def _input_single_candidates(self, possible: list[list[list[int]]]) -> None:
        """Checks if there are single candidates to input
        and updates the solving board."""
        for i, row in enumerate(possible):
            for j, col in possible[row]:
                if len(row[col]) == 1:
                    self._solving_board._current_board[i][j] = row[col][0]
    

    def _alone_in_possible_row(self) -> None:
        """Checks if there are single digits in possible row to input
        and updates the solving board."""
        pass


    def _alone_in_possible_col(self) -> None:
        """Checks if there are single digits in possible column to input
        and updates the solving board."""
        pass

    
    def _get_possible_digits(self) -> list[list[list[int]]]:
        pass


    def _eliminate_possible_digits(self) -> None:
        """Remove from possible digits that don't fit in the cell
         - there are better options."""


    def solve(self) -> None:
        possible = self._get_possible_digits()
        pass
