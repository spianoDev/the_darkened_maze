def combat(self, enemy, health, damage):
    if (health - damage) <= 0:
        self.health = health - damage
        print(f'{enemy.name} has struck a fatal blow! Your health is now {self.health} and you died...')
        return health
    else:
        self.health = health - damage
        print(f'Your remaining health is {self.health}')
        return health

