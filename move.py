from players import *
from boards import *
from find_chest import *
from combat import *

def move_up(self):
    if self.position_one > 0:
        self.position_one -= 1
        print(self.position_one, board[self.position_one][self.position_two])
        return
    else:
        print('out of bounds')
        return

def move_down(self):
    if self.position_one < 3:
        self.position_one += 1
        print(self.position_one, board[self.position_one][self.position_two])
        return
    else:
        print('out of bounds')
        return

# def move_right(self):
#     if pos_two < 3:
#         self.position = board[pos_one][pos_two + 1]
#         print('right', self.position, pos_one, pos_two + 1)
#         return pos_two + 1, self.position
#     else:
#         print('out of bounds')
#         return self.position
#
# def move_left(self):
#     if pos_two > 0:
#         self.position = board[pos_one][pos_two - 1]
#         print(self.position, pos_one, pos_two - 1)
#         return pos_two - 1, self.position
#     else:
#         print('out of bounds')
#         return self.position


# def found_wall(self, place):
#     if self.position == '||':
#         print(f'You have encountered a wall.')
#         if place == 'up':
#             move_down(self)
#         if place == 'down':
#             move_up(self)
#         if place == 'right':
#             move_left(self)
#         if place == 'left':
#             move_right(self)
#         print(f'Go back to {self.position} and try again')
#         return

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
    # if self.position == '||':
    #     found_wall(self, direction)
    # elif self.position == '$$':
    #     find_chest(1, self)
    # elif self.position == '^^':
    #     combat(self, level_aa_monster, self.health, level_aa_monster.damage)

Hero.move = move
