import random

import countries
import food_and_drink
import technology


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

    decision = input(f"{name}, you have selected {user_choice}. Do you wish to continue? Y/N ").upper()


welcome_player()
