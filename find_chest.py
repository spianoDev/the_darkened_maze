from random import randint
from boards import *

def find_chest(game_level, player):
    chest = randint((game_level * 1), (game_level * 4))
    player.money += chest
    print(f'Congratulations warrior, you have found a chest containing {chest} coins and now carry'
          f' {player.money} coins!!\n')
    board[player.position_one][player.position_two] = ' - '

