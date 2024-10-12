import random


def pull_num(x):
    # Function to get the user input for guessing a number
    guess = 'r'
    print(f'\t\tTurn {x + 1}:')
    guess = input("\t\t")

    # Loop until the user enters a valid number
    while not guess.isnumeric():
        print(f'\t\tPlease enter a number:')
        guess = input("\t\t")

    return int(guess)


##### Game loop
def Game_loop(minG, maxG):
    # Local Variables
    Num = random.randint(minG, maxG)  # Random secret number between minG and maxG
    guess = 0

    # Display game instructions
    print('\t\tGuess the number! You have a total of 10 turns to guess! ')
    print(f'\t\tMy secret number is in the range of {minG} and {maxG}!')

    # Loop for 10 turns
    for x in range(10):
        guess = 'r'
        guess = pull_num(x)  # Get the user's guess

        # Ensure guess is within the allowed range
        while not (minG <= int(guess) <= maxG):
            print(f"\t\tI'm sorry, please enter a number between {minG} and {maxG}!")
            guess = pull_num(x)

        # Check if the guess is correct
        if guess == Num:
            print(f'\t\tYay! You won with {10 - (x + 1)} turns left!')
            return
        elif guess > Num:
            print(f'\t\tSorry... Guess a bit lower than {guess}')
        elif guess < Num:
            print(f'\t\tSorry... Guess a bit higher than {guess}')

    # If the user doesn't guess the number in 10 turns
    print(f"\t\tWhomp Whomp!! You didn't make it :(")
    return


# Main function to handle game setup and play-again loop
def GTN():
    ##### Variables
    play_again = True  # Flag to keep track of whether the user wants to play again

    ##### Intro
    print("\n\033[34m" + r""" 
      _   _                    ____                           _             
     | \ | |_   _ _ __ ___    / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
     |  \| | | | | '_ ` _ \  | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
     | |\  | |_| | | | | | | | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
     |_| \_|\__,_|_| |_| |_|  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
        """ + "\033[0m")

    # Ask the user if they want to start the game
    print(
        "\t\tReady to give it a try? (" + "\033[0;32m" + "yes" + "\033[0m" + "/" + "\033[0;31m" + "no" + "\033[0m" + ")")
    print("\t\t(Saying no will exit this program)")

    # If the user says 'no', exit the game
    if 'no' in input('\t\t').lower():
        play_again = False

    ##### Game loop
    while play_again:
        Game_loop(1, 100)  # Play a round of guessing with the range 1 to 100

        # Ask if the user wants to play again
        print(
            "\t\tWanna play again? (" + "\033[0;32m" + "yes" + "\033[0m" + "/" + "\033[0;31m" + "no" + "\033[0m" + ")")
        answer = input("\t\t").lower()
        if 'no' in answer:
            play_again = False

    return


# Main entry point of the program
if __name__ == "__main__":
    GTN()  # Start the game
