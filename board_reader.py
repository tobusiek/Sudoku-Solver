from abc import ABC, abstractmethod
from string import digits


class BoardReader(ABC):
    """Abstract class for board reading."""

    def __init__(self) -> None:
        super().__init__()
        self._board = []
    

    def _valid_row_values(self, row: list[str]) -> bool:
        """Checking if values for cells are numbers between [0-9]."""
        for digit in row:
            if digit not in digits:
                return False
        return True


    @abstractmethod
    def _parse_row(self, row: str) -> list[int]:
        """Parsing the input from string to list of digits."""
        pass


    def _set_row(self, row_idx: int, row: list[int]) -> None:
        """Setting board's row of given index."""
        self._board.insert(row_idx, row)


    @abstractmethod
    def read(self) -> None:
        """Reading the board from input."""
        pass


class InputReader(BoardReader):
    """Class for board reading from console input, row by row."""

    def __init__(self) -> None:
        super().__init__()


    def _parse_row(self, row: str) -> list[int]:
        row = row.strip()
        row = row.split(' ')

        if len(row) != 9:
            print('Please insert 9 values divided by spaces\n')
            return []

        if not self._valid_row_values(row):
            print('Input values must be digits in range [0-9]\n')
            return []
        
        return [int(digit) for digit in row]


    def read(self) -> None:
        msg = '\nEnter rows of given digits. If cell doesn\'t have a digit yet, enter 0.'
        msg += ' Separate each digit with space.\nEnter rows:'
        print(msg)
        
        for i in range(9):
            row = []
            while not row:
                msg = f'{i+1}: '
                row = input(msg)
                row = self._parse_row(row)
                
            self._set_row(i, row)

        return self._board
    

    def __str__(self) -> str:
        return 'console input'


class CSVReader(BoardReader):
    """Class for board reading from csv file."""

    def __init__(self) -> None:
        super().__init__()
        self.value_separator = ';'

    
    def change_separator(self, separator):
        self.value_separator = separator

    
    def _parse_row(self, row: str) -> list[int]:
        pass

    
    def read(self) -> None:
        pass


    def __str__(self) -> str:
        return 'CSV file'
