from boards import *
from map import *
from find_treasure import *
from combat import *
from players import *
from style import typing

## Basic move functions without hard coded values ##
def move_up(self):
    if self.position_one > 0:
        self.position_one -= 1
        return
    else:
        found_wall(self, 'up', 'the boundary')
        return

def move_down(self):
    if self.position_one < len(board):
        self.position_one += 1
        return
    else:
        found_wall(self, 'down', 'the boundary')
        return

def move_right(self):
    if self.position_two < len(board):
        self.position_two += 1
        return
    else:
        found_wall(self, 'right', 'the boundary')
        return

def move_left(self):
    if self.position_two > 0:
        self.position_two -= 1
        return
    else:
        found_wall(self, 'left', 'the boundary')
        return


## actions when encountering a wall in the board ##
def found_wall(self, direction, barrier):
    typing(f'You have encountered {barrier}. ')
    if direction == 'up':
        if barrier == 'the boundary':
            self.position_one = 0
        else:
            move_down(self)
    if direction == 'down':
        if barrier == 'the boundary':
            self.position_one = len(board) - 1
        else:
            move_up(self)
    if direction == 'right':
        move_left(self)
    if direction == 'left':
        move_right(self)
    typing(f'Go back to {self.position_one, self.position_two} and try again.\n')
    return

## actions according to what the move encounters ##
def action(self, opponent, direction):
    if self.position_one < len(board) and self.position_two == len(board):
        print(f'{self.name} is now out of the maze')
        return
    if self.position_one == len(board) and self.position_two < len(board):
        print(f'{self.name} is now out of the maze')
        return
    if self.position_one == len(board) or self.position_two == len(board):
        print('boundary')
        found_wall(self, direction, 'the boundary')
    if board[self.position_one][self.position_two] == ' - ':
        map_of_board[self.position_one][self.position_two] = '- '
    if board[self.position_one][self.position_two] == '||':
        map_of_board[self.position_one][self.position_two] = '||'
        found_wall(self, direction, 'a wall')
        action(self, opponent, direction)
    elif board[self.position_one][self.position_two] == '$$':
        map_of_board[self.position_one][self.position_two] = '- '
        find_chest(len(board), self)
    elif board[self.position_one][self.position_two] == '^^':
        map_of_board[self.position_one][self.position_two] = '^^'
        typing(f'{self.name}, you see an enemy ahead! Prepare for COMBAT with {opponent.name}!!\n')
        combat(self, opponent, self.health, opponent.damage)
    elif board[self.position_one][self.position_two] == '@>':
        map_of_board[self.position_one][self.position_two] = '- '
        find_potion(self)
    else:
        typing(f'This location seems safe for now...\n')

## Using the move and actions together to get different results ##
def move(self, opponent, direction):
    if direction == 'up':
        move_up(self)
        action(self, opponent, direction)
    if direction == 'down':
        move_down(self)
        action(self, opponent, direction)
    if direction == 'right':
        move_right(self)
        action(self, opponent, direction)
    if direction == 'left':
        move_left(self)
        action(self, opponent, direction)






