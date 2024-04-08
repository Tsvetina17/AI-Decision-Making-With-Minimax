# Tic-Tac-Toe Game
# Instructions for the project are from CodeCademy and I wrote the code, while also applying my own ideas.

# The Tic-Tac-Toe board has three columns and three rows.
# For simplicity I will present the board as a 2D list.
# We start with an empty board that has numbers for each position.
my_board = [
  ['1', '2', '3'],
  ['4', '5', '6'],
  ['7', '8', '9']
  ]

# Print board with simple formatting.
def print_board(board):
    for i in range(len(board)):
        print(board[i])

# Entries in the board will be empty (' ') or with pieces from player one ('X') or player two ('O').
# Moves should be entered in the format 'board, column, piece.'
def execute_move(board, position, piece):
    for i in range(0, len(board), 1):
        for j in range(0, len(board[0]), 1):
            if board[i][j] == str(position):
                board[i][j] = piece
                print("Placed an '" + piece + "' in position " + str(position) + '.')
                return True
            else:
                j += 1
        i += 1

# Check all the possible combinations horizontally, vertically or diagonally if there is a winner.
# If there are no more moves available and there is no winner established yet, then there is a tie.

def has_won(board):
    winner = ' '

    # Return and print a list of the available moves remaining.
    def find_available_moves(board):
        l_moves_available = []
        for i in range(0, len(board), 1):
            for j in range(0, len(board[0]), 1):
                if board[i][j] != 'X' and board[i][j] != 'O':
                    l_moves_available.append(board[i][j])
                else:
                    continue
        print('Available moves are: ')
        print(l_moves_available)
        return l_moves_available

    moves_available = find_available_moves(board)

    # If there are no more moves available, then there is a tie.
    if moves_available == 0: 
        print("There are no more available moves. It's a tie.")
        winner = 'Tie'
        return board, winner

    # If there is no tie, check if any of the players has won.
    for i in range(len(board[0])):

        # Check horizontal spaces.
        if board[i][0] == 'X' and board[i][1] == 'X' and board[i][2] == 'X':
            print_board(board)
            print("Game over. Player 'X' has won.")
            winner = 'X'
            return board, winner
        if board[i][0] == 'O' and board[i][1] == 'O' and board[i][2] == 'O':
            print_board(board)
            print("Game over. Player 'O' has won.")
            winner = 'O'
            return board, winner
           
        # Check vertical spaces.
        if board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == 'X':
            print_board(board)
            print("Game over. Player 'X' has won.")
            winner = 'X'
            return board, winner
        if board[0][i] == 'O' and board[1][i] == 'O' and board[2][i] == 'O':
            print_board(board)
            print("Game over. Player 'O' has won.")
            winner = 'O'
            return board, winner

        # Check / diagonal spaces.
        if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
            print_board(board)
            print("Game over. Player 'X' has won.")
            winner = 'X'
            return board, winner
        if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
            print_board(board)
            print("Game over. Player 'O' has won.")
            winner = 'O'
            return board, winner

        # Check \ diagonal spaces.
        if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
            print_board(board)
            print("Game over. Player 'X' has won.")
            winner = 'X'
            return board, winner
        if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
            print_board(board)
            print("Game over. Player 'O' has won.")
            winner = 'O'
            return board, winner

execute_move(my_board, 9, 'X')
print_board(my_board)
has_won(my_board)