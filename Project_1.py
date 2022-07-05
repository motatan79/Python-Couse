# Print the board
from IPython.display import clear_output


def display_board(board):

    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

test_board = [' '] * 10
display_board(test_board)


# Tupple unpacking
mylist = [(1,2),(3,4),(5,6),(7,8)]

for a,b in mylist:
    print(a)
    print(b)