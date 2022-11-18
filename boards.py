"""
Module to hold the boards that areprinted that the battleships
game is played on.
"""


def battle_boards(board):
    """
    Prints the battle board areas to the terminal.
    Placeholder present to enable manipulation in game.
    """
    print("  A B C D E F G H")
    print("__________________")
    row_num = 1
    for row in board:
        print(f"{row_num}|{'|'.join(row)}|")
        row_num += 1
