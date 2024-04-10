from players import *
from boards import *
from find_chest import *
from combat import *

pos_one = 0
pos_two = 0

def move(self, direction):
    if direction == 'up' and random_start_number > 0:
        self.position = board[random_start_number - 1][0]
        print(self.position)
    if direction == 'down' and random_start_number < 3:
        self.position = board[random_start_number + 1][0]
        print(self.position)
    if direction == 'right':
        self.position = board[random_start_number][pos_two + 1]
        print(self.position)
    if direction == 'left':
        print(f'Direction {direction} is out of bounds. {self.name} remains on position {self.position}')
    if self.position == '||':
        print(f'You have encountered a wall.')
    elif self.position == '$$':
        find_chest(1, self)
    elif self.position == '^^':
        combat(self, level_aa_monster, self.health, level_aa_monster.damage)
    #
    #     return
    # elif direction == 'up' and int(self.position) >= 10:
    #     self.position = add_leading_zero(str(int(self.position) - 10))
    #     print(f'{self.name}\'s new position is {add_leading_zero(self.position)}')
    #     return add_leading_zero(self.position)
    # if direction == 'down' and int(self.position) > 34:
    #     print(f'Direction {direction} is out of bounds. {self.name} remains on position {self.position}')
    #     return
    # elif direction == 'down' and int(self.position) < 44:
    #     self.position = add_leading_zero(str(int(self.position) + 10))
    #     print(f'{self.name}\'s new position is {add_leading_zero(self.position)}')
    #     return add_leading_zero(self.position)
    # if direction == 'left' and int(self.position) % 10 == 0:
    #     print(f'Direction {direction} is out of bounds. {self.name} remains on position {self.position}')
    #     return
    # elif direction == 'left' and int(self.position) % 10 != 0:
    #     self.position = add_leading_zero(str(int(self.position) - 1))
    #     print(f'{self.name}\'s new position is {add_leading_zero(self.position)}')
    #     return add_leading_zero(self.position)
    # if direction == 'right' and (int(self.position) + 1) % 5 == 0:
    #     print(f'Direction {direction} is out of bounds. {self.name} remains on position {self.position}')
    #     return
    # elif direction == 'right' and (int(self.position) + 1) % 5 != 0:
    #     self.position = add_leading_zero(str(int(self.position) + 1))
    #     print(f'{self.name}\'s new position is {add_leading_zero(self.position)}')
    #     return add_leading_zero(self.position)
    # else:
    #     raise ValueError(f'Direction is not valid. {self.name} remains on position {self.position}')

Hero.move = move
