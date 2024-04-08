from random import randint

def find_chest(size, player):
    chest = randint((size * 10), (size * 100))
    player.money += chest
    print(f'Congratulations warrior, you have found a chest containing ${chest} coins and now carry'
          f' {player.money} coins!!\n')
