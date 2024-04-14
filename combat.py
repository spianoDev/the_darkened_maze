def combat(self, enemy, health, damage):
    if self.position_one == enemy.position_one and self.position_two == enemy.position_two:
        print(f'{self.name}, you see an enemy ahead! Prepare for COMBAT with {enemy.name}!!')
        if (health - damage) <= 0:
            self.health = health - damage
            print(f'{enemy.name} has struck a fatal blow! Your health is now {self.health} and you died...')
            return health
        else:
            self.health = health - damage
            print(f'Your remaining health is {self.health}')
            return health
    else:
        print(f'This location seems safe for now...')
