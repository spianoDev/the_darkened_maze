from random import randint
from boards import *
from style import typing
from health import *

potion_image = '  |~|  \n.\'   `.\n`.___.\'\n'
chest_image = (' ._____._____.  \n/_____/|\\____/ \\\n\\             \\ )\n/____ $$$ ____/ |\n|             | '
               '|\n|_____/|\\_____| /\n')
print(chest_image)


## print image of item ##
def print_image(item):
    typing(item)


## initial find chest function ##
def find_chest(game_level, player):
    chest = randint((game_level * 1), (game_level * 4))
    player.money += chest
    typing(f'Congratulations {player.name}, you have found a chest containing {chest} coins and now carry'
           f' {player.money} coins!!\n')
    print_image(chest_image)
    board[player.position_one][player.position_two] = ' - '


## initial find potion function ##
def find_potion(player):
    typing(f'Incredible {player.name}! You have found a health potion!!\n')
    print_image(potion_image)
    if player.health < 95:
        answer = input(f'Your current health is {player.health}%, would you like to restore 5 '
                       'health points? [yes or no] \n')
        if answer == 'yes':
            player.health += 5
            typing(f'Excellent! A potion will heal your battle wounds. Health restored to {player.health}.\n')
        else:
            typing(f'Storing potion for now...')
            player.potion += 1
    else:
        player.potion += 1
        typing(f'You are in perfect health, you pick up this potion for later. You now hold {player.potion} potions.\n')
    board[player.position_one][player.position_two] = ' - '
