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

# my_name = input('Player 1 please enter your name: ')

player2 = Hero('computer')
player1 = Hero()

player2.damage = 10

create_monsters()
do_turn(player1, level_aa_monster)
do_turn(player1, level_aa_monster)
do_turn(player1, level_aa_monster)
do_turn(player1, level_aa_monster)
do_turn(player1, level_aa_monster)
do_turn(player1, level_aa_monster)
# do_turn(player2, player1)
