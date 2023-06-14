import random

from countries import country_list
from food_and_drink import fd_list
from technology import tech_list
from gallows import art



def welcome_player():
    """
    Welcomes the user, asks to select a category and 
    checks whether they are happy with their decision
    """

    global name

    print("Welcome to Hangman\n")
    name = input("Please Enter your Name: ").capitalize()

    while True:
        category = select_category()

        decision = input(f"{name}, you have selected {category}. Are you happy with your choice? (Y/N) ").upper()

        if decision == "Y":
            print("Let's play. Good luck!\n")
            break
        elif decision == "N":
            print("Please select another category.\n")
        else:
            print("Invalid input. Please enter 'Y' or 'N'.\n")
    
    print (f"Welcome {name}. You will only have six attempts to correctly guess the word.\n")


def select_category():
    """
    Prompts the user to select a category from a list.
    """

    while True:
        try:
            selection = int(input("Please select a category:\n1. Countries\n2. Technology\n3. Food and Drink\n"))
            if 1 <= selection <= 3:
                break
            else:
                print("Invalid entry. Please select a valid category.\n")
        except ValueError:
            print("Please enter a number between 1 and 3.\n")

    if selection == 1:
        category = "Countries"
    elif selection == 2:
        category = "Technology"
    else:
        category = "Food and Drink"

    return category


welcome_player()