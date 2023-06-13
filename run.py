countries = ['Denmark', 'Malaysia', 'Egypt', 'Luxembourg', 'New Zealand']
technology = ['Playstation', 'Polaroid', 'Samsung', 'Microsoft', 'Google']
food_and_drink = ['Mozzarella', 'Baguette', 'Apple', 'Tea', 'Physalis']

def welcome_player():
    """
    Welcomes user and asks for a category to begin game
    """

    print("Welcome to Hangman\n")
    name = input("Please Enter your Name: \n").capitalize()
    print(f"Welcome {name}.\n")
    category = input("Please Select a category.\n Countries(C), Technology(T) or Food and Drink(F)\n").upper()
    
    if category != "c":
        print("Invalid entry, please select a category\n")

welcome_player()