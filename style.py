## For a more rich terminal output: https://rich.readthedocs.io/en/stable/console.html#attributes ##
from rich.console import Console
console = Console()

from time import sleep

## function to stylize the terminal print commands to look like a typewriter ##
def typing(s):
    for letter in s:
        print(letter, end='', flush=True)
        sleep(.04)


# console.print([1, 2, 3])
# console.print("[blue underline]Looks like a link")
# console.print("FOO", style="black on tan")
