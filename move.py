from boards import *
from map import *
from random import randint
from find_treasure import *
from combat import *
from players import *
from style import *


## Basic move functions without hard coded values ##
def move_up(self):
    if self.position_one > 0:
        self.position_one -= 1
        return
    else:
        found_boundary(self, 'up')
        return


def move_down(self):
    if self.position_one < len(board):
        self.position_one += 1
        return
    else:
        found_boundary(self, 'down')
        return


def move_right(self):
    if self.position_two < len(board):
        self.position_two += 1
        return
    else:
        found_boundary(self, 'right')
        return


def move_left(self):
    if self.position_two > 0:
        self.position_two -= 1
        return
    else:
        found_boundary(self, 'left')
        return


## actions when encountering a wall or the boundary of the board ##
def found_wall(self, direction):
    if direction.lower() == 'up' or direction.lower() == 'u':
        move_down(self)
        print('move back down')
    elif direction.lower() == 'down' or direction.lower() == 'd':
        move_up(self)
        print('move back up')
    elif direction.lower() == 'right' or direction.lower() == 'r':
        move_left(self)
    elif direction.lower() == 'left' or direction.lower() == 'l':
        move_right(self)
    typing(f'{self.name} returns to the previous position.\n')
    return


def boundary():
    off_board_types = ['a thicket of thorny brambles', 'a 2000 foot drop', 'the side of a mountain',
                       'swirling water rapids', 'a black abyss', 'molten lava']
    off_board = off_board_types[randint(0, 5)]
    typing(f'You have encountered {off_board}. \n')


def found_boundary(self, direction):
    if direction == 'up':
        self.position_one = 0
    elif direction.lower() == 'down':
        move_up(self)
    elif direction == 'right':
        move_left(self)
    elif direction == 'left':
        self.position_two = 0
    boundary()
    typing(f'{self.name} spins around, quickly returning to a safer spot.\n')
    return


## actions according to what the move encounters ##
def action(self, opponent, direction):
    if board[self.position_one][self.position_two] == ' - ':
        make_map(self)
        typing(f'This location seems safe for now...\n')
    elif board[self.position_one][self.position_two] == '||':
        typing(f'{self.name} has run into a wall.\n')
        make_wall(self)
        found_wall(self, direction)
    elif board[self.position_one][self.position_two] == '$$':
        set_path(self)
        find_chest(len(board), self)
    elif board[self.position_one][self.position_two] == '^^':
        map_of_board[self.position_one][self.position_two] = '^^'
        typing(f'{self.name}, you see an enemy ahead! Prepare for ')
        console.print('[red1]COMBAT[/red1]', end='')
        typing(f' with {opponent.name}!!\n')
        combat(self, opponent)
    elif board[self.position_one][self.position_two] == '@>':
        set_path(self)
        find_potion(self)

    out_of_board(self)


## Using the move and actions together to get different results ##
def move(self, opponent, direction):
    if self.position_one == len(board) or self.position_two == len(board):
        out_of_board(self)
        found_boundary(self, direction)
    if board[self.position_one][self.position_two] == '^^':
        pass
    else:
        set_path(self)
    typing(f'{self.name} moves to new position...\n')
    if direction.lower() == 'up' or direction.lower() == 'u':
        move_up(self)
        action(self, opponent, direction)
    if direction.lower() == 'down' or direction.lower() == 'd':
        move_down(self)
        action(self, opponent, direction)
    if direction.lower() == 'right' or direction.lower() == 'r':
        move_right(self)
        action(self, opponent, direction)
    if direction.lower() == 'left' or direction.lower() == 'l':
        move_left(self)
        action(self, opponent, direction)
