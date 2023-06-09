import random
import sys
import os

from countries import country_list
from food_and_drink import fd_list
from technology import tech_list
from gallows import art, title

def clear():
    """
    Clears the screen
    """

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def welcome_player():
    """
    Welcomes the user, asks to select a category and 
    checks whether they are happy with their decision
    """

    print("Welcome to Hangman\n")
    name = input("Please Enter your Name: ").capitalize()

    while True:
        category = select_category()

        decision = input(f"{name}, you have six lives and have selected {category}. \nAre you happy with your choice? (Y/N) ").upper()

        if decision == "Y":
            print("Let's play. Good luck!\n")
            break
        elif decision == "N":
            clear()
        else:
            print("Invalid input. Please enter 'Y' or 'N'.\n")
    
    return category


def select_category():
    """
    Prompts the user to select a category from a list.
    """

    while True:
        try:
            selection = int(input("\nPlease select a category:\n1. Countries\n2. Technology\n3. Food and Drink\n\n"))
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


chosen_category = welcome_player()

def play_game():
    """
    Starts the game of Hangman
    """

    # Clear screen for better user visibility
    clear()

    random_word = ""
    print(title)
    print()
    print("HINT: some words may contain spaces")
    print()
    print(art[6])
    
    # Generates a random word based on the category selected
    if chosen_category == "Countries":
        random_word = random.choice(country_list)
    elif chosen_category == "Technology":
        random_word = random.choice(tech_list)
    else:
        random_word = random.choice(fd_list)
    
    word_length = len(random_word)

    hidden_word = "-" * word_length
    wrong_letters = ""
    guessed_letters = []
 
    while True:
        
        # Gallows and word to guess
        print(chosen_category)
        print()
        print(hidden_word)
        
        letter = input("\nPlease enter a letter: ").upper()
        if letter in random_word:
            temp = ""
            for index in range(len(random_word)):
                if letter == random_word[index]:
                    temp += letter
                    clear()
                    print(art[6])
                    print(f"\nLetters Guessed: {''.join(guessed_letters)}")
                    print(f"\nIncorrect Letters: {wrong_letters}")
                elif hidden_word[index] != "-":
                    temp += hidden_word[index]
                else:
                    temp += "-"
            hidden_word = temp
        
        else:
            wrong_letters += letter

        guessed_letters.append(letter)

        # print(f"\nLetters Guessed: {''.join(guessed_letters)}")
        # print(f"\nIncorrect Letters: {wrong_letters}")

        # Gallows and number of attempts 

        if len(wrong_letters) == 1:
            clear()
            print(f"\nLetters Guessed: {''.join(guessed_letters)}")
            print(f"\nIncorrect Letters: {wrong_letters}")
            print(art[5])
        
        if len(wrong_letters) == 2:
            clear()
            print(f"\nLetters Guessed: {''.join(guessed_letters)}")
            print(f"\nIncorrect Letters: {wrong_letters}")
            print(art[4])

        if len(wrong_letters) == 3:
            clear()
            print(f"\nLetters Guessed: {''.join(guessed_letters)}")
            print(f"\nIncorrect Letters: {wrong_letters}")
            print(art[3])

        if len(wrong_letters) == 4:
            clear()
            print(f"\nLetters Guessed: {''.join(guessed_letters)}")
            print(f"\nIncorrect Letters: {wrong_letters}")
            print(art[2])

        if len(wrong_letters) == 5:
            clear()
            print(f"\nLetters Guessed: {''.join(guessed_letters)}")
            print(f"\nIncorrect Letters: {wrong_letters}")
            print(art[1])

        if len(wrong_letters) == 6:

            # Clear screen before asking about retry
            clear()
            print(art[0])
            print("You're Dead")
            print(f"The word was {random_word}")
            retry = input("\nTry Again? Y/N ").upper()
            if retry == "Y":
                clear()
                play_game()
            else:
                clear()
                print("\nCome back when you're brave enough!!")
                exit()

        if "-" not in hidden_word:
            clear()
            print(random_word)
            print(art[7])
            play_again = input("\nCongratulations. You Survived. Play Again? Y/N ").upper()
            if play_again == "Y":
                clear()
                play_game()
            else:
                clear()
                print("Thanks for playing.")
                exit()


play_game()
