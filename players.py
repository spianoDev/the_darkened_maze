from random import randint
from boards import *


random_start_number = randint(0,3)

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

class Monster(object):
    def __init__(self, name='Teeters'):
        self.name = name
        self.position_one = -1
        self.position_two = -1
        self.health = 5
        self.damage = 10


# my_name = 'spiano'
myHero = Hero()

# print(board)
monster_locations = [(pos1,pos2) for pos1,i in enumerate(board)
       for pos2,y in enumerate(i) if y == '^^']

# print(monster_locations)

def create_monsters():
    for location in monster_locations:
        iterator = 1
        monster = Monster()
        monster.name = 'Teeters'
        monster.position_one = location[0]
        monster.position_two = location[1]
        monster.health = 5
        monster.damage = 10
        iterator += 1
        print(monster.name, monster.position_one, monster.position_two)
    return


# another_hero = Hero(my_name)
level_aa_monster = Monster()
# level_a_monster = Monster('Skeeter Bite')
# level_a_monster.health = 20
# level_a_monster.damage = 5
# level_b_monster = Monster('Milky Mounds')
# level_c_monster = Monster('Jugs Er Knot')
# level_d_monster = Monster('Death Hooters')
# level_dd_monster = Monster('Slimy Boobies')
# level_ddd_monster = Monster('Hell\'s Gate Knockers')
# def monster_stats(monster):
#     print(f'Monster Stats: {monster.name}, is in position {add_leading_zero(monster.position)} with'
#           f' {monster.health} health')
