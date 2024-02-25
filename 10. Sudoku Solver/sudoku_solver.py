class SudokuSolver:
    def __init__(self, board):
        self.board = board

    def print_board(self):
        for row in self.board:
            print(' '.join(map(str, row)))

    def is_valid(self, row, col, num):
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False

        return True

    def find_empty_location(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def solve_sudoku(self):
        empty_location = self.find_empty_location()
        if not empty_location:
            return True

        row, col = empty_location

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num

                if self.solve_sudoku():
                    return True

                self.board[row][col] = 0

        return False
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solver = SudokuSolver(sudoku_board)

print("Input Sudoku:")
solver.print_board()

if solver.solve_sudoku():
    print("\nSolved Sudoku:")
    solver.print_board()
else:
    print("\nNo solution exists.")
