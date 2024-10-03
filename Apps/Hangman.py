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

#hangman sprites
Hangmansprites = ['''
       
       
       
       
       
       
=========''','''
      |
      |
      |
      |
      |
      |
=========''','''
  +---+
      |
      |
      |
      |
      |
=========''','''
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


#letters in word
def wordletter(word):
    onlyletter = ''
    for i in word:
        if not i in onlyletter:
            onlyletter += i
    return onlyletter

# Letterchecker
def Checkletter(word, letter):
    for i in word:
        if i == letter:
            return True
    return False

# Gameloop
def Gameloop(wordlist):
    difficulty = input("What difficulty do you want? (easy/medium/hard): ")
    word = wordlist.pull_word(difficulty)
    asked_letters = []
    good_letters = []
    letter_used = False

    print(word)

    for i in word:
        print("_", end=" ")
    print("\n")

    print("\n\n Letters asked:")
    for i in asked_letters:
        print(i, end=" ")

    onlyletter = wordletter(word)

    x = 10
    while x > 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo + '\n')
        print(Hangmansprites[10-x])
        print(f"You have {x} lives left")


        for i in word:
            if i in good_letters:
                print(i, end=" ")
            else:
                print("_", end=" ")

        j = 0
        j_old = len(good_letters)
        for i in onlyletter:
            if i in good_letters:
                j += 1
        if j_old == j:
            x -= 1

        print()
        print("Letters guesssed :")
        for i in asked_letters:
            print(i, end=" ")
        print()
        print("Guess a letter")
        if j == len(onlyletter):
            return 'Win'
        if(letter_used): print("Letter used sorry")
        Input = str()
        while len(Input) != 1:
            Input  = input()
        Input = Input.lower()
        if not Checkletter(asked_letters, Input):
            asked_letters.append(Input)
            letter_used = False
            if (Checkletter(word, Input)):
                good_letters.append(Input)
                x += 1
        else:
            x += 1
            letter_used = True
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