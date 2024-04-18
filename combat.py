from style import typing

def combat(self, enemy, health, damage):
    if (health - damage) <= 0:
        self.health = health - damage
        typing(f'{enemy.name} has struck a fatal blow! Your health is now {self.health} and you died...\n')
        return health
    else:
        self.health = health - damage
        typing(f'Your remaining health is {self.health}\n')
        return health

