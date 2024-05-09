from boards import *
from map import *
from random import randint
from find_treasure import *
from combat import *
from players import *
from style import *

# combat = '[blink][red]COMBAT![/blink]'
# print_combat = console.print(combat)

# def special_words(word):
#     console.print(word)


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


## actions when encountering a wall or the boundary of the board ##
def found_wall(self, direction, barrier):
    if direction == 'up':
        if barrier == 'the boundary':
            self.position_one = 0
            boundary()
        else:
            move_down(self)
    if direction == 'down':
        if barrier == 'the boundary':
            self.position_one = len(board) - 1
            boundary()
        else:
            move_up(self)
    if direction == 'right':
        if barrier == 'the boundary':
            self.position_two = len(board) - 1
            boundary()
        else:
            move_left(self)
    if direction == 'left':
        if barrier == 'the boundary':
            self.position_two = 0
            boundary()
        else:
            move_right(self)
    typing(f'{self.name} spins around, remaining on the same space.\n')
    return


def boundary():
    off_board_types = ['a thicket of thorny brambles', 'a 2000 foot drop', 'the side of a mountain',
                       'swirling water rapids', 'a black abyss', 'molten lava']
    off_board = off_board_types[randint(0, 5)]
    typing(f'You have encountered {off_board}. \n')


## actions according to what the move encounters ##
def action(self, opponent, direction):
    if self.position_one == len(board) and self.position_two == len(board) - 1:
        return
    if self.position_one == len(board) or self.position_two == len(board):
        if self.position_one < len(board) or self.position_two < len(board):
            found_wall(self, direction, 'the boundary')
        else:
            print(f'{self.name} is now out of the maze')
        return
    if board[self.position_one][self.position_two] == ' - ':
        map_of_board[self.position_one][self.position_two] = '- '
    if board[self.position_one][self.position_two] == '||':
        typing(f'{self.name} has run into a wall.\n')
        map_of_board[self.position_one][self.position_two] = '||'
        found_wall(self, direction, 'a wall')
        action(self, opponent, direction)
    elif board[self.position_one][self.position_two] == '$$':
        map_of_board[self.position_one][self.position_two] = '- '
        find_chest(len(board), self)
    elif board[self.position_one][self.position_two] == '^^':
        map_of_board[self.position_one][self.position_two] = '^^'
        typing(f'{self.name}, you see an enemy ahead! Prepare for COMBAT! with {opponent.name}!!\n')
        combat(self, opponent)
    elif board[self.position_one][self.position_two] == '@>':
        map_of_board[self.position_one][self.position_two] = '- '
        find_potion(self)
    else:
        typing(f'This location seems safe for now...\n')


## Using the move and actions together to get different results ##
def move(self, opponent, direction):
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
