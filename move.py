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
        # print('up', self.position_one, board[self.position_one][self.position_two])
        return
    else:
        typing(f'Up is out of bounds. Returning to {self.position_one, self.position_two}.\n')
        return

def move_down(self):
    if self.position_one <= len(board):
        self.position_one += 1
        return
    else:
        typing(f'Down is out of bounds. Returning to {self.position_one, self.position_two}.\n')
        return

def move_right(self):
    if self.position_two <= len(board):
        self.position_two += 1
        return
    else:
        typing(f'Right is out of bounds. Returning to {self.position_one, self.position_two}.\n')
        return

def move_left(self):
    if self.position_two > 0:
        self.position_two -= 1
        return
    else:
        typing(f'Left is out of bounds. Returning to {self.position_one, self.position_two}.\n')
        return


## actions when encountering a wall in the board ##
def found_wall(self, direction):
    typing(f'You have encountered a wall. ')
    if direction == 'up':
        move_down(self)
    if direction == 'down':
        move_up(self)
    if direction == 'right':
        move_left(self)
    if direction == 'left':
        move_right(self)
    typing(f'Go back to {self.position_one, self.position_two} and try again.\n')
    return

## actions according to what the move encounters ##
def action(self, opponent, direction):
    if self.position_one > len(board) or self.position_two > len(board):
        print('boundary')
        found_wall(self, direction)
    if board[self.position_one][self.position_two] == ' - ':
        map_of_board[self.position_one][self.position_two] = '- '
    if board[self.position_one][self.position_two] == '||':
        map_of_board[self.position_one][self.position_two] = '||'
        found_wall(self, direction)
        action(self, opponent, direction)
    elif board[self.position_one][self.position_two] == '$$':
        map_of_board[self.position_one][self.position_two] = '- '
        find_chest(len(board), self)
    elif board[self.position_one][self.position_two] == '^^':
        map_of_board[self.position_one][self.position_two] = '^^'
        typing(f'{self.name}, you see an enemy ahead! Prepare for COMBAT with {opponent.name}!!\n')
        typing(' .  / \  . \n')
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






