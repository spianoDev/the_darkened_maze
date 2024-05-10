from style import *  ## Pull in styling ##
from move import *  ## Pull in the move function ##
from players import *  ## Pull in characters ##
from boards import *
from health import *


def print_options(self, opponent, user_input):
    if user_input.lower() == 'get status' or user_input.lower() == 's':
        print_status(self)
    if user_input.lower() == 'print map' or user_input.lower() == 'm':
        print_map(self)
    if user_input.lower() == 'both' or user_input.lower() == 'b':
        print_status(self)
        print_map(self)
    else:
        move(self, opponent, user_input)


def do_turn(player, opponent):
    """Run turn sequence"""
    typing(f'{player.name} what direction would you like to go? \n'
           f'[u = up, d = down, r = right, l = left] ')
    move_option = input('')
    typing(f'{player.name} moves to new position...\n')
    map_of_board[player.position_one][player.position_two] = '- '

    move(player, opponent, move_option)
    if player.position_one == len(board) and player.position_two == len(board) - 1:
        return
    else:
        map_of_board[player.position_one][player.position_two] = 'P1'
    typing(f'{player.name}, what would you like to do next? \n'
           f'[s = get status, m = print map, b = both, or move u = up, d = down, r = right, l = left] ')
    next_step = input('')
    print_options(player, opponent, next_step)


player2 = Hero('computer')

player2.damage = 10

create_monsters(1)


def play_level(player, enemy):
    while player.position_one < len(board) and player.position_two < len(board):
        if enemy[0].health > 0:
            do_turn(player1, enemy[0])
        elif enemy[1].health > 0:
            do_turn(player1, enemy[1])
        else:
            do_turn(player, enemy)
    typing(f'Congratulations {player.name}, you have solved the maze!\n')
    typing(f'Before continuing to the next level, you have the option to restore your health.\n')
    buy_health(player, player.health, player.money, player.potion)


print('\n')
console.rule('[bold red] The Darkened Maze: Level 1')
print('\n')
my_name = input('Player 1 please enter your name: ')
player1 = Hero(my_name)

typing(f'{player1.name}, you have discovered a maze! Do you have the courage to enter? [e = enter, a = avoid] \n')
play_game = input('')
if play_game.lower() == 'enter' or play_game.lower() == 'e':
    play_level(player1, monsters)
else:
    typing(f'{player1.name}, fair thee well... \n')
    sleep(2)
    typing('A creaking sound behind you forces you to turn around just in time to see the maze entrance obscure '
           'itself with vines and brambles.\n')




