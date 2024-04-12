from players import *
from boards import *
from find_chest import *
from combat import *

pos_one = 0
pos_two = 0

def move_up(self):
    if pos_one > 0:
        self.position = board[pos_one - 1][pos_two]
        print(self.position, pos_one, pos_two)
    else:
        print('out of bounds')

def move_down(self):
    if pos_one < 3:
        self.position = board[pos_one + 1][pos_two]
        print(self.position, pos_one, pos_two)
    else:
        print('out of bounds')

def move_right(self):
    if pos_two < 3:
        self.position = board[pos_one][pos_two + 1]
        print(self.position, pos_one, pos_two)
    else:
        print('out of bounds')

def move_left(self):
    if pos_two > 0:
        self.position = board[pos_one][pos_two - 1]
        print(self.position, pos_one, pos_two)
    else:
        print('out of bounds')


def found_wall(self, place):
    if self.position == '||':
        print(f'You have encountered a wall.\n')
        if place == 'up':
            move_down(self)
        if place == 'down':
            move_up(self)
        if place == 'right':
            move_left(self)
        if place == 'left':
            move_right(self)
        print(f'Go back to {self.position} and try again')
        return

def move(self, direction):
    if direction == 'up':
        move_up(self)
    if direction == 'down':
        move_down(self)
    if direction == 'right':
        move_right(self)
    if direction == 'left':
        print(f'Direction {direction} is out of bounds. {self.name} remains on position {self.position}')
        move_left(self)
    if self.position == '||':
        found_wall(self, direction)
    elif self.position == '$$':
        find_chest(1, self)
    elif self.position == '^^':
        combat(self, level_aa_monster, self.health, level_aa_monster.damage)

Hero.move = move
