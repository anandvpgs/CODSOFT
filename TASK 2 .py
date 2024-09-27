import random

def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def empty_cells(board):
    return [i for i, x in enumerate(board) if x == " "]

def winning(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in winning_combinations)

def game_over(board):
    return winning(board, 'X') or winning(board, 'O') or len(empty_cells(board)) == 0

def minimax(board, depth, is_maximizing):
    if winning(board, 'O'):
        return 1
    if winning(board, 'X'):
        return -1
    if len(empty_cells(board)) == 0:
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for move in empty_cells(board):
            board[move] = 'O'
            score = minimax(board, depth + 1, False)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in empty_cells(board):
            board[move] = 'X'
            score = minimax(board, depth + 1, True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = float('-inf')
    best_move = None
    for move in empty_cells(board):
        board[move] = 'O'
        score = minimax(board, 0, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def play_game():
    board = [" " for _ in range(9)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not game_over(board):
        # Human's turn
        while True:
            move = input("Enter your move (0-8): ")
            if move.isdigit() and int(move) in empty_cells(board):
                board[int(move)] = 'X'
                break
            else:
                print("Invalid move. Try again.")

        print_board(board)

        if game_over(board):
            break

        # AI's turn
        print("AI is thinking...")
        ai_move = get_best_move(board)
        board[ai_move] = 'O'
        print(f"AI chose position {ai_move}")
        print_board(board)

    if winning(board, 'X'):
        print("You win!")
    elif winning(board, 'O'):
        print("AI wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
