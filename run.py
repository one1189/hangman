countries = ['Denmark', 'Malaysia', 'Egypt', 'Luxembourg', 'New Zealand']
technology = ['Playstation', 'Polaroid', 'Samsung', 'Microsoft', 'Google']
food_and_drink = ['Mozzarella', 'Baguette', 'Apple', 'Tea', 'Physalis']

def start_game():
    """
    Welcomes user and asks for a category to begin game
    """
    
    print("Welcome to Hangman\n")
    name = input("Please Enter your Name: \n")
    print(f"Welcome {name}.\n")
    category = input("Please Select a category. Countries(c), Technology(t) or Food and Drink(f)\n")
    
    if category != "c":
        print("Invalid entry, please select a category\n")

start_game()