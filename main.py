import os

def screen_clear():
  os.system('clear') # mac and linux
  os.system('cls') # windows

x_win_criteria = ['x','x','x'] # x_win_criteria = ['x']*3
o_win_criteria = ['o','o','o']

def set_up_players():
  player_1_choice = ''
  while player_1_choice.upper() != 'X' and player_1_choice.upper() != 'O':
    player_1_choice = input('Player 1: Do you want to be X or O? ')

  player_1 = player_1_choice.upper()
  if player_1 == 'X':
    player_2 = 'O'
  else:
    player_2 = 'X'

  return (player_1, player_2)

def ask_to_start_game(): 
  answer = ''
  while answer.upper() != 'Y' and answer.upper() != 'N':
    answer = input('Are you ready to play? (Y/N) ')

  if answer.upper() == 'Y':
    return True
  else:
    return False

def display_board(board):
  screen_clear()
  # print(f'[{board[6]}] [{board[7]}] [{board[8]}]\n\n[{board[3]}] [{board[4]}] [{board[5]}]\n\n[{board[0]}] [{board[1]}] [{board[2]}]')
  print(f'{board[6]} | {board[7]} | {board[8]}')
  print('--+---+--')
  print(f'{board[3]} | {board[4]} | {board[5]}')
  print('--+---+--')
  print(f'{board[0]} | {board[1]} | {board[2]}')

def get_position(turn_number, board, x_player, o_player):
  is_position_valid = False

  while is_position_valid == False:
    if turn_number % 2 != 0:
      position = input(f'{x_player} (X) - Choose an available position (1-9): ')
    else:
      position = input(f'{o_player} (O) - Choose an available position (1-9): ')
    is_position_valid = validate_position(position, board)
  return int(position)

def validate_position(position, board):
  if position.isdigit() == False:
    print('Input was not a digit')
    return False
  if int(position) not in range(1,10):
    print('Please enter a number from 1 to 9, inclusive')
    return False
  if board[int(position) - 1] == 'x' or board[int(position) - 1] == 'o':
    print(f'Position {position} already taken.')
    return False
  return True

def update_board(position, board, turn_number):
  if turn_number % 2 != 0:
    board[position - 1] = 'x'
  else: 
    board[position - 1] = 'o'
  display_board(board)

def check_for_win_or_tie(board, turn_number, x_player, o_player):
  if turn_number > 8:
    print("It's a tie!")
    return True
  if turn_number % 2 != 0:
    return is_winner(board, x_win_criteria, x_player)
  else:
    return is_winner(board, o_win_criteria, o_player)

def is_winner(board, win_criteria, player):
  top_row = [board[6], board[7], board[8]]
  middle_row = [board[3], board[4], board[5]]
  bottom_row = [board[0], board[1], board[2]]

  left_column = [board[6], board[3], board[0]]
  middle_column = [board[7], board[4], board[1]]
  right_column = [board[8], board[5], board[2]]

  top_left_to_bottom_right = [board[6], board[4], board[2]]
  top_right_to_bottom_left = [board[8], board[4], board[0]]

  all_checks = [top_row, middle_row, bottom_row, left_column, middle_column, right_column, top_left_to_bottom_right, top_right_to_bottom_left]

  for check in all_checks:
    if check == win_criteria:
      print(f'{player} wins!!!')
      return True
  return False

def replay_game():
  answer = ''
  while answer.upper() != 'Y' and answer.upper() != 'N':
    answer = input('Would you like to play again? (Y/N) ')

  if answer.upper() == 'Y':
    return True
  else:
    return False

def play_game():
  print('Welcome to Tic Tac Toe!')

  play = True
  while play == True:
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    # board = ['1','2','3','4','5','6','7','8','9']
    # board = ['x','x','3','o','5','6','7','8','9']

    (player_1_symbol, player_2_symbol) = set_up_players() 
    print(f'Player 1 will be {player_1_symbol} and Player 2 will be {player_2_symbol}')
    
    if player_1_symbol == 'X':
      x_player = 'Player 1'
      o_player = 'Player 2'
    else:
      x_player = 'Player 2'
      o_player = 'Player 1'

    is_game_start = ask_to_start_game()
    if not is_game_start:
      return

    game_over = False
    turn_number = 1
    while not game_over:
      display_board(board)
      position = get_position(turn_number, board, x_player, o_player)
      update_board(position, board, turn_number)

      game_over = check_for_win_or_tie(board, turn_number, x_player, o_player)
      if game_over == True:
        play = replay_game()
        break

      turn_number += 1

play_game()
