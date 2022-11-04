"""
Battleships game that runs in a custom terminal
"""

# Libraries imported into the game
import os
import time
from art import text2art


def type_slow(word):
    """
    Types letters slowley in terminal
    """
    for letter in word:
        time.sleep(0.1)
        print(letter, end="", flush=True)


def game_load():
    """
    Shows in terminal when first accessing battleships game.
    """
    print(type_slow("Game Loading....\n"))
    os.system("clear")
    art = text2art("Battle Ships")
    print(art)


game_load()
