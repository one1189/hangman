import random

from countries import country_list
from food_and_drink import fd_list
from technology import tech_list
from gallows import art


def welcome_player():
    """
    Welcomes user and asks for a category to begin game
    """

    print("Welcome to Hangman\n")
    name = input("Please Enter your Name: ").capitalize()
    print(f"Welcome {name}.\n")

    while True:
        try:
            user_choice = int(input(
                "Please Select a category.\n 1. Countries\n 2. Technology\n 3. Food and Drink\n"))
            if user_choice >= 1 and user_choice <= 3:
                print("Valid Selection")
                break
            else:
                print("Invalid Entry. Please select a category.\n")
        except ValueError:
            print("Please select a number between 1 and 3.\n")

    selection = ""

    if user_choice == 1:
        selection = "Countries"
    elif user_choice == 2:
        selection = "Technology"
    else:
        selection = "Food and Drink"

    while True:
        try:
            decision = str(input(
                f"{name}, you have selected {selection}. Do you wish to continue? Y/N ")).upper()
            if decision == "Y":
                print("Let's Play. Good luck\n")
                break
            elif decision == "N":
                return user_choice
            else:
                print("You must select either y or n")
        except ValueError:
            print("Invalid character. Please try again")


def hangman_game():
    """
    Begins the game of hangman
    """


welcome_player()
