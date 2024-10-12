from datetime import datetime
import json
import os
import time

# Global variables
# Logo to display at the top of the diary application
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

# Path to the diary JSON file
diary_location = 'Apps/DiaryPackage.json'

# Function to read and display the diary entries
def ReadJson(user):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    print(logo)  # Display the diary logo

    # Open the diary JSON file and load its content
    with open(diary_location, 'r') as input_file:
        data = json.load(input_file)

    i = 0  # Counter for diary entries
    # Loop through each diary entry and display it
    for item in data["Diary"]:
        i += 1
        print("\t\t", f'{i}.', item['Date'], item['Time'])  # Show date and time of entry
        print("\t\t", item['Note'], "\n")  # Show the actual note
    return i  # Return the total number of entries for potential removal

# Function to write a new diary entry to the JSON file
def write_json(new_data, filename=diary_location):
    # Open the JSON file and append the new entry
    with open(filename, 'r+') as input_file:
        data = json.load(input_file)
        data["Diary"].append(new_data)  # Append the new entry to the diary list
        data["Diary"].sort(key=lambda x: x["Date"])  # Sort the entries by date
        input_file.seek(0)  # Move to the beginning of the file to overwrite
        json.dump(data, input_file, indent=4)  # Write the updated diary with indentation

# Function to remove a specific diary entry
def RemoveEntry(j):
    with open(diary_location, 'r') as input_file:
        data = json.load(input_file)

    succes = False  # Track if removal was successful

    i = 0  # Counter for entries
    for item in data["Diary"]:
        i += 1
        # Check if the entry matches the one to be removed
        if i == int(j):
            data["Diary"].pop(i - 1)  # Remove the entry
            print(f"\t\t Removed entry {i} out of Diary")
            succes = True

    if not succes:
        print(f'\t\t Failed to remove entry {j} out of Diary')

    # Write the updated diary back to the JSON file
    with open(diary_location, 'w') as output_file:
        json.dump(data, output_file, indent=4)
    time.sleep(1)

# Main function to control the diary application
def DiaryReader(user):
    now = datetime.now()  # Get current date and time
    DiaryOn = True  # Diary application running flag
    Current_date = now.strftime("%d/%m/%Y")  # Current date in DD/MM/YYYY format
    Current_time = now.strftime("%H:%M")  # Current time in HH:MM format
    New_Note = ''  # Placeholder for new notes

    dt_string = now.strftime("%d/%m/%Y %H:%M")  # Full timestamp string
    while DiaryOn:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        print(logo)
        print(f"\t\t{dt_string}")

        # Main menu
        print(f"\t\tWelcome to your diary {user}!")
        print("\t\tWhat would you like to do?")
        print("\t\t1. Create a new entry")
        print("\t\t2. Read your diary")
        print("\t\t3. Remove an entry")
        print("\t\tq. Exit")
        INPUT = input("\t\tYour choice: ")

        match INPUT:
            case '1':
                # Create a new diary entry
                print("\t\tDo you want to use current date and time? (y/n)")
                if input("\t\t") == 'y':
                    # Update time & Date with current values
                    now = datetime.now()
                    Current_date = now.strftime("%d/%m/%Y")
                    Current_time = now.strftime("%H:%M")
                else:
                    # User-specified date and time
                    print("\t\tPlease input date using following format (DD/MM/YYYY)")
                    Current_date = input("\t\t")
                    print("\t\tPlease input time using following format (HH:MM)")
                    Current_time = input("\t\t")

                # Ask the user for the note
                New_Note = input("\t\tEnter your note: ")

                # Create a dictionary for the new entry
                dictionary = {
                    "Date": Current_date,
                    "Time": Current_time,
                    "Note": New_Note
                }

                write_json(dictionary)  # Write the new entry to the diary

            case '2':
                # Read the diary entries
                ReadJson(user)
                input('\t\t Press enter to exit reading mode')

            case '3':
                # Remove a specific diary entry
                max_entries = ReadJson(user)  # Display diary and get entry count
                print(f'\t\t Which entry would you like to remove? (1-{max_entries})')
                RemoveEntry(input("\t\t "))

            case 'q':
                # Exit the diary application
                DiaryOn = False

            case '_':
                # Handle invalid input
                print('Please retry your choice!')
                input()

# If the script is run directly, start the diary application for the user 'Test'
if __name__ == "__main__":
    DiaryReader("Test")
