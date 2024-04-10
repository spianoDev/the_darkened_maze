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
        self.position = board[0][0]
        self.health = 100
        self.damage = 5
        self.experience = 0
        self.money = 30

class Monster(object):
    def __init__(self, name='Teeters'):
        self.name = name
        self.position = board[1][1]
        self.health = 10
        self.damage = 2


my_name = 'spiano'
myHero = Hero()

another_hero = Hero(my_name)
level_aa_monster = Monster()
level_a_monster = Monster('Skeeter Bite')
level_a_monster.health = 20
level_a_monster.damage = 5
level_b_monster = Monster('Milky Mounds')
level_c_monster = Monster('Jugs Er Knot')
level_d_monster = Monster('Death Hooters')
level_dd_monster = Monster('Slimy Boobies')
level_ddd_monster = Monster('Hell\'s Gate Knockers')
def monster_stats(monster):
    print(f'Monster Stats: {monster.name}, is in position {add_leading_zero(monster.position)} with'
      f' {monster.health} health')

monster_stats(level_aa_monster)
level_aa_monster.position = board[1][1]
# level_a_monster.position = board[3][0]
# monster_stats(level_a_monster)
