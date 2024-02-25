# Sudoku Solver 

This is a simple Python implementation of a Sudoku solver using a backtracking algorithm.

## How to Use

1. **Clone the Repository:**

    ```bash
    https://github.com/anushasundark/Python_Mini_Projects/blob/main/10.%20Sudoku%20Solver/sudoku_solver.py
    ```

2. **Run the Solver:**

    ```bash
    python sudoku_solver.py
    ```

3. **Input Sudoku Puzzle:**

    - The example Sudoku puzzle is provided in the `sudoku_board` list.
    - Modify the puzzle or input your own Sudoku puzzle by changing the values in the list.
    - `0` represents empty cells.

4. **Run the Solver:**

    - The SudokuSolver class is used to solve the puzzle.
    - The `solve_sudoku` method attempts to find a solution.
    - If a solution is found, the solved puzzle is printed.

5. **Example Usage:**

    ```python
    # Example Sudoku board
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        # ... (complete the rest of the Sudoku puzzle)
    ]

    solver = SudokuSolver(sudoku_board)

    print("Input Sudoku:")
    solver.print_board()

    if solver.solve_sudoku():
        print("\nSolved Sudoku:")
        solver.print_board()
    else:
        print("\nNo solution exists.")
    ```
