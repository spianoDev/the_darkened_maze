from players import *
from boards import *
from find_chest import *
from combat import *

def move_up(self):
    if self.position_one > 0:
        self.position_one -= 1
        print('up', self.position_one, board[self.position_one][self.position_two])
        return
    else:
        print('out of bounds')
        return

def move_down(self):
    if self.position_one < 3:
        self.position_one += 1
        print('down', self.position_one, board[self.position_one][self.position_two])
        return
    else:
        print('out of bounds')
        return

def move_right(self):
    if self.position_two < 3:
        self.position_two += 1
        print('right', self.position_two, board[self.position_one][self.position_two])
        return
    else:
        print('out of bounds')
        return

def move_left(self):
    if self.position_two > 0:
        self.position_two -= 1
        print('left', self.position_two, board[self.position_one][self.position_two])
        return
    else:
        print('out of bounds')
        return


def found_wall(self, direction):
    print(f'You have encountered a wall.')
    if direction == 'up':
        move_down(self)
    if direction == 'down':
        move_up(self)
    if direction == 'right':
        move_left(self)
    if direction == 'left':
        move_right(self)
    print(f'Go back to {self.position_one, self.position_two} and try again')
    return

def move(self, direction):
    if direction == 'up':
        move_up(self)
    if direction == 'down':
        move_down(self)
    if direction == 'right':
        move_right(self)
    if direction == 'left':
        move_left(self)
    if board[self.position_one][self.position_two] == '||':
        found_wall(self, direction)
    elif board[self.position_one][self.position_two] == '$$':
        find_chest(1, self)
    elif board[self.position_one][self.position_two] == '^^':
        combat(self, level_aa_monster, self.health, level_aa_monster.damage)

Hero.move = move
