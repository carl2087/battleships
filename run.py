"""
Battleships game that runs in a custom terminal
"""

# Libraries imported into the game
import os
import time
from art import text2art


def type_slow(word):
    """
    Types letters slowly in terminal
    """
    for letter in word:
        time.sleep(0.15)
        print(letter, end="", flush=True)


def type_fast(word):
    """
    Types letters fast in terminal
    """
    for letter in word:
        time.sleep(0.01)
        print(letter, end="", flush=True)


def game_load():
    """
    Shows in terminal when first accessing battleships game.
    """
    print(type_slow("Game Loading....\n"))
    os.system("clear")
    art = text2art("Battle Ships")
    type_fast(art)
    os.system("clear")


def game_rules():
    """
    Prints the games rules to terminal
    """
    time.sleep(1.5)
    type_fast("The aim of the game is to sink all of your ")
    type_fast("opponents ships.\n")
    type_fast("You and the computer will each have their own ")
    type_fast("battlefield grid\n")
    type_fast("Place your ships strategically.\n")
    type_fast("You cannot see your opponents ships ")
    type_fast("and they cannot see yours.\n")
    type_fast("Whoever sinks all of the opponents ")
    type_fast("ships first wins the game.\n")
    time.sleep(4)23
    os.system("clear")


def player_name():
    """
    Uses a while loop to get players name that is letters only
    will repeat until correct data entered.
    """
    while True:
        print("Please enter your name and hit return button.")
        player_name = input("Enter name here:")
        if player_name.isalpha():
            print(f"Welcome {player_name} I hope you're ready for battle.")
            break
        else:
            print("Only letters are allowed")
    return player_name


def main():
    """
    Runs all program functions.
    """
    game_load()
    game_rules()
    player_name()


main()
