"""
Battleships game that runs in a custom terminal
"""

# Libraries imported into the game
import os
import time
import random
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
    green = "\033[0;32m"


# The length of each ship in the game
LENGTH_OF_SHIP = [2, 3, 3, 4, 4]


# The battleship fields of play boards
PLAYER_BOARD = [[" "] * 8 for i in range(8)]
COMPUTER_BOARD = [[" "] * 8 for i in range(8)]
PLAYER_GUESS_BOARD = [[" "] * 8 for i in range(8)]
COMPUTER_GUESS_BOARD = [[" "] * 8 for i in range(8)]

# Changes letters into integers for the battleship board
letters_to_integers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}


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
        player_name = input("Enter name here: \n").capitalize()
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
        answer = input("Type your answer yes or no?: \n").lower()
        print("\n")
        if answer == "yes":
            type_fast("Welcome to the high seas")
            print("\n")
            start_the_game()
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
    type_fast(Colours.purple + art_one)
    print("\n")
    type_fast(art_two)
    print("\n")
    type_fast(art_three + Colours.white)
    time.sleep(6)
    os.system("clear")
    main()


def battle_boards(board):
    """
    Prints the battle board areas to the terminal.
    Placeholder present to enable manipulation in game.
    """
    print("  A B C D E F G H")
    print("__________________")
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


def place_ship(board):
    """
    Allows the user and the computer to place ships on the board.
    This function will loop through the ship lengths and will also check for
    ship overlap on board.
    """
    for ship in LENGTH_OF_SHIP:
        while True:
            if board == COMPUTER_BOARD:
                ship_place, row, column = random.choice(["h", "v"]), \
                    random.randint(0, 7), random.randint(0, 7)
                if ship_board(ship, row, column, ship_place):
                    if not ship_overlap(board, row, column, ship_place, ship):
                        if ship_place == "h":
                            for i in range(column, column + ship):
                                board[row][i] = "@"
                        else:
                            for i in range(row, row + ship):
                                board[i][column] = "@"
                        break
            else:
                place_your_ship = True
                type_fast("Time to place your ship")
                type_fast(" with a length of " + str(ship))
                print("\n")
                row, column, ship_place = player_choice(place_your_ship)
                if ship_board(ship, row, column, ship_place):
                    if ship_overlap(board, row, column, ship_place, ship):
                        print("You cannot place your ship here!.")
                    else:
                        if ship_place == "h":
                            for i in range(column, column + ship):
                                board[row][i] = "@"
                        else:
                            for i in range(row, row + ship):
                                board[i][column] = "@"
                        battle_boards(PLAYER_BOARD)
                        break


def player_choice(place_your_ship):
    """
    Allows the user to place ships on the board.
    """
    if place_your_ship:
        while True:
            try:
                ship_place = input("Horizontal (H) or Vertical (V)?\n").lower()
                if ship_place == "h" or ship_place == "v":
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please only enter H or V. ")
        while True:
            try:
                row = input("Which row 1 to 8?\n")
                if row in "12345678":
                    row = int(row) - 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please only enter 1 to 8.\n")
        while True:
            try:
                column = input("Which column (A-H)?\n").upper()
                if column not in "ABCDEFGH":
                    print("Please enter a valid letter A to H\n")
                else:
                    column = letters_to_integers[column]
                    break
            except KeyError:
                print("Please only enter A to H\n")
        return row, column, ship_place
    else:
        player_choice(place_your_ship)


def aim_at_ship():
    """
    Allows the player to aim at enemy ships on the board
    """
    while True:
        try:
            row = input("Which row 1 to 8? \n")
            if row in "12345678":
                row = int(row) - 1
                break
            else:
                raise ValueError
        except ValueError:
            print("Please only enter 1 to 8.\n")
    while True:
        try:
            column = input("Which column A to H? \n").upper()
            if column not in "ABCDEFGH":
                print("Please only enter A to H\n")
            else:
                column = letters_to_integers[column]
                break
        except KeyError:
            print("Please only enter A to H\n")
    return row, column


