from random import randint
from boards import *
from style import typing

## initial find chest function ##
def find_chest(game_level, player):
    chest = randint((game_level * 1), (game_level * 4))
    player.money += chest
    typing(f'Congratulations warrior, you have found a chest containing {chest} coins and now carry'
          f' {player.money} coins!!\n')
    board[player.position_one][player.position_two] = ' - '

## initial find potion function ##
def find_potion(player):
    if player.health < 95:
        answer = input(f'You have found a potion! Your current health is {player.health}%, would you like to restore 5 '
                       'health points? [yes or no] ')
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
