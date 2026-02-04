import random

# Define the game board
board = [" " for _ in range(9)]

# Display board
def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("---------")

# Check win
def check_winner(player):
    win_combinations = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in win_combinations:
        if all(board[pos] == player for pos in combo):
            return True
    return False

# Check tie
def check_tie():
    return " " not in board

# Player move
def player_move():
    while True:
        move = int(input("Enter position (1-9): ")) - 1
        if board[move] == " ":
            board[move] = "X"
            break
        else:
            print("Position already taken!")

# Simple AI move (learns best free spots)
def ai_move():
    free_positions = [i for i in range(9) if board[i] == " "]
    
    # Try winning move
    for pos in free_positions:
        board[pos] = "O"
        if check_winner("O"):
            return
        board[pos] = " "

    # Block player
    for pos in free_positions:
        board[pos] = "X"
        if check_winner("X"):
            board[pos] = "O"
            return
        board[pos] = " "

    # Random move
    move = random.choice(free_positions)
    board[move] = "O"

# Main game loop
def main_game():
    print("Tic-Tac-Toe Game Started!")
    print_board()

    while True:
        player_move()
        print_board()

        if check_winner("X"):
            print("You win!")
            break

        if check_tie():
            print("It's a tie!")
            break

        ai_move()
        print("\nAI played:")
        print_board()

        if check_winner("O"):
            print("AI wins!")
            break

        if check_tie():
            print("It's a tie!")
            break

# Call the main game loop
main_game()
