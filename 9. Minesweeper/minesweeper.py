import random

def initialize_board(rows, cols, mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]

    mine_positions = random.sample(range(rows * cols), mines)

    for mine_position in mine_positions:
        row = mine_position // cols
        col = mine_position % cols
        board[row][col] = '*'

    return board

def print_board(board, revealed):
    for i in range(len(board)):
        row_display = []
        for j in range(len(board[0])):
            if revealed[i][j]:
                row_display.append(board[i][j])
            else:
                row_display.append(' ')
        print(' '.join(row_display))

def count_adjacent_mines(board, row, col):
    mine_count = 0
    for i in range(max(0, row-1), min(row+2, len(board))):
        for j in range(max(0, col-1), min(col+2, len(board[0]))):
            if board[i][j] == '*':
                mine_count += 1
    return mine_count

def reveal_board(board, revealed, row, col):
    if revealed[row][col]:
        return
    revealed[row][col] = True

    if board[row][col] == ' ':
        for i in range(max(0, row-1), min(row+2, len(board))):
            for j in range(max(0, col-1), min(col+2, len(board[0]))):
                reveal_board(board, revealed, i, j)

def play_game(rows, cols, mines):
    board = initialize_board(rows, cols, mines)
    revealed = [[False for _ in range(cols)] for _ in range(rows)]
    while True:
        print_board(board, revealed)
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        if board[row][col] == '*':
            print("Game Over! You hit a mine.")
            break
        else:
            mine_count = count_adjacent_mines(board, row, col)
            revealed[row][col] = True
            if mine_count == 0:
                reveal_board(board, revealed, row, col)
            remaining_cells = sum(row.count(False) for row in revealed)
            if remaining_cells == mines:
                print("Congratulations! You won!")
                break

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    mines = int(input("Enter the number of mines: "))

    play_game(rows, cols, mines)
