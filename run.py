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
    
    user_choice = input("Please Select a category.\n 1. Countries\n 2. Technology\n 3. Food and Drink\n")
    category = ""
    
    if user_choice == 1:
        category = "Countries"
    elif user_choice == 2:
        category = "Technology"
    elif user_choice == 3:
        category = "Food and Drink"
    else:
        print("Invalid selection. Please select a category 1 - 3.")
    
    input(f"{name}, you have selected {category}. Do you wish to continue with this selection? Y/N ").upper()
    
    

welcome_player()