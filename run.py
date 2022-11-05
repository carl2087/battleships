"""
Battleships game that runs in a custom terminal
"""

# Libraries imported into the game
import os
import time
from art import text2art


class Colours:
    """
    Class of colours for different segments of text in game
    """
    red = '\033[91m'
    blue = '\033[94m'
    yellow = '\033[93m'
    purple = '\033[95m'
    white = '\033[0m'


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
    type_fast(Colours.purple + art + Colours.white)
    time.sleep(1)
    os.system("clear")


def game_rules():
    """
    Prints the games rules to terminal
    """
    type_fast("The aim of the game is to sink all of your ")
    type_fast("opponents ships.\n")
    type_fast("You and the computer will each have their own ")
    type_fast("battlefield grid\n")
    type_fast("Place your ships strategically.\n")
    type_fast("You cannot see your opponents ships ")
    type_fast("and they cannot see yours.\n")
    type_fast("Whoever sinks all of the opponents ")
    type_fast("ships first wins the game.\n")
    time.sleep(3)
    os.system("clear")


def get_player_name():
    """
    Uses a while loop to get players name that is letters only
    will repeat until correct data entered.
    """
    while True:
        type_fast("Please enter your name and hit return button.\n")
        player_name = input("Enter name here: ").capitalize()
        print("\n")
        if player_name.isalpha():
            type_fast(f"Welcome {player_name} I hope you're ready for battle")
            print("\n")
            break
        else:
            type_fast("Only letters are allowed.\n")
    return player_name


def play_game():
    """
    Asks player if they want to play game will exit game if they say no.
    """
    player_name = get_player_name()
    type_fast(f"So {player_name} are you up for the challenge?")
    while True:
        print("\n")
        answer = input("Type your answer yes or no?: ").lower()
        print("\n")
        if answer == "yes":
            type_fast("Welcome to the high seas")
            break
        elif answer == "no":
            type_fast("Hope to see you on the high seas soon")
            print("\n")
            time.sleep(2)
            os.system("clear")
            exit_game()
            break
        else:
            type_fast("Error, answer must be yes or no")


def exit_game():
    """
    Exit game that shows if a player decides not to play battle ships.
    """
    art_one = text2art("Goodbye")
    art_two = text2art("Hope to see")
    art_three = text2art("you again")
    type_fast(art_one)
    print("\n")
    type_fast(art_two)
    print("\n")
    type_fast(art_three)
    time.sleep(6)
    os.system("clear")
    main()


def main():
    """
    Runs all program functions.
    """
    game_load()
    game_rules()
    play_game()


main()
