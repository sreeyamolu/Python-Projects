print("===== WELCOME TIC TAC TOE GAME =====")
print()
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 ")


# Create an empty game board
board = [" "] * 9

# Function to display the board

# Tic Tac Toe Game
# Two-player console-based game

def display_board(board):
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


def take_move(board, player):
    while True:
        try:
            choice = input(
                f"Player {player}, enter a position (1-9): "
            ).strip()

            if choice == "":
                print("Input cannot be empty. Try again.")
                continue

            position = int(choice)

            if position < 1 or position > 9:
                print("Choose a number from 1 to 9.")
            elif board[position - 1] != " ":
                print("Cell already occupied. Try again.")
            else:
                board[position - 1] = player
                break

        except ValueError:
            print("Please enter a valid number.")


def check_winner(board, player):
    winning_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for position in winning_positions:
        if all(board[i] == player for i in position):
            return True

    return False


def check_draw(board):
    return " " not in board


def play_again():
    while True:
        answer = input(
            "Do you want to play again? (yes/no): "
        ).strip().lower()

        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print("Please enter yes or no.")


def play_game():
    board = [" "] * 9
    current_player = "X"

    print("\n===== TIC TAC TOE GAME =====")
    print("Choose a cell using numbers 1 to 9.")
    print("Player 1: X | Player 2: O")

    display_board(board)

    while True:
        print(f"Player {current_player}'s turn")
        take_move(board, current_player)
        display_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print("The game is a draw!")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


while True:
    play_game()

    if not play_again():
        print("Thank you for playing Tic Tac Toe!")
        break