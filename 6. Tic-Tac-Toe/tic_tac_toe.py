def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def play_tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter the row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter the column (0, 1, or 2): "))
        if board[row][col] != ' ':
            print("Invalid move. Cell already occupied. Try again.")
            continue
        board[row][col] = current_player
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins! Congratulations!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a tie! The board is full.")
            break
        current_player = 'O' if current_player == 'X' else 'X'
play_tic_tac_toe()
