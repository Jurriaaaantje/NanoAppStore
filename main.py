import os
from Apps.Guess_the_num import GTN
from Apps.Diary import DiaryReader
from Apps.Hangman import HangerMan
from Apps.calculator import start_calculator

### Variable
loop = True
error1 = False

user = os.getlogin()

while loop:
    os.system('cls' if os.name == 'nt' else 'clear')
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
    print(f'\t\tHi {user}! Welkom in de Bruhmongus Appstore.')
    print("\n\n")
    print(" \t 1. Guess the number game! Give it your best try!")
    print(" \t 2. Diary! Write your wildest stories!")
    print(" \t 3. Hangman! You better know your alfabet!")
    print(" \t 4. Calculator! When you don't know the answers!")
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
        case '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            start_calculator()
        case 'q':
            os.system('cls' if os.name == 'nt' else 'clear')
            loop = False
        case _:
            error1 = True