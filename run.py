"""
Battleships game that runs in a custom terminal
"""

import os
import time
from art import text2art


def game_load():
    """
    Shows in terminal when first accessing battleships game.
    """
    print("Game Loading....\n")
    time.sleep(2)
    os.system("clear")
    art = text2art("Battle Ships")
    print(art)


game_load()
