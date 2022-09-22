from abc import ABC, abstractmethod
from os import curdir
from string import digits
from csv_opener import CSVSelector


class BoardReader(ABC):
    """Abstract class for board reading."""

    def __init__(self) -> None:
        super().__init__()
        self._board = []

    
    def _valid_row_length(self, row: list[int]) -> bool:
        """Checking if row length is equal to 9."""
        return len(row) == 9
    

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
    def read(self) -> list[list[int]]:
        """Reading the board from input."""
        pass


class InputReader(BoardReader):
    """Class for board reading from console input, row by row."""

    def __init__(self) -> None:
        super().__init__()


    def _parse_row(self, row: str) -> list[int]:
        row = row.strip()
        row = row.split(' ')

        if not self._valid_row_length(row):
            print('Please insert 9 values divided by spaces\n')
            return []

        if not self._valid_row_values(row):
            print('Input values must be digits in range [0-9]\n')
            return []
        
        return [int(digit) for digit in row]


    def read(self) -> list[list[int]]:
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
        self._filename = None

    
    def _parse_row(self, row: str) -> list[int]:
        row = row.strip()
        separator = row[1]
        row = row.split(separator)

        if not self._valid_row_length(row):
            msg = 'Please reformat the file to 9 values (0 for no given digit'
            msg = ' in a cell) divided by chosen separator\n'
            print(msg)
            raise ValueError('Reformat the file and run program again')

        if not self._valid_row_values(row):
            print('Input values must be digits in range [0-9]\n')
            raise ValueError('Reformat the file and run program again')
        
        return [int(digit) for digit in row]

    
    def read(self) -> list[list[int]]:
        self._filename = CSVSelector().get_filename()

        if self._filename and self._filename != curdir:
            with open(self._filename) as csv_file:
                for i, row in enumerate(csv_file):
                    row = self._parse_row(row)
                    self._set_row(i, row)
        
        return self._board


    def __str__(self) -> str:
        return 'CSV file'
