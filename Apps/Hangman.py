import requests
import json
import random
import os
from the_hangman_wordlist import HangmanWordlist

# Logo for the Hangman game - displayed when the game starts
logo = "\n\033[94m" + r"""
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                """ + "\033[0m"

# List of hangman stages (sprites) to show progression of the game as the player loses lives
Hangmansprites = ['''






=========''', '''
      |
      |
      |
      |
      |
      |
=========''', '''
  +---+
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


# Function to get unique letters in a word
# This is used to ensure that the player guesses each unique letter in the word to win the game
def wordletter(word):
    onlyletter = ''
    for i in word:
        if not i in onlyletter:
            onlyletter += i
    return onlyletter


# Function to check if a letter exists in a word
# It returns True if the letter is found in the word, otherwise returns False
def Checkletter(word, letter):
    for i in word:
        if i == letter:
            return True
    return False


# Main game loop function that manages the game state, player inputs, and game progress
def Gameloop(wordlist):
    # Ask for difficulty level from the user
    difficulty = input("What difficulty do you want? (easy/medium/hard): ")

    # Pull a word based on the chosen difficulty from the wordlist
    word = wordlist.pull_word(difficulty)

    # Lists to keep track of letters the player has guessed and letters guessed correctly
    asked_letters = []
    good_letters = []
    letter_used = False

    # Print the word for debugging purposes (you may want to remove this line)
    print(word)

    # Print underscores as placeholders for the letters of the word
    for i in word:
        print("_", end=" ")
    print("\n")

    # Display the letters that have been asked (initially empty)
    print("\n\n Letters asked:")
    for i in asked_letters:
        print(i, end=" ")

    # Get only unique letters of the word
    onlyletter = wordletter(word)

    # Set the number of lives (chances)
    x = 10

    # Game loop runs as long as the player has lives left
    while x > 0:
        # Clear the console for better readability
        os.system('cls' if os.name == 'nt' else 'clear')

        # Display the logo and hangman sprite based on remaining lives
        print(logo + '\n')
        print(Hangmansprites[10 - x])
        print(f"You have {x} lives left")

        # Display the current progress of the word, showing correctly guessed letters
        for i in word:
            if i in good_letters:
                print(i, end=" ")
            else:
                print("_", end=" ")

        # Count the number of correctly guessed unique letters
        j = 0
        j_old = len(good_letters)
        for i in onlyletter:
            if i in good_letters:
                j += 1

        # If no new correct letters were guessed, reduce the player's lives by 1
        if j_old == j:
            x -= 1

        # Show the letters that have been guessed so far
        print()
        print("Letters guessed:")
        for i in asked_letters:
            print(i, end=" ")

        # Prompt the player to guess a letter
        print()
        print("Guess a letter")

        # If all unique letters have been guessed, the player wins
        if j == len(onlyletter):
            return 'Win'

        # Notify the player if they tried a letter that was already used
        if (letter_used):
            print("Letter used, sorry")

        # Take a single-letter input from the player
        Input = str()
        while len(Input) != 1:
            Input = input()
        Input = Input.lower()

        # Check if the letter has already been guessed
        if not Checkletter(asked_letters, Input):
            asked_letters.append(Input)
            letter_used = False
            # If the letter is in the word, add it to the list of good letters
            if (Checkletter(word, Input)):
                good_letters.append(Input)
                x += 1
        else:
            # If the letter was already guessed, give the player an extra life
            x += 1
            letter_used = True

    # If the player runs out of lives, display the word and return 'Lose'
    print(f'Sorry, the word was {word}')
    return 'Lose'


# Main function to run the Hangman game
def HangerMan():
    # Print the game logo at the start
    print(logo)

    # Create a wordlist object to get words for the game
    wordlist = HangmanWordlist()

    # Control variable to decide whether to play again
    PlayAgain = True

    # Main game loop: play the game, check win/lose, and ask if the player wants to play again
    while PlayAgain:
        if Gameloop(wordlist) == 'Win':
            print('You Win!')
        else:
            print('You Lose!')
        if 'n' in input('Play again? (y/n)'):
            PlayAgain = False


# Check if the script is run directly and start the game
if __name__ == "__main__":
    HangerMan()
