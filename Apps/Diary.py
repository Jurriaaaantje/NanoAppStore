from datetime import datetime
import json
import os
import time

# Global variables
logo = "\n\033[95m" + r""" 
             ______     .-./`)    ____    .-------.       ____     __  
            |    _ `''. \ .-.') .'  __ `. |  _ _   \      \   \   /  / 
            | _ | ) _  \/ `-' \/   '  \  \| ( ' )  |       \  _. /  '  
            |( ''_'  ) | `-'`"`|___|  /  ||(_ o _) /        _( )_ .'   
            | . (_) `. | .---.    _.-`   || (_,_).' __  ___(_ o _)'    
            |(_    ._) ' |   | .'   _    ||  |\ \  |  ||   |(_,_)'     
            |  (_.\.' /  |   | |  _( )_  ||  | \ `'   /|   `-'  /      
            |       .'   |   | \ (_ o _) /|  |  \    /  \      /       
            '-----'`     '---'  '.(_,_).' ''-'   `'-'    `-..-'        
                        """ + "\033[0m"

#Diary Location
diary_location = 'Apps/DiaryPackage.json'

# Open and read the Diary
def ReadJson(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)


    with open(diary_location, 'r') as input_file:
        data = json.load(input_file)

    i = 0
    for item in data["Diary"]:
        i = i + 1
        # Print the data
        print("\t\t",f'{i}.',item['Date'], item['Time'])
        print("\t\t",item['Note'], "\n")
    return i

# Open and write the Diary
def write_json(new_data, filename=diary_location):
    with open(filename,'r+') as input_file:
        data = json.load(input_file)
        data["Diary"].append(new_data)
        data["Diary"].sort(key=lambda x: x["Date"])
        input_file.seek(0)
        json.dump(data, input_file, indent = 4)


def RemoveEntry(j):
    with open(diary_location, 'r') as input_file:
        data = json.load(input_file)

    succes = False

    i = 0
    for item in data["Diary"]:
        i = i + 1
        # Print the data

        if i==int(j):
            data["Diary"].pop(i-1)
            print()
            time.sleep(0.5)
            print(f"\t\t Removed entry {i} out of Diary")
            succes = True

    if succes == False:
            print(f'\t\t Failed to remove entry {j} out of Diary')

    with open(diary_location, 'w') as output_file:
        json.dump(data, output_file, indent = 4)
    time.sleep(1)
# datetime object containing current date and time

# main function
def DiaryReader(user):
    now = datetime.now()
    DiaryOn = True
    Current_date = now.strftime("%d/%m/%Y")
    Current_time = now.strftime("%H:%M")
    New_Note = ''

    dt_string = now.strftime("%d/%m/%Y %H:%M")
    while DiaryOn:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print(f"\t\t{dt_string}")

        print(f"\t\tWelcome to your diary {user}!")
        print("\t\tWhat would you like to do?")
        print("\t\t1. Create a new entry")
        print("\t\t2. Read your diary")
        print("\t\t3. Remove an entry")
        print("\t\tq. Exit")
        INPUT = input("\t\tYour choice: ")

        match INPUT:
            case '1':

                print("\t\tDo you want to use current date and time? (y/n)")
                if(input("\t\t") == 'y'):
                    # Update time & Date
                    now = datetime.now()
                    Current_date = now.strftime("%d/%m/%Y")
                    Current_time = now.strftime("%H:%M")
                else:
                    print("\t\tPlease input date using following format (DD/MM/YYYY)")
                    Current_date = input("\t\t")
                    print("\t\tPlease input time using following format (HH:MM)")
                    Current_time = input("\t\t")
                # insert note
                New_Note = input("\t\tEnter your note: ")

                dictionary = {
                    "Date": Current_date,
                    "Time": Current_time,
                    "Note": New_Note
                }

                write_json(dictionary)
            case '2':
                ReadJson(user)
                input('\t\t Press enter to exit reading mode')
            case '3':
                max = ReadJson(user)
                print(f'\t\t Which entry would you like to remove? (1-{max})')
                RemoveEntry(input("\t\t "))
            case 'q':
                DiaryOn = False
            case '_':
                print('Please retry your choice!')
                input()