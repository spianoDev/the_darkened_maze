from random import randint
from boards import *
from style import *
from health import *


chest_image = '[gold3] ._____._____.  \n/_____/|\\____/ \\\n\\             \\ )\n/____[yellow1] $$$ [/yellow1]____/ |\n|             | |\n|_____/|\\_____| /\n'
potion_image = '  |~|  \n.\'[green]o0o[/green]`.\n`.___.\'\n'


## print image of item ##
def print_image(item):
    console.print(item)


## initial find chest function ##
def find_chest(game_level, player):
    chest = randint((game_level * 1), (game_level * 4))
    player.money += chest
    print_image(chest_image)
    typing(f'Congratulations {player.name}, you have found a chest containing {chest} coins and now carry'
           f' {player.money} coins!!\n')
    board[player.position_one][player.position_two] = ' - '


## initial find potion function ##
def find_potion(player):
    print_image(potion_image)
    typing(f'Incredible {player.name}! You have found a health potion!!\n')
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
