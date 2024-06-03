import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check for a winner
def check_winner(board):
    # Check rows, columns and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    return None

# Function to check if the board is full
def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == 'X':
        return -1
    elif winner == 'O':
        return 1
    elif is_full(board):
        return 0
    
    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for the AI
def best_move(board):
    best_val = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = ' '
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

# Main game loop
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    human_turn = True
    
    while True:
        print_board(board)
        if check_winner(board) or is_full(board):
            break
        
        if human_turn:
            row = int(input("Enter the row (0, 1, 2): "))
            col = int(input("Enter the column (0, 1, 2): "))
            if board[row][col] == ' ':
                board[row][col] = 'X'
                human_turn = False
            else:
                print("Invalid move. Try again.")
        else:
            move = best_move(board)
            if move:
                board[move[0]][move[1]] = 'O'
                human_turn = True
    
    winner = check_winner(board)
    if winner:
        print(f"The winner is {winner}!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()