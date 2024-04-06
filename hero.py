class Hero(object):
    def __init__(self, name='Hero'):
        self.name = name
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0
        self.money = 30

my_name = 'spiano'
myHero = Hero()

another_hero = Hero(my_name)
