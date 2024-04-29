from random import randint
import move as run_away
from map import *

## Player dies ##

def player_died(self):
    if self.health <= 0:
        exit()
    else:
        pass

def combat(self, enemy):
    while enemy.health > 0:
        self_luck = randint(1, 6)
        monster_luck = randint(2, 6)
        print(f'self = {self_luck} and monster = {monster_luck}')
        if self_luck == monster_luck or self_luck > monster_luck:
            typing(f'{self.name} and {enemy.name} eye each other suspiciously...\n')
            reply = input(f'{self.name}, you can try to strike the first blow or run away [fight, run] ')
            if reply == 'fight':
                health_points(self, enemy, enemy.health, self.damage)
            elif reply == 'run':
                if self_luck >= 3:
                    run_away.move(self, enemy, 'left')
                    break
            else:
                typing(f'{self.name} loses balance and falls...\n')
                health_points(enemy, self, self.health, enemy.damage)
        else:
            health_points(enemy, self, self.health, enemy.damage)
            player_died(self)
    map_of_board[self.position_one][self.position_two] = '- '
    board[self.position_one][self.position_two] = '- '


def health_points(attacker, defender, health, damage):
    if defender.health <= 50 and defender.potion > 0:
        use_potion = input(f'{defender}, your health is dropping quickly. Would you like to use a health potion? [yes '
                          f'or no] ')
        if use_potion == 'yes':
            defender.health += 10
            defender.potion -= 1
    if (health - damage) <= 0:
        defender.health = health - damage
        typing(f'{attacker.name} has struck a fatal blow! {defender.name}\'s health is now {defender.health} and '
               f'{defender.name} died...\n')
        return health
    else:
        typing(f'{attacker.name} strikes!\n')
        defender.health = health - damage
        typing(f'{defender.name} remaining health is {defender.health}\n')
        return health

