#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Marcel Birkhahn"
__version__ = "0.1.0"
__license__ = "MIT"

from random import randint
import sys

player_weapon = ''
computer_weapon = ''
last_user_input = 0
boardFields = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
turn = 0
winner = 0
used_board_fields = 0


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
    last_user_input = int(input())
    if boardFields[last_user_input] == 'X':
        field_already_used()
    if boardFields[last_user_input] == 'O':
        field_already_used()
    else:
        global used_board_fields
        used_board_fields += 1
        boardFields[last_user_input] = player_weapon


def is_field_empty(field):
    if boardFields[field] != " ":
        return False
    else:
        return True


def set_computer_on_board(field_number):
    global used_board_fields
    used_board_fields += 1
    if player_weapon == "X":
        boardFields[field_number] = "O"
    else:
        boardFields[field_number] = "X"


def computer_action():
    if last_user_input == 0:
        set_computer_on_board(randint(1, 9))
        return False
    if last_user_input == 1:
        if boardFields[2] == " ":
            set_computer_on_board(2)
            return False
        if boardFields[4] == " ":
            set_computer_on_board(4)
            return False
        if boardFields[5] == " ":
            set_computer_on_board(5)
            return False
    if last_user_input == 2:
        if boardFields[1] == " ":
            set_computer_on_board(1)
            return False
        if boardFields[3] == " ":
            set_computer_on_board(3)
            return False
        if boardFields[5] == " ":
            set_computer_on_board(5)
            return False
    if last_user_input == 3:
        if boardFields[2] == " ":
            set_computer_on_board(2)
            return False
        if boardFields[5] == " ":
            set_computer_on_board(5)
            return False
        if boardFields[6] == " ":
            set_computer_on_board(6)
            return False
    if last_user_input == 4:
        if boardFields[1] == " ":
            set_computer_on_board(1)
            return False
        if boardFields[5] == " ":
            set_computer_on_board(5)
            return False
        if boardFields[7] == " ":
            set_computer_on_board(7)
            return False
    if last_user_input == 5:
        for x in range(1, len(boardFields)):
            if x != 5:
                if boardFields[x] == " ":
                    set_computer_on_board(x)
                    return False
    if last_user_input == 6:
        if boardFields[3] == " ":
            set_computer_on_board(3)
            return False
        if boardFields[5] == " ":
            set_computer_on_board(5)
            return False
        if boardFields[9] == " ":
            set_computer_on_board(9)
            return False
    if last_user_input == 7:
        if boardFields[4] == " ":
            set_computer_on_board(4)
            return False
        if boardFields[5] == " ":
            set_computer_on_board(5)
            return False
        if boardFields[9] == " ":
            set_computer_on_board(9)
            return False
    if last_user_input == 8:
        if boardFields[5] == " ":
            set_computer_on_board(5)
            return False
        if boardFields[7] == " ":
            set_computer_on_board(7)
            return False
        if boardFields[9] == " ":
            set_computer_on_board(9)
            return False
    if last_user_input == 9:
        if boardFields[5] == " ":
            set_computer_on_board(5)
            return False
        if boardFields[6] == " ":
            set_computer_on_board(6)
            return False
        if boardFields[8] == " ":
            set_computer_on_board(8)
            return False
    else:
        for x in range(1, len(boardFields)):
            if boardFields[x] == " ":
                set_computer_on_board(x)
                return False


def ask_for_another_game():
    print("Do you wanna play another game?")
    print("Type yes or no!")
    answer = input()
    if answer == 'yes':
        reset_game()
        ask_player_for_weapon()
        decide_who_goes_first()
    else:
        print(" ")
        print("Good Bye!")
        sys.exit()


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
        return True


def draw_board():
    print(" ")
    print(" ")
    print(boardFields[1] + " | " + boardFields[2] + " | " + boardFields[3])
    print("---------")
    print(boardFields[4] + " | " + boardFields[5] + " | " + boardFields[6])
    print("---------")
    print(boardFields[7] + " | " + boardFields[8] + " | " + boardFields[9])
    print(" ")
    print(" ")


def play_round():
    global winner
    if turn == 1:
        player_action()
        watch_for_a_winner()
        if winner != 0:
            draw_board()
        else:
            computer_action()
            watch_for_a_winner()
            draw_board()
    if turn == 2:
        computer_action()
        watch_for_a_winner()
        draw_board()
        if winner == 0:
            player_action()
            watch_for_a_winner()
        if winner != 0:
            draw_board()


def reset_game():
    global boardFields
    global player_weapon
    global computer_weapon
    global last_user_input
    global turn
    global winner
    global used_board_fields
    player_weapon = ''
    computer_weapon = ''
    last_user_input = 0
    boardFields = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    turn = 0
    winner = 0
    used_board_fields = 0


def play_round_or_exit():
    for x in range(0, 999):
        if winner == 1:
            print(" ")
            print("Congrats! You win!")
            ask_for_another_game()
        if winner == 2:
            print(" ")
            print("You loose! What a pity!")
            ask_for_another_game()
        else:
            if used_board_fields == 9:
                draw_board()
                print("It's a tie!")
                ask_for_another_game()
            else:
                play_round()


def decide_who_goes_first():
    global turn
    turn = randint(1, 2)
    if turn == 2:
        global used_board_fields
        used_board_fields = 1
        print("The computer goes first!")
    play_round_or_exit()


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
