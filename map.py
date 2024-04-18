from boards import *

map_of_board = []

for row in board:
    print(*row[:-1])
    for item in row:
        if item != '\n':
            map_of_board.append('??')
        else:
            map_of_board.append('\n')

map_of_board[0] = ' - '
print(*map_of_board)

