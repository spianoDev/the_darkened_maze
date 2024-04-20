from style import * ## Pull in styling ##
from move import * ## Pull in the move function ##
from players import * ## Pull in characters ##

def do_turn(player, opponent):
    def print_status(person):
        # print(person.name, person.position, person.health, person.damage, person.experience, person.money)
        typing(f'{person.name} is now in position {person.position_one, person.position_two} with {person.health} health and '
               f'{person.money} coins...\n')

    '''Run turn sequence'''
    print_status(player)
    typing(f'New turn: {player.name} what direction would you like to try next? [up, down, right, '
                          f'left] ')
    move_option = input('')
    typing(f'{player.name} moves to new position...\n')
    # typing('. . . . . . . . \n')
    move(player, opponent, move_option)
    print_map()

player2 = Hero('computer')


player2.damage = 10

create_monsters()
my_name = input('Player 1 please enter your name: ')
player1 = Hero(my_name)

def play_level(player):
    while player.position_one < len(board) and player.position_one < len(board):
        if player.position_one == len(board) and player.position_two == len(board):
            print(f'Congratulations {player}, you have solved the board!')
        do_turn(player1, level_aa_monster)

play_level(player1)
