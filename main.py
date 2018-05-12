#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Marcel Birkhahn"
__version__ = "0.1.0"
__license__ = "MIT"

from random import randint

player_weapon = ''
computer_weapon = ''
last_user_input = 0
boardFields = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
turn = 0
winner = 0


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
    global computer_weapon
    player_weapon = input().upper()
    if player_weapon == 'X':
        computer_weapon = 'O'
        return player_weapon
    if player_weapon == 'O':
        computer_weapon = 'X'
        return player_weapon
    else:
        print("This character is not allowed!")
        return ask_player_for_weapon()


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
    next_field = int(last_user_input) + 1
    if last_user_input == 0:
        set_computer_on_board(randint(1, 9))
    else:
        if False:
            if is_field_empty(prev_field):
                set_computer_on_board(prev_field)
            else:
                if is_field_empty(next_field):
                    set_computer_on_board(next_field)
                else:
                    print('next steps')


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
    global winner
    if turn == 1:
        player_action()
        watch_for_a_winner()
        computer_action()
        watch_for_a_winner()
        draw_board()
    if turn == 2:
        computer_action()
        draw_board()
        watch_for_a_winner()
        player_action()
        watch_for_a_winner()
        if winner != 0:
            draw_board()


def decide_who_goes_first():
    global turn
    turn = randint(1, 2)
    if turn == 2:
        print("The computer goes first!")
    for x in range(0, len(boardFields)-1):
        if winner == 1:
            print(" ")
            print("You win!")
            return False
        if winner == 2:
            print(" ")
            print("You loose!")
            return False
        else:
            play_round()


def watch_for_a_winner():
    global player_weapon
    global computer_weapon
    global winner
    if boardFields[1] == player_weapon:
        if boardFields[2] == player_weapon:
            if boardFields[3] == player_weapon:
                winner = 1
    if boardFields[4] == player_weapon:
        if boardFields[5] == player_weapon:
            if boardFields[6] == player_weapon:
                winner = 1
    if boardFields[7] == player_weapon:
        if boardFields[8] == player_weapon:
            if boardFields[9] == player_weapon:
                winner = 1
    if boardFields[1] == player_weapon:
        if boardFields[4] == player_weapon:
            if boardFields[7] == player_weapon:
                winner = 1
    if boardFields[2] == player_weapon:
        if boardFields[5] == player_weapon:
            if boardFields[8] == player_weapon:
                winner = 1
    if boardFields[3] == player_weapon:
        if boardFields[6] == player_weapon:
            if boardFields[9] == player_weapon:
                winner = 1
    if boardFields[1] == player_weapon:
        if boardFields[5] == player_weapon:
            if boardFields[9] == player_weapon:
                winner = 1
    if boardFields[3] == player_weapon:
        if boardFields[5] == player_weapon:
            if boardFields[7] == player_weapon:
                winner = 1
    if boardFields[1] == computer_weapon:
        if boardFields[2] == computer_weapon:
            if boardFields[3] == computer_weapon:
                winner = 2
    if boardFields[4] == computer_weapon:
        if boardFields[5] == computer_weapon:
            if boardFields[6] == computer_weapon:
                winner = 2
    if boardFields[7] == computer_weapon:
        if boardFields[8] == computer_weapon:
            if boardFields[9] == computer_weapon:
                winner = 2
    if boardFields[1] == computer_weapon:
        if boardFields[4] == computer_weapon:
            if boardFields[7] == computer_weapon:
                winner = 2
    if boardFields[2] == computer_weapon:
        if boardFields[5] == computer_weapon:
            if boardFields[8] == computer_weapon:
                winner = 2
    if boardFields[3] == computer_weapon:
        if boardFields[6] == computer_weapon:
            if boardFields[9] == computer_weapon:
                winner = 2
    if boardFields[1] == computer_weapon:
        if boardFields[5] == computer_weapon:
            if boardFields[9] == computer_weapon:
                winner = 2
    if boardFields[3] == computer_weapon:
        if boardFields[5] == computer_weapon:
            if boardFields[7] == computer_weapon:
                winner = 2


def main():
    if False:
        get_logo()
        get_introduction()
    ask_player_for_weapon()
    decide_who_goes_first()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
