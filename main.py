from board_reader import BoardReader, InputReader, CSVReader, TestBoardReader
from board import Board, BoardValidator
from solver import BasicSolver


input_readers = {
    '1': InputReader(),
    '2': CSVReader(),
    '3': TestBoardReader(),
}


def read_board() -> BoardReader:
    """Choosing the board reader."""

    reader = None
    print('How would you like to input your sudoku board? Choose:')

    while not reader:
        for k, v in input_readers.items():
            print(f'{k}. from {v}')
        
        reader = input('your answer: ')
        if reader not in input_readers.keys():
            reader = None
            print('Invalid input, please enter number from list above.\n')
    
    return input_readers[reader]


def main():
    reader = read_board()
    board_input = reader.read()

    board = Board(board_input)
    print(board)

    validator = BoardValidator()
    if not validator.valid_board(board.current_board):
        print('Not a valid board')
        return
    
    solver = BasicSolver(board.current_board, validator)


if __name__ == '__main__':
    main()
