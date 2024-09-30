import random

def pull_num(x):
    guess = 'r'
    print(f'\t\tTurn {x + 1}:')
    guess = input("\t\t")
    while not guess.isnumeric():
        print(f'\t\tPlease enter a number:')
        guess = input("\t\t")
    return int(guess)

##### Game loop
def Game_loop(minG, maxG):
    # Lokale Variables
    Num = random.randint(minG, maxG)
    guess = 0

    print('\t\tGuess the number! You have a total of 10 turns to guess! ')
    print(f'\t\tMy secret number is in the range of {minG} and {maxG}!')
    for x in range(10):
        guess = 'r'
        guess = pull_num(x)
        while not(int(guess) < maxG + 1 and int(guess) > minG):
            print(f"\t\tI'm Sorry, please enter a number between {minG} and {maxG}!")
            guess = pull_num(x)

        if guess == Num:
            print(f'\t\tYay! You won with {10-(x+1)} turns left!')
            return
        elif guess > Num:
            print(f'\t\tSorry.... Guess a bit lower than {guess}')
        elif guess < Num:
            print(f'\t\tSorry.... Guess a bit higher than {guess}')
    print(f"\t\tWhomp Whomp!! You didn't make it :(")
    return

def GTN():
    ##### Variables
    Play_again = True
    ##### Intro
    print("\n\033[34m" + r""" 
      _   _                    ____                           _             
     | \ | |_   _ _ __ ___    / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
     |  \| | | | | '_ ` _ \  | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
     | |\  | |_| | | | | | | | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
     |_| \_|\__,_|_| |_| |_|  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
        """ + "\033[0m")

    print("\t\tReady to give it a try? (" + "\033[0;32m" + "yes" + "\033[0m" + "/" + "\033[0;31m" + "no" + "\033[0m" + ")")
    print("\t\t(Saying no will exit this program)")
    if 'no' in input('\t\t'):
        Play_again = False
    ##### Games
    while Play_again:
        Game_loop(1,100)
        print("\t\tWanna play Again? (" + "\033[0;32m" + "yes" + "\033[0m" + "/" + "\033[0;31m" + "no" + "\033[0m" + ")")
        if 'no' in input('\t\t').lower:
            Play_again = False
    return

