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
        typing('out of bounds\n')
        return

def move_down(self):
    if self.position_one <= len(board):
        self.position_one += 1
        # print('down', self.position_one, board[self.position_one][self.position_two])
        return
    else:
        typing('out of bounds\n')
        return

def move_right(self):
    if self.position_two <= len(board):
        self.position_two += 1
        # print('right', self.position_two, board[self.position_one][self.position_two])
        return
    else:
        typing('out of bounds\n')
        return

def move_left(self):
    if self.position_two > 0:
        self.position_two -= 1
        # print('left', self.position_two, board[self.position_one][self.position_two])
        return
    else:
        typing('out of bounds\n')
        return


## actions when encountering a wall in the board ##
def found_wall(self, direction):
    typing(f'You have encountered a wall.')
    if direction == 'up':
        move_down(self)
    if direction == 'down':
        move_up(self)
    if direction == 'right':
        move_left(self)
    if direction == 'left':
        move_right(self)
    typing(f'Go back to {self.position_one, self.position_two} and try again')
    return

## actions according to what the move encounters ##
def action(self, opponent, direction):
    if board[self.position_one][self.position_two] == '||':
        found_wall(self, direction)
        action(self, opponent, direction)
    elif board[self.position_one][self.position_two] == '$$':
        find_chest(len(board), self)
    elif board[self.position_one][self.position_two] == '^^':
        print(f'{self.name}, you see an enemy ahead! Prepare for COMBAT with {opponent.name}!!')
        combat(self, opponent, self.health, opponent.damage)
    elif board[self.position_one][self.position_two] == '@>':
        find_potion(self)
    else:
        typing(f'This location seems safe for now...')

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






