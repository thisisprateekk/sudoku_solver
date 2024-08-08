from pprint import pprint


def search_empty_rc(puzzle):
    # it searches the rows and columns which are unfilled. here we represent the empty cells by using "x"

    # we are using range of 0 to 8 to represent the row and cell number
    for r in range(0,9):
        for c in range(0,9):
            if puzzle[r][c] == "x":
                return r, c # shows the exact value of r,c where cell is empty

    return None, None # if there are no empty cells


def valid_sudoku(puzzle, guess, row, col ):
    # checks the validity of the puzzle using the sudoku rules that states that a number should repeat once in a row , column and 3x3 square
    # returns True or False

    # checking in the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False  # if the number is repeating then the guess is False

    # checking in the column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # checking in the 3x3 square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True


def solve_sudoku(puzzle):
    # solving sudoku using backtracking

    # choosing a row and column to make a guess
    row, col = search_empty_rc(puzzle)

    # if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:
        return True

    # if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):
    #check if this is a valid guess
        if valid_sudoku(puzzle, guess, row, col):
            #if this is a valid guess, then place it at that spot on the puzzle
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        puzzle[row][col] = "x"

    # if every guess is wrong then the puzzle is wrong and unsolvable
    return False


if __name__ == '__main__':
    example_puzzle = [
            [5, 3, 'x', 'x', 7, 'x', 'x', 'x', 'x'],
            [6, 'x', 'x', 1, 9, 5, 'x', 'x', 'x'],
            ['x', 9, 8, 'x', 'x', 'x', 'x', 6, 'x'],

            [8, 'x', 'x', 'x', 6, 'x', 'x', 'x', 3],
            [4, 'x', 'x', 8, 'x', 3, 'x', 'x', 1],
            [7, 'x', 'x', 'x', 2, 'x', 'x', 'x', 6],

            ['x', 6, 'x', 'x', 'x', 'x', 2, 8, 'x'],
            ['x', 'x', 'x', 4, 1, 9, 'x', 'x', 5],
            ['x', 'x', 'x', 'x', 8, 'x', 'x', 7, 9]
]
    print(solve_sudoku(example_puzzle))
    pprint(example_puzzle)