from random import randint

class Hero(object):
    def __init__(self, name='Hero'):
        self.name = name
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0
        self.money = 30

class Monster(object):
    def __init__(self, name='Teeters'):
        self.name = name
        self.position = str(randint(0, 100))
        self.health = 10
        self.damage = 2


my_name = 'spiano'
myHero = Hero()

another_hero = Hero(my_name)
level_aa_monster = Monster()
level_a_monster = Monster('Skeeter Bite')
level_b_monster = Monster('Milky Mounds')
level_c_monster = Monster('Jugs Er Knot')
level_d_monster = Monster('Death Hooters')
level_dd_monster = Monster('Slimy Boobies')
level_ddd_monster = Monster('Hell\'s Gate Knockers')
print(level_aa_monster.name)
