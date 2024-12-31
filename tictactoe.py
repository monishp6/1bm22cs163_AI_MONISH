import random
def print_board(board):
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("---|---|---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("---|---|---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")
    print()

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
   
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
   
    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    iteration = 0
    winner = None

    while winner is None:
       

        # Alternate between 'X' and 'O'
        if iteration % 2 == 0:
            print_board(board)
       
            try:
                row = int(input("Input row (1-3): ")) - 1
                column = int(input("Input column (1-3): ")) - 1
            except ValueError:
                print("Invalid input. Please enter numbers between 1 and 3.")
                continue
   
            if row not in range(3) or column not in range(3):
                print("The number of rows or columns is out of bounds. Please enter numbers between 1 and 3.")
                continue
   
            if board[row][column] != ' ':
                print("The position has already been entered! Please try another position.")
                continue
            board[row][column] = 'O'
        else:
            row = random.randrange(3)
            column = random.randrange(3)
            while(board[row][column] != ' '):
                row = random.randrange(3)
                column = random.randrange(3)
            board[row][column] = 'X'
       
        iteration += 1

        # Check for winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    print(" user:O \n bot:X")
    main()
