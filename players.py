from random import randint
from boards import *
from style import typing

random_start_number = randint(0, 3)


def add_leading_zero(answer):
    if len(answer) == 1:
        return '0' + answer
    else:
        return answer


class Hero(object):
    def __init__(self, name='Hero'):
        self.name = name
        self.position_one = 0
        self.position_two = 0
        self.health = 100
        self.damage = 5
        self.experience = 0
        self.money = 5
        self.potion = 0


class Monster(object):
    def __init__(self):
        self.name = 'placeholder'
        self.position_one = -1
        self.position_two = -1
        self.health = 10
        self.damage = 10


myHero = Hero()

monster_names = ['Teeters ', 'Skeeter Bite ', 'Milky Mounds ', 'Jugs Er Knot ', 'Death Hooters ', 'Slimy Boobies ',
                 'Hell\'s Gate Knockers ']
monster_locations = [(pos1, pos2) for pos1, i in enumerate(board)
                     for pos2, y in enumerate(i) if y == '^^']

# print(monster_locations)
monsters = []


def monster_level_stat():
    # for i in range(maze_level):
    stat = randint(8, 12)
    return stat


def create_monsters(maze_level):
    iterator = 1
    for location in monster_locations:
        m = Monster()
        m.name = monster_names[maze_level - 1] + str(iterator)
        m.position_one = location[0]
        m.position_two = location[1]
        m.health = monster_level_stat() * maze_level
        m.damage = monster_level_stat() * maze_level
        m.potion = 0
        iterator += 1
        # print(m.name, m.position_one, m.position_two, m.health, m.damage)
        monsters.append(m)
    # return m


create_monsters(1)


def print_status(person):
    typing(
        f'{person.name} is now in position {person.position_one, person.position_two} with {person.health} health and '
        f'{person.money} coins and {person.potion} potions...\n')
