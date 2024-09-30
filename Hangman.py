import requests
import os

#logo
logo = "\n\033[94m" + r"""
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                """ + "\033[0m"

# URI
URI = "https://random-word-api.herokuapp.com/"
pnq = "word?length="

# Function request word
def ReWord(size):
    responses = requests.get(URI + pnq + str(size))
    response_data = responses.json()
    return(response_data[0])

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
def Gameloop(size):
    word = ReWord(size)
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
    while (x >= 1):
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
        if j_old == j:
            x = x - 1



        print()
        print("Letters guesssed :")
        for i in asked_letters:
            print(i, end=" ")
        print()
        print("Guess a letter")
        if(j == len(word)):
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

    return 'Lose'



def HangerMan():
    print(logo)
    PlayAgain = True
    while PlayAgain == True:
        if Gameloop(10) == 'Win':
            print('You Win!')
        else:
            print('You Lose!')
        if 'n' in input('play again? (y/n)'):
            PlayAgain = False