def ship_overlap(board, row, column, ship_place, ship):
    """
    Checks if ships overlap when computer or players
    places them on board.
    """
    if ship_place == "h":
        for i in range(column, column + ship):
            if board[row][i] == "@":
                return True
    else:
        for i in range(row, row + ship):
            if board[i][column] == "@":
                return True
    return False


def ship_board(ship, row, column, ship_place):
    """
    Function checks if ships are placed within the board
    if they are placed off the board then an error message is
    printed to player.
    """
    if ship_place == "h":
        if column + ship > 8:
            return False
        else:
            return True
    else:
        if row + ship > 8:
            return False
        else:
            return True


def player_turn(board):
    """
    This function cycles between player and computer turns to play the game
    """
    if board == PLAYER_GUESS_BOARD:
        row, column = aim_at_ship()
        if board[row][column] == "O":
            type_fast("You've already aimed there!!")
            print("\n")
            player_turn(board)
        elif board[row][column] == "X":
            type_fast("You've already aimed there!!")
            print("\n")
            player_turn(board)
        elif COMPUTER_BOARD[row][column] == "@":
            board[row][column] = "X"
            type_fast(Colours.green + "You hit them!!" + Colours.white)
            print("\n")
        else:
            board[row][column] = "O"
            type_fast(Colours.red + "You missed them better luck next time!"
                      + Colours.white)
            print("\n")
    else:
        row, column = random.randint(0, 7), random.randint(0, 7)
        if board[row][column] == "O":
            player_turn(board)
        elif board[row][column] == "X":
            player_turn(board)
        elif PLAYER_BOARD[row][column] == "@":
            board[row][column] = "X"
            type_fast(Colours.red + "We have been hit!!!" + Colours.white)
            print("\n")
        else:
            board[row][column] = "O"
            type_fast(Colours.green + "The computer MISSED!!!" + Colours.white)


def start_the_game():
    """
    This function holds the code that starts the game after
    the introductory screens.
    """
    place_ship(COMPUTER_BOARD)
    battle_boards(PLAYER_BOARD)
    place_ship(PLAYER_BOARD)
    while True:
        while True:
            type_fast("Time to pick your shot!!")
            print("\n")
            battle_boards(PLAYER_GUESS_BOARD)
            player_turn(PLAYER_GUESS_BOARD)
            time.sleep(1.5)
            break
        if score_count(PLAYER_GUESS_BOARD) == 16:
            art = text2art("YOU HAVE WON!")
            type_fast(Colours.purple + art + Colours.white)
            play_game_again()
            break
        while True:
            player_turn(COMPUTER_GUESS_BOARD)
            time.sleep(1.5)
            break
        battle_boards(COMPUTER_GUESS_BOARD)
        if score_count(COMPUTER_GUESS_BOARD) == 16:
            art = text2art("YOU LOST :(")
            type_fast(Colours.red + art + Colours.white)
            play_game_again()
            break


def score_count(board):
    """
    Counts the number of succesful hits on the ships, keeps
    track of the score to end game when all ships sunk.
    """
    hit_count = 0
    for row in board:
        for column in row:
            if column == "X":
                hit_count += 1
    return hit_count


def play_game_again():
    """
    Asks if player wants to play again enables game to restart without first
    loading screens.
    """
    while True:
        answer = input("would you like to play again? \n").lower()
        if answer == "yes":
            start_the_game()
        elif answer == "no":
            art = text2art("Goodbye")
            type_fast(Colours.yellow + art + Colours.white)
            time.sleep(2)
            main()
        else:
            type_fast("You must enter yes or no.")
            print("\n")


def main():
    """
    Runs program functions to start the battleship game.
    """
    game_load()
    game_rules()
    play_game()


main()
