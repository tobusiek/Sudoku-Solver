from abc import ABC, abstractmethod
from board import Board, BoardValidator


class BoardSolver(ABC):
    """Abstract class for board solvers."""
    def __init__(self, board: Board, validator: BoardValidator) -> None:
        self._cur_board = board
        self._solving = Board(board.current_board)
        self._validator = validator
    

    def _update_current_board(self) -> None:
        """Updating the current board with solved one."""
        self._cur_board._cur_board = self._solving._cur_board
    

    def _revert_solving_board(self) -> None:
        """Updating the solving board with current one."""
        self._solving._cur_board = self._cur_board._cur_board

    
    @property
    def board(self) -> Board:
        """Returns current board."""
        return self._cur_board

    
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
    

    def _search_single_candidates(self, possible: list[list[list[int]]]) -> bool:
        """Checks if there are single candidates to input and updates
         the solving board. If at least one digit was inserted to a cell,
         it returns True, as the board was updated and new single
         candidates can be found."""
        inserted: bool = False

        for i in range(len(possible)):
            for j in range(len(possible[i])):
                if len(possible[i][j]) == 1:
                    self._solving._cur_board[i][j] = possible[i][j][0]

                    if not self._validator.valid_board(self._solving._cur_board):
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

    
    def _get_possible_digits(self) -> list[list[list[int]]]:

        pass


    def _eliminate_possible_digits(self,
            possible: list[list[list[int]]]
        ) -> list[list[list[int]]]:
        """Remove from possible digits that don't fit in the cell
         - there are better options."""
        



    def solve(self) -> None:
        possible = self._get_possible_digits()
        pass
