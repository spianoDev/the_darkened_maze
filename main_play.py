from random import randint
from time import sleep
from combat import * ## Pull in the combat function ##
from move import * ## Pull in the move function ##
from health import * ## Pull in buy health function ##
from players import *

dice_roll = randint(1, 6)
move_options = ['blank', 'right', 'left', 'up', 'down', 'left', 'right']
def typing(s):
    for letter in s:
        print(letter, end='', flush=True)
        sleep(.05)

def do_turn(player, opponent):

    def get_coins():
        coin_win = randint(10, 100)
        player.money += coin_win
        typing(f'Congratulations warrior, you have won ${coin_win} and now carry {player.money}!!\n')

    def print_status(person):
        # print(person.name, person.position, person.health, person.damage, person.experience, person.money)
        typing(f'{person.name} is now in position {person.position} with {person.health} health and '
               f'{person.money} coins...\n')

    '''Run turn sequence'''
    typing(f'New turn: {player.name} rolls {dice_roll}\n')
    typing(f'{player.name} moves to new position...\n')
    typing('. . . . . . . . \n')
    player.move(move_options[dice_roll])
    combat(player, opponent, player.health, opponent.damage)
    get_coins()
    buy_health(player, player.health, player.money)
    print_status(player)

# my_name = input('Player 1 please enter your name: ')

player2 = Hero('computer')
player1 = Hero()

player2.damage = 10



Hero.move = move

do_turn(player1, level_aa_monster)
do_turn(player2, player1)
