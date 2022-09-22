from abc import ABC
from .board import Board


class BoardSolver(ABC):
    def __init__(self, board: Board) -> None:
        self.board = board


class DefaultSolver(BoardSolver):
    pass
