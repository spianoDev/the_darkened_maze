from boards import *
from style import *

map_of_board = []

for row in board:
    map_row = []
    for item in row:
        if item != '\n':
            map_row.append('  ')
        else:
            map_row.append('\n')
    map_of_board.append(map_row)


# map_of_board[0][0] = 'P1'


def print_map(self):
    console.print('Map Legend', style='Bold red')
    console.print('" - " is a path, "||" is a wall')
    console.print(f'"^^" is a monster, "P1" is Player [green]{self.name}')
    maze_map = []
    printable_maze_map = ''
    for r in map_of_board:
        maze_map.append(r)
        printable_maze_map += ''.join(r)
    console.print(Panel(printable_maze_map[:-1], title='[bold dark_red]Maze Level 1',
                        style='bold black on light_yellow3', expand=False))


def make_map(self):
    map_of_board[self.position_one][self.position_two] = 'P1'
    print('MAP')


def set_path(self):
    map_of_board[self.position_one][self.position_two] = '- '
    print('PATH')


def make_wall(self):
    map_of_board[self.position_one][self.position_two] = '||'
    print('WALL')


def out_of_board(player):
    if player.position_one == len(board) and player.position_two == len(board) - 1:
        print('maze solved')

