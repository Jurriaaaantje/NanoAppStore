import os
from Apps.Guess_the_num import GTN
from Apps.Diary import DiaryReader
from Apps.Hangman import HangerMan

### Variable
loop = True
error1 = False

user = os.getlogin()

while loop:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\033[92m" + r""" 
    888b    |                                        e                                   d8                             
    |Y88b   |   /~~~8e  888-~88e  e88~-_            d8b     888-~88e  888-~88e   d88~\ _d88__  e88~-_  888-~\  e88~~8e  
    | Y88b  |       88b 888  888 d888   i          /Y88b    888  888b 888  888b C888    888   d888   i 888    d888  88b 
    |  Y88b |  e88~-888 888  888 8888   |         /  Y88b   888  8888 888  8888  Y88b   888   8888   | 888    8888__888 
    |   Y88b| C888  888 888  888 Y888   '        /____Y88b  888  888P 888  888P   888D  888   Y888   ' 888    Y888    , 
    |    Y888  "88_-888 888  888  "88_-~        /      Y88b 888-_88"  888-_88"  \_88P   "88_/  "88_-~  888     "88___/  
                                                            888       888                                                """ + "\033[0m")
    print(f'\t\tHi {user}! Welkom in de Nano Appstore.')
    print("\n\n")
    print(" \t 1. Guess the number game! Give it your best try!")
    print(" \t 2. Diary! Write your wildest stories!")
    print(" \t 3. Hangman! You better know your alfabet!")
    print(" \t q. Exit!")
    if error1:
        print("\n \t Please enter valid input!")
    else:
        print("\n")

    INPUT = input("\t -> ")
    match INPUT:
        case '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            GTN()
        case '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            DiaryReader(user)
        case '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            HangerMan()
        case 'q':
            os.system('cls' if os.name == 'nt' else 'clear')
            loop = False
        case _:
            error1 = True