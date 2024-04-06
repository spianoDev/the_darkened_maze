from players import *



def move(self, direction):
    if direction == 'up' and int(self.position) < 10:
        print(f'Direction {direction} is out of bounds. {self.name} remains on position {self.position}')
        return
    elif direction == 'up' and int(self.position) >= 10:
        self.position = add_leading_zero(str(int(self.position) - 10))
        print(f'{self.name}\'s new position is {add_leading_zero(self.position)}')
        return add_leading_zero(self.position)
    if direction == 'down' and int(self.position) > 34:
        print(f'Direction {direction} is out of bounds. {self.name} remains on position {self.position}')
        return
    elif direction == 'down' and int(self.position) < 44:
        self.position = add_leading_zero(str(int(self.position) + 10))
        print(f'{self.name}\'s new position is {add_leading_zero(self.position)}')
        return add_leading_zero(self.position)
    if direction == 'left' and int(self.position) % 10 == 0:
        print(f'Direction {direction} is out of bounds. {self.name} remains on position {self.position}')
        return
    elif direction == 'left' and int(self.position) % 10 != 0:
        self.position = add_leading_zero(str(int(self.position) - 1))
        print(f'{self.name}\'s new position is {add_leading_zero(self.position)}')
        return add_leading_zero(self.position)
    if direction == 'right' and (int(self.position) + 1) % 5 == 0:
        print(f'Direction {direction} is out of bounds. {self.name} remains on position {self.position}')
        return
    elif direction == 'right' and (int(self.position) + 1) % 5 != 0:
        self.position = add_leading_zero(str(int(self.position) + 1))
        print(f'{self.name}\'s new position is {add_leading_zero(self.position)}')
        return add_leading_zero(self.position)
    else:
        raise ValueError(f'Direction is not valid. {self.name} remains on position {self.position}')

Hero.move = move
