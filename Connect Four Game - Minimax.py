# Connect Four Game with Minimax.
# Instructions and help for the project are from CodeCademy.

# Import deepcopy and random modules.
from copy import deepcopy
import random
random.seed(108)

# Print board in a simple format.
def print_board(board):
    print()
    print(' ', end='')
    for x in range(1, len(board) + 1):
        print(' %s  ' % x, end='')
    print()
    print('+---+' + ('---+' * (len(board) - 1)))
    for y in range(len(board[0])):
        print('|   |' + ('   |' * (len(board) - 1)))
        print('|', end='')
        for x in range(len(board)):
            print(' %s |' % board[x][y], end='')
        print()
        print('|   |' + ('   |' * (len(board) - 1)))
        print('+---+' + ('---+' * (len(board) - 1)))

# Take a turn. The function takes three parameters: board, space (number between 1 and 9), symbol ('X' or 'O').
def select_space(board, column, player):
    if not move_is_valid(board, column):
        return False
    if player != 'X' and player != 'O':
        return False
    for y in range(len(board[0])-1, -1, -1):
        if board[column-1][y] == ' ':
            board[column-1][y] = player
            return True
    return False

# Determine if the board is full.
def board_is_full(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == ' ':
                return False
    return True

# Determine if the move is valid.
def move_is_valid(board, move):
    if move < 1 or move > (len(board)):
        return False
    if board[move-1][0] != ' ':
        return False
    return True

# Return a list with the available moves.
def available_moves(board):
    moves = []
    for i in range(1, len(board)+1):
        if move_is_valid(board, i):
            moves.append(i)
    return moves

# Determine if there is a winner.
def has_won(board, symbol):
    # Check horizontal spaces.
    for y in range(len(board[0])):
        for x in range(len(board) - 3):
            if board[x][y] == symbol and board[x+1][y] == symbol and board[x+2][y] == symbol and board[x+3][y] == symbol:
                return True
    
    # Check vertical spaces.
    for x in range(len(board)):
        for y in range(len(board[0]) - 3):
            if board[x][y] == symbol and board[x][y+1] == symbol and board[x][y+2] == symbol and board[x][y+3] == symbol:
                return True
    
    # Check / diagonal spaces.
    for x in range(len(board) - 3):
        for y in range(3, len(board[0])):
            if board[x][y] == symbol and board[x+1][y-1] == symbol and board[x+2][y-2] == symbol and board[x+3][y-3] == symbol:
                return True
            
    # Check \ diagonal spaces.
    for x in range(len(board) - 3):
        for y in range(len(board[0]) - 3):
            if board[x][y] == symbol and board[x+1][y+1] == symbol and board[x+2][y+2] == symbol and board[x+3][y+3] == symbol:
                return True
    return False

# Return winner if game is over.
def game_is_over(board):
  return has_won(board, 'X') or has_won(board, 'O') or len(available_moves(board)) == 0

def codecademy_evaluate_board(board):
    if has_won(board, 'X'):
      return float('Inf')
    elif has_won(board, 'O'):
      return -float('Inf')
    else:
      x_streaks = count_streaks(board, 'X')
      o_streaks = count_streaks(board, 'O')
      return x_streaks - o_streaks

def count_streaks(board, symbol):
    count = 0
    for col in range(len(board)):
        for row in range(len(board[0])):
            if board[col][row] != symbol:
                continue
            # right
            if col < len(board) - 3:
                num_in_streak = 0
                for i in range(4):
                    if board[col + i][row] == symbol:
                        num_in_streak += 1
                    elif board[col + i][row] != ' ':
                        num_in_streak = 0
                        break
                count += num_in_streak
            #left
            if col > 2:
                num_in_streak = 0
                for i in range(4):
                    if board[col - i][row] == symbol:
                        num_in_streak += 1
                    elif board[col - i][row] != ' ':
                        num_in_streak = 0
                        break
                count += num_in_streak
            #up-right
            if col < len(board) - 3 and row > 2:
                num_in_streak = 0
                for i in range(4):
                    if board[col + i][row - i] == symbol:
                       num_in_streak += 1
                    elif board[col + i][row - i] != ' ':
                        num_in_streak = 0
                        break
                count += num_in_streak
            #down-right
            if col < len(board) - 3 and row < len(board[0]) - 3:
                num_in_streak = 0
                for i in range(4):
                    if board[col + i][row + i] == symbol:
                        num_in_streak += 1
                    elif board[col + i][row + i] != ' ':
                        num_in_streak = 0
                        break
                count += num_in_streak
            #down-left
            if col > 2 and row < len(board[0]) - 3:
                num_in_streak = 0
                for i in range(4):
                    if board[col - i][row + i] == symbol:
                        num_in_streak += 1
                    elif board[col - i][row + i] != ' ':
                        num_in_streak = 0
                        break
                count += num_in_streak
            #up-left
            if col > 2 and row > 2:
                num_in_streak = 0
                for i in range(4):
                    if board[col - i][row - i] == symbol:
                        num_in_streak += 1
                    elif board[col - i][row - i] != ' ':
                        num_in_streak = 0
                        break
                count += num_in_streak
            #down-left
            if col > 2 and row < len(board[0]) - 3:
                num_in_streak = 0
                for i in range(4):
                    if board[col - i][row + i] == symbol:
                        num_in_streak += 1
                    elif board[col - i][row + i] != ' ':
                        num_in_streak = 0
                        break
                count += num_in_streak
            #down
            num_in_streak = 0
            if row < len(board[0]) - 3:
                for i in range(4):
                    if row + i < len(board[0]):
                        if board[col][row + i] == symbol:
                            num_in_streak += 1
                        else:
                            break
            for i in range(4):
                if row - i > 0:
                    if board[col][row - i] == symbol:
                        num_in_streak += 1
                    elif board[col][row - i] == ' ':
                        break
                    else:
                        num_in_streak == 0
            if row < 3:
                if num_in_streak + row < 4:
                    num_in_streak = 0
            count += num_in_streak
    return count

''' Define minimax function
We add the parameter eval_function. It will allow us to choose the evaluation function we want to run, i.e. swap the strategy of our AI.
This alllows different players to use different evaluation functions.
The core idea behind alpha-beta pruning is to ignore parts of the tree that we know will be dead ends.
Alpha-beta pruning is accomplished by keeping track of two variables for each node — alpha and beta. 
alpha keeps track of the minimum score the maximizing player can possibly get. It starts at negative infinity and gets updated as that minimum score increases.
On the other hand, beta represents the maximum score the minimizing player can possibly get. It starts at positive infinity and will decrease as that maximum possible score decreases.
For any node, if alpha is greater than or equal to beta, that means that we can stop looking through that node’s children.
To implement this in our code, we’ll have to include two new parameters in our function — alpha and beta. When we first call minimax() we’ll set alpha to negative infinity and beta to positive infinity.
We also want to make sure we pass alpha and beta into our recursive calls. We’re passing these two values down the tree.
Next, we want to check to see if we should reset alpha and beta. In the maximizing case, we want to reset alpha if the newly found best_value is greater than alpha. In the minimizing case, we want to reset beta if best_value is less than beta.
Finally, after resetting alpha and beta, we want to check to see if we can prune. If alpha is greater than or equal to beta, we can break and stop looking through the other potential moves.
'''

def minimax(input_board, is_maximizing, depth, alpha, beta, eval_function):
  if game_is_over(input_board) or depth == 0:
        return [eval_function(input_board), '']
  if is_maximizing:
    best_value = -float('Inf')
    moves = available_moves(input_board)
    random.shuffle(moves)
    best_move = moves[0]
    for move in moves:
      new_board = deepcopy(input_board)
      select_space(new_board, move, 'X')
      hypothetical_value = minimax(new_board, False, depth - 1, alpha, beta, eval_function)[0]
      if hypothetical_value > best_value:
        best_value = hypothetical_value
        best_move = move
      alpha = max(alpha, best_value)
      if alpha >= beta:
        break
    return [best_value, best_move]
  else:
    best_value = float('Inf')
    moves = available_moves(input_board)
    random.shuffle(moves)
    best_move = moves[0]
    for move in moves:
      new_board = deepcopy(input_board)
      select_space(new_board, move, 'O')
      hypothetical_value = minimax(new_board, True, depth - 1, alpha, beta, eval_function)[0]
      if hypothetical_value < best_value:
        best_value = hypothetical_value
        best_move = move
      beta = min(beta, best_value)
      if alpha >= beta:
        break
    return [best_value, best_move]
  
def make_board():
    new_game = []
    for x in range(7):
        new_game.append([' '] * 6)
    return new_game
	
def random_eval(board):
  return random.randint(-100, 100)

# We write an evaluation function that works on non-leaf game states, so we can stop the recursion early
def my_evaluate_board(board):
  if has_won(board, 'X'):
    return float('Inf')
  elif has_won(board, 'O'):
    return -float('Inf')
 
  x_two_streak = 0
  o_two_streak = 0
  
  for col in range(len(board)-1):
    for row in range(len(board[0])):
      if board[col][row] == 'X' and board [col + 1][row] == 'X':
        x_two_streak += 1
      elif board[col][row] == 'O' and board[col + 1][row] == 'O':
        o_two_streak += 1
    
    return x_two_streak - o_two_streak
  
def two_ai_game():
    my_board = make_board()
    while not game_is_over(my_board):
      #The 'X' player finds their best move.
      result = minimax(my_board, True, 4, -float('Inf'), float('Inf'), random_eval)
      print( 'X Turn\nX selected ', result[1])
      print(result[1])
      select_space(my_board, result[1], 'X')
      print_board(my_board)
      if not game_is_over(my_board):
        #The 'O' player finds their best move
        result = minimax(my_board, False, 2, -float('Inf'), float('Inf'), codecademy_evaluate_board)
        print( 'O Turn\nO selected ', result[1])
        print(result[1])
        select_space(my_board, result[1], 'O')
        print_board(my_board)
    if has_won(my_board, 'X'):
        print('X won!')
    elif has_won(my_board, 'O'):
        print('O won!')
    else:
        print("It's a tie!")

two_ai_game()
new_board = make_board()
select_space(new_board, 5, 'X')
select_space(new_board, 6, 'O')
print_board(new_board)
print(my_evaluate_board(new_board))