import os  # Importing the OS module for interacting with the operating system
from Apps.Guess_the_num import GTN  # Import the 'Guess the Number' game function from the Apps package
from Apps.Diary import DiaryReader  # Import the DiaryReader function to read/write a diary
from Apps.Hangman import HangerMan  # Import the Hangman game function
from Apps.calculator import start_calculator  # Import the calculator function

### Variable initialization
loop = True  # Control variable for the main loop, will stop when set to False
error1 = False  # Variable to indicate if there was an invalid input from the user

user = os.getlogin()  # Fetch the username of the current system user

# Main application loop
while loop:
    # Clear the screen (platform-specific, 'cls' for Windows and 'clear' for Unix)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Displaying a welcome message in a decorative banner
    print("\n\033[92m" + r"""
888888b.                    888                                                                 
888  "88b                   888                                                                 
888  .88P                   888                                                                 
8888888K.  888d888 888  888 88888b.  88888b.d88b.   .d88b.  88888b.   .d88b.  888  888 .d8888b  
888  "Y88b 888P"   888  888 888 "88b 888 "888 "88b d88""88b 888 "88b d88P"88b 888  888 88K      
888    888 888     888  888 888  888 888  888  888 888  888 888  888 888  888 888  888 "Y8888b. 
888   d88P 888     Y88b 888 888  888 888  888  888 Y88..88P 888  888 Y88b 888 Y88b 888      X88 
8888888P"  888      "Y88888 888  888 888  888  888  "Y88P"  888  888  "Y88888  "Y88888  88888P' 
                                                                          888                   
                                                                     Y8b d88P                   """ + "\033[0m")

    # Displaying a welcome message with the user's name
    print(f'\t\tHi {user}! Welkom in de Bruhmongus Appstore.')
    print("\n\n")

    # Displaying the menu options to the user
    print(" \t 1. Guess the number game! Give it your best try!")
    print(" \t 2. Diary! Write your wildest stories!")
    print(" \t 3. Hangman! You better know your alfabet!")
    print(" \t 4. Calculator! When you don't know the answers!")
    print(" \t q. Exit!")  # Option to quit the application

    # Show an error message if the user previously entered invalid input
    if error1:
        print("\n \t Please enter valid input!")
    else:
        print("\n")

    # Taking user input for choosing an option
    INPUT = input("\t -> ")

    # Matching the user input to different cases to run the corresponding app
    match INPUT:
        case '1':  # Start 'Guess the Number' game
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen before running the game
            GTN()
        case '2':  # Start the Diary Reader
            os.system('cls' if os.name == 'nt' else 'clear')
            DiaryReader(user)  # Pass the username as a parameter to the diary app
        case '3':  # Start the Hangman game
            os.system('cls' if os.name == 'nt' else 'clear')
            HangerMan()
        case '4':  # Start the calculator
            os.system('cls' if os.name == 'nt' else 'clear')
            start_calculator()
        case 'q':  # Exit the application
            os.system('cls' if os.name == 'nt' else 'clear')
            loop = False  # Set the loop control variable to False to stop the loop
        case _:  # Default case for invalid input
            error1 = True  # Set error flag to display the invalid input message