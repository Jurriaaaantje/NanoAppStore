import requests
import json
import random
import os
from the_hangman_wordlist import HangmanWordlist

#logo
logo = "\n\033[94m" + r"""
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                """ + "\033[0m"

# Letterchecker
def Checkletter(word, letter):
    for i in word:
        if i == letter:
            return True
    return False

# Clear dubbles
def ClrDubbles(list):
    for i in list:
        pass

# Gameloop
def Gameloop(wordlist):
    difficulty = input("What difficulty do you want? (easy/medium/hard): ")
    word = wordlist.pull_word(difficulty)
    asked_letters = []
    good_letters = []

    print(word)

    for i in word:
        print("_", end=" ")
    print("\n")

    print("\n\n Letters asked:")
    for i in asked_letters:
        print(i, end=" ")

    x = 10
    while x > 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)

        print(f"You have {x} lives left")

        j = 0
        j_old = len(good_letters)
        for i in word:
            if i in good_letters:
                j = j + 1
                print(i, end=" ")
            else:
                print("_", end=" ")
        if j_old <= j:
            x = x - 1



        print()
        print("Letters guesssed :")
        for i in asked_letters:
            print(i, end=" ")
        print()
        print("Guess a letter")
        if j == len(word):
            return 'Win'

        Input = str()
        while len(Input) != 1:
            Input  = input()
        Input = Input.lower()
        if not Checkletter(asked_letters, Input):
            asked_letters.append(Input)
            if (Checkletter(word, Input)):
                good_letters.append(Input)
        else:
            print("Letter used sorry")
        #ClrDubbles(asked_letters)
    print(f'Sorry the word was {word}')
    return 'Lose'



def HangerMan():
    print(logo)
    wordlist = HangmanWordlist()
    PlayAgain = True
    while PlayAgain:
        if Gameloop(wordlist) == 'Win':
            print('You Win!')
        else:
            print('You Lose!')
        if 'n' in input('play again? (y/n)'):
            PlayAgain = False

if __name__ == "__main__":
    HangerMan()