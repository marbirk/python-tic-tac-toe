#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Marcel Birkhahn"
__version__ = "0.1.0"
__license__ = "MIT"

from random import randint

player_weapon = ''
last_user_input = 0
boardFields = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
turn = 0


def get_logo():
    print("___________.__         ___________                ___________")
    print("\__    ___/|__| ____   \__    ___/____     ____   \__    ___/___   ____")
    print("  |    |   |  |/ ___\    |    |  \__  \  _/ ___\    |    | /  _ \_/ __ \ ")
    print("  |    |   |  \  \___    |    |   / __ \ \  \___    |    |(  <_> )  ___/")
    print("  |____|   |__|\___  >   |____|  (____  / \___  >   |____| \____/ \___  >")
    print("                   \/                 \/     \/                      \/ ")
    print(" ")
    print("Welcome Stranger!")
    print(" ")
    print(" ")


def ask_player_for_weapon():
    print("Please choose your weapon! X or O? ;-)")
    global player_weapon
    player_weapon = input().upper()
    return player_weapon


def field_already_used():
    print("Field is already used! Please choose another field!")
    player_action()


def player_action():
    print("It's your turn! Type a number from 1 to 9!")
    global last_user_input
    last_user_input = input()
    global boardFields
    if boardFields[int(last_user_input)] == 'X':
        field_already_used()
    if boardFields[int(last_user_input)] == 'O':
        field_already_used()
    else:
        boardFields[int(last_user_input)] = player_weapon


def is_field_empty(field):
    if boardFields[field] != " ":
        return False
    else:
        return True


def set_computer_on_board(field_number):
    if player_weapon == "X":
        boardFields[field_number] = "O"
    else:
        boardFields[field_number] = "X"


def computer_action():
    global boardFields
    prev_field = int(last_user_input) - 1
    if last_user_input == 0:
        set_computer_on_board(randint(1, 9))
    else:
        print(prev_field)


def get_introduction():
    print("Do you need an introduction? Type yes or no!")
    answer = input()
    if answer == 'yes':
        print("Tic-tac-toe is a paper-and-pencil game for two players, "
              "X and O, who take turns marking the spaces in a 3×3 grid.\n"
              "The player who succeeds in placing three of their marks in a horizontal, "
              "vertical, or diagonal row wins the game.")
        print(" ")
        print("Use numbers for placing your marker on the board. Here is an example:")
        print(" ")
        print("1 | 2 | 3")
        print("---------")
        print("4 | 5 | 6")
        print("---------")
        print("7 | 8 | 9")
        print(" ")
        print(" ")
    else:
        return


def draw_board():
    print(boardFields[1] + " | " + boardFields[2] + " | " + boardFields[3])
    print("---------")
    print(boardFields[4] + " | " + boardFields[5] + " | " + boardFields[6])
    print("---------")
    print(boardFields[7] + " | " + boardFields[8] + " | " + boardFields[9])


def play_round():
    if turn == 1:
        player_action()
        computer_action()
        draw_board()
    if turn == 2:
        computer_action()
        draw_board()
        player_action()


def decide_who_goes_first():
    global turn
    turn = randint(1, 2)
    if turn == 2:
        print("The computer go first!")
    for x in range(0, len(boardFields)-1):
        play_round()


def main():
    get_logo()
    get_introduction()
    ask_player_for_weapon()
    decide_who_goes_first()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
