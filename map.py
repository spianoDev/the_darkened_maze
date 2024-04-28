from boards import *
from style import *

map_of_board = []

for row in board:
    # print(*row[:-1])
    map_row = []
    for item in row:
        if item != '\n':
            map_row.append('  ')
        else:
            map_row.append('\n')
    map_of_board.append(map_row)

map_of_board[0][0] = 'P1'
# print(*map_of_board)

def print_map():
    console.print('Below is a map of the maze.', style='Bold Green')
    console.print('" - " is a path, "||" is a wall, and "^^" is a monster\n')
    for r in map_of_board:
        console.print(*r[:-1], style='black on yellow')
        print('\n')

