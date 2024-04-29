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

def print_map(self):
    console.print('Map Legend', style='Bold Green')
    console.print('" - " is a path, "||" is a wall')
    console.print(f'"^^" is a monster, "P1" is Player {self}')
    maze_map = []
    printable_maze_map = ''
    for r in map_of_board:
        maze_map.append(r)
        printable_maze_map += ''.join(r)
    console.print(Panel(printable_maze_map, title='Maze Level 1', style='bold black on light_yellow3', expand=False))
    # print('\n')
    # print(maze_map)
    # print(printable_maze_map)

# print_map('spiano')
