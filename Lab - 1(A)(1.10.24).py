#Implement tic-tac-toe game

import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def p_board(player):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def check_win():

  for i in range(0, 7, 3):
    if board[i] == board[i + 1] == board[i + 2] and board[i] != '-':
      return board[i]

  for i in range(3):
    if board[i] == board[i + 3] == board[i + 6] and board[i] != '-':
      return board[i]

  if board[0] == board[4] == board[8] and board[0] != '-':
    return board[0]
  if board[2] == board[4] == board[6] and board[2] != '-':
    return board[2]

  return None

def check_tie():
  if '-' not in board:
    return True
  return False


def play_game():
  current_player = "X"  
  game_over = False

  while not game_over:
    p_board(current_player)

    if current_player == "X":  
      print("It's your turn (X).")
      try:
        position = int(input("Choose a position from 1-9: ")) - 1
        if position < 0 or position > 8 or board[position] != '-':
          print("Invalid move. Try again.")
          continue
      except ValueError:
        print("Invalid input. Please enter a number between 1 and 9.")
        continue
    else:  
      print("Computer's turn (O).")
      available_moves = [i for i, spot in enumerate(board) if spot == '-']
      position = random.choice(available_moves)

    board[position] = current_player
    winner = check_win()

    if winner:
      p_board(current_player)
      print(winner + " won!")
      game_over = True
    elif check_tie():
      p_board(current_player)
      print("It's a tie!")
      game_over = True
    else:
      current_player = "O" if current_player == "X" else "X"

play_game()
