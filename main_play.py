from style import *  ## Pull in styling ##
from move import *  ## Pull in the move function ##
from players import *  ## Pull in characters ##
from boards import *
from health import *


def do_turn(player, opponent):
    """Run turn sequence"""
    # print_status(player)
    typing(f'{player.name} what direction would you like to go? [up, down, right, '
           f'left] ')
    move_option = input('')
    typing(f'{player.name} moves to new position...\n')
    map_of_board[player.position_one][player.position_two] = '- '

    move(player, opponent, move_option)
    if player.position_one == len(board) and player.position_two == len(board) - 1:
        return
    else:
        map_of_board[player.position_one][player.position_two] = 'P1'
    typing(f'{player.name}, what would you like to do next? [get status, print map, move] ')
    next_step = input('')
    if next_step == 'get status':
        print_status(player)
    if next_step == 'print map':
        print_map(player)
    else:
        pass
    # print_map(player)


player2 = Hero('computer')

player2.damage = 10

create_monsters()
my_name = input('Player 1 please enter your name: ')
player1 = Hero(my_name)
console.rule('[bold red] The Darkened Maze: Level 1')


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


play_level(player1, monsters)
