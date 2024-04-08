# Connect Four Game
# Instructions for the project are from CodeCademy and I wrote the code, while also applying my own ideas.


# The traditional Connect Four board has seven columns and six rows.
# For simplicity I will present the board as a 2D list.
# We start with an empty board.
# The board is represented sideways which will make adding pieces easier.
def build_board():
    board = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    return board

# Print board with simple formatting.
def print_board(board):
    # Add header
    header = ' '
    for num in range(1, len(board) + 1):
        header += ' '+ str(num) +'  '
    print(header)
    print('+---' * (len(board)) + '+')
   
    # Add rows
    for row in range(len(board[0])):
        print('|   ' * (len(board) +1))
        row_with_items = ''
        for col in range(len(board)):
            row_with_items += ('| '+str(board[col][row])) + ' '
        print(row_with_items + '|')
        print('|   ' * (len(board) +1))
        print('+---' * (len(board)) + '+')

# Entries in the board will be empty (' ') or with pieces from player one ('X') or player two ('O').
# Moves should be entered in the format 'board, column, piece.'
def execute_move(board, column, piece):
        
    # Check if the requested column is within the boarders of the board.
    while column < 1 or column > (len(board)):
        print('Error! ' + str(column) + " isn't valid input. The requested column is not within the boarders of the board. Please try again.")
        column = int(input('Please try again.'))
    
    # Check if the requested column is full.
    while board[column-1][0] != ' ':
        print('Error! The requested column is already full. Please try again.')
        column = int(input('Please try again.'))

    # If the requested column is within the boarders of the board and is not full, then execute the move.
    else:
        for y in range(len(board[0])-1, -1, -1):
            if board[column-1][y] == ' ':
                board[column-1][y] = piece
                print("Placed an '" + piece + "' in column " + str(column) + '.')
                print()
                return True
        return False
        my_board = build_board()

# Check if the game is over.
# Return True if either player has won or if there are no more available moves.
def game_over(board):    
    # Return True if there are any possible moves left, i.e. if all the columns are not already full.
    n_moves_available = 0
    for i in range(len(board)):
        if board[i][0] == ' ':
            n_moves_available += 1
        i += 1
        if i == range(len(board)):
            break

    if n_moves_available == 0:
        print_board(board)
        print('There are no more moves available. Game over.')
        return True

    # Return True if any of the players has won.
    else:
        # Check horizontal spaces.
        for y in range(len(board[0])):
            for x in range(len(board) - 3):
                if board[x][y] == 'X' and board[x+1][y] == 'X' and board[x+2][y] == 'X' and board[x+3][y] == 'X':
                    print_board(board)
                    print("Game over. Player 'X' has won.")
                    return True
                if board[x][y] == 'O' and board[x+1][y] == 'O' and board[x+2][y] == 'O' and board[x+3][y] == 'O':
                    print_board(board)
                    print("Game over. Player 'O' has won.")
                    return True
            
        # Check vertical spaces.
        for x in range(len(board)):
            for y in range(len(board[0]) - 3):
                if board[x][y] == 'X' and board[x][y+1] == 'X' and board[x][y+2] == 'X' and board[x][y+3] == 'X':
                    print_board(board)
                    print("Game over. Player 'X' has won.")
                    return True
                if board[x][y] == 'O' and board[x][y+1] == 'O' and board[x][y+2] == 'O' and board[x][y+3] == 'O':
                    print_board(board)
                    print("Game over. Player 'O' has won.")
                    return True
                    
        # Check / diagonal spaces.
        for x in range(len(board) - 3):
            for y in range(3, len(board[0])):
                if board[x][y] == 'X' and board[x+1][y-1] == 'X' and board[x+2][y-2] == 'X' and board[x+3][y-3] == 'X':
                    print_board(board)
                    print("Game over. Player 'X' has won.")
                    return True
                if board[x][y] == 'O' and board[x+1][y-1] == 'O' and board[x+2][y-2] == 'O' and board[x+3][y-3] == 'O':
                    print_board(board)
                    print("Game over. Player 'O' has won.")
                    return True

        # Check \ diagonal spaces.
        for x in range(len(board) - 3):
            for y in range(len(board[0]) - 3):
                if board[x][y] == 'X' and board[x+1][y+1] == 'X' and board[x+2][y+2] == 'X' and board[x+3][y+3] == 'X':
                    print_board(board)
                    print("Game over. Player 'X' has won.")
                    return True
                if board[x][y] == 'O' and board[x+1][y+1] == 'O' and board[x+2][y+2] == 'O' and board[x+3][y+3] == 'O':
                    print_board(board)
                    print("Game over. Player 'O' has won.")
                    return True
        
        return False

# Play the game. Start building the board and then execute all the moves.
def play_game():
    my_board = build_board()
    
    # Player 'X' goes first.
    next_turn = 'X'

    # Keep on playing until the game is over according to the rules created in game_over().
    while (not game_over(my_board)):
        print_board(my_board)
        move = 0
	    # Ask for a valid move.
        move = int(input("It is " + next_turn + "'s turn. Please select a column."))
        execute_move(my_board, move, next_turn)

	    # Check if the game is over. If so, exit the loop.
        if game_over(my_board):
           break
	    
        # If the game is not over, ask the next player to make a turn, i.e. switch the players.
        if next_turn == 'X':
	        next_turn = 'O'
        else:
	        next_turn = 'X'
    
play_game()