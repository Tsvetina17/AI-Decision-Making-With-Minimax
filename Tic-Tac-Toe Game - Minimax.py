# Tic-Tac-Toe Game with Minimax
# Instructions for the project are from CodeCademy and I wrote the code, while also applying my own ideas.

# Import deepcopy.
from copy import deepcopy

# Print board in a simple format.
def print_board(board):
    print('|-------------|')
    print('| Tic Tac Toe |')
    print('|-------------|')
    print('|             |')
    print('|    ' + board[0][0] + ' ' + board[0][1] + ' ' + board[0][2] + '    |')
    print('|    ' + board[1][0] + ' ' + board[1][1] + ' ' + board[1][2] + '    |')
    print('|    ' + board[2][0] + ' ' + board[2][1] + ' ' + board[2][2] + '    |')
    print('|             |')
    print('|-------------|')
    print()

# Take a turn. The function takes three parameters: board, space (number between 1 and 9), symbol ('X' or 'O').
def select_space(board, move, turn):
    if move not in range(1,10):
        return False
    row = int((move-1)/3)
    col = (move-1)%3
    if board[row][col] != 'X' and board[row][col] != 'O':
        board[row][col] = turn
        return True
    else:
        return False
    
# Return a list of available moves.
def available_moves(board):
    moves = []
    for row in board:
        for col in row:
            if col != 'X' and col != 'O':
                moves.append(int(col))
    return moves

# Return a winner if there is any.
def has_won(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
       return True
    return False
  
# Return winner if game is over.  
def game_is_over(board):
  return has_won(board, 'X') or has_won(board, 'O') or len(available_moves(board)) == 0

# The function returns the “value” of the best possible move.
# 1: a move exists that guarantees that 'X' will win.
# -1: there’s nothing that 'X' can do to prevent 'O' from winning.
# 0: the best 'X' can do is force a tie (assuming 'O' doesn’t make a mistake).
def evaluate_board(board):
  if has_won(board, 'X'):
    return 1
  elif has_won(board, 'O'):
    return -1
  else:
    return 0

# The minimax algorithm is a decision-making algorithm that is used for finding the best move in a two player game. 
# It’s a recursive algorithm — it calls itself. 
# In order for us to determine if making move A is a good idea, we need to think about what our opponent would do if we made that move.
# We make a tree of the hypothetical game states. We’ll eventually reach a point where the game is over — we’ll reach a leaf of the tree. Either we won, our opponent won, or it was a tie. 

# The function has two parameters: 
# 1. The game state that we’re interested in finding the best move.
# 2. A boolean is_maximizing represents whose turn it is. If True, then we know we’re working with the maximizing player. This means when we’re picking the “best” move from the list of moves, the move with the highest value. 
# If False, then we’re the minimizing player and want to pick the minimum value.
def minimax(input_board, is_maximizing):
  # Base case - the game is over, so we return the value of the board
  if game_is_over(input_board):
    return [evaluate_board(input_board), '']
  # The maximizing player
  if is_maximizing:
    # The best value starts at the lowest possible value
    best_value = -float('Inf')
    best_move = ''
    # Loop through all the available moves
    for move in available_moves(input_board):
      # Make a copy of the board and apply the move to it
      new_board = deepcopy(input_board)
      select_space(new_board, move, 'X')
      # Recursively find your opponent's best move
      hypothetical_value = minimax(new_board, False)[0]
      # Update best value if you found a better hypothetical value
      if hypothetical_value > best_value:
        best_value = hypothetical_value
        best_move = move
    return [best_value, best_move]
  # The minimizing player
  else:
    # The best value starts at the highest possible value
    best_value = float('Inf')
    best_move = ''
    # Testing all potential moves
    for move in available_moves(input_board):
      # Copying the board and making the move
      new_board = deepcopy(input_board)
      select_space(new_board, move, 'O')
      # Passing the new board back to the maximizing player
      hypothetical_value = minimax(new_board, True)[0]
      # Keeping track of the best value seen so far
      if hypothetical_value < best_value:
        best_value = hypothetical_value
        best_move = move
    return [best_value, best_move]


my_board = [
  ['1', '2', '3'],
  ['4', '5', '6'],
  ['7', '8', '9']
]
while not game_is_over(my_board):
  select_space(my_board, minimax(my_board, True)[1], 'X')
  print_board(my_board)
  if not game_is_over(my_board):
    select_space(my_board, minimax(my_board, False)[1], 'O')
    print_board(my_board)