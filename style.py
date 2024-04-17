## For a more rich terminal output: https://rich.readthedocs.io/en/stable/console.html#attributes ##

from time import sleep

## function to stylize the terminal print commands to look like a typewriter ##
def typing(s):
    for letter in s:
        print(letter, end='', flush=True)
        sleep(.04)
