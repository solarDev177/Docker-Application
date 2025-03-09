# Tyson E.
# 3/4/2025
# Docker Application
# Unit converter

from colorama import Fore, Style
import os
import sys
"""
LOCKFILE = "lockfile.txt"

def open_new_console():

    # Check if lockfile exists (indicating another instance is running) or clean any stray lock files:

    cleanup_lockfile()
    if os.path.exists(LOCKFILE):
        print("A console is already open. Exiting to prevent infinite windows.")
        return

    # Create the lockfile to prevent recursion:

    with open(LOCKFILE, "w") as f:
        f.write("locked")

    # Open a new console:
    if os.getenv("DOCKER") == "true":
    print("Running in Docker. Skipping console opening.")
    input("Press Enter to exit...")  # Keeps the terminal open

        
    if sys.platform == "win32":
        os.system(f"start cmd /k python {sys.argv[0]} no_console")
    elif sys.platform == "darwin":
        os.system(f"osascript -e 'tell application \"Terminal\" to do script \"python3 {sys.argv[0]} no_console\"'")
    elif sys.platform == "linux":
        os.system(f"gnome-terminal -- python3 {sys.argv[0]} no_console")

def cleanup_lockfile():

    # Remove the lockfile when the script closes:

    if os.path.exists(LOCKFILE):
        os.remove(LOCKFILE)
"""
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def hours_to_minutes(hours, minutes, seconds):
    return hours * 60 + minutes + seconds_to_minutes(seconds)

def seconds_to_minutes(seconds):
    return seconds / 60

def minutes_to_hours(minutes, seconds, hours):
    return minutes + seconds_to_minutes(seconds) / 60 + hours

def kmph_to_mph(kmph):
    return kmph * 0.621371

def mph_to_kmph(mph):
    return mph / 0.621371

def main():

    if len(sys.argv) == 1:
        print("Opening a new console window...")
        open_new_console()
        return

        # If the new console is already open, the code proceeds here
    print("Welcome to the Unit Converter!")
    hub = str(input("Type any of these letters to select a function:\n" +
                    "'1' -->| Meters to Feet\n" +
                    "'2' -->| Feet to Meters\n" +
                    "'3' -->| Kilograms to Pounds \n" +
                    "'4' -->| Pounds to Kilograms\n" +
                    "'5' -->| Celsius to Fahrenheit\n" +
                    "'6' -->| Fahrenheit to Celsius\n" +
                    "'7' -->| Hours to Minutes\n" +
                    "'8' -->| Minutes to Hours\n" +
                    "'9' -->| Kmph to Mph\n" +
                    "'10'-->| Mph to Kmph\n"
                    "'Quit' or 'quit': Quit the program\n"
                    "Enter: "))
    while hub != "quit" or hub != "Quit":

        if hub == "1":
            nav = "go"
            while nav == "go" or nav == "Go":

                val = input("Enter meters to convert to feet: ")
                if is_float(val):
                    print(f"Conversion to feet is: {meters_to_feet(val)} feet.")
                else:
                    print(Fore.RED + 'Error: Invalid input. Value is not a decimal '
                                     'or integer. Restart the function.\n' + "----------" + Style.RESET_ALL)
                nav = str(input("Restart? Type 'go' or 'Go' to run again. Type anything else to continue: "))

            hub = str(input("Type any of these letters to select a function:\n" +
                            "'1' -->| Meters to Feet\n" +
                            "'2' -->| Feet to Meters\n" +
                            "'3' -->| Kilograms to Pounds \n" +
                            "'4' -->| Pounds to Kilograms\n" +
                            "'5' -->| Celsius to Fahrenheit\n" +
                            "'6' -->| Fahrenheit to Celsius\n" +
                            "'7' -->| Hours to Minutes\n" +
                            "'8' -->| Minutes to Hours\n" +
                            "'9' -->| Kmph to Mph\n" +
                            "'10'-->| Mph to Kmph\n"
                            "'Quit' or 'quit': Quit the program\n"
                            "Enter: "))

        elif hub == '2':
            nav = "go"
            while nav == "go" or nav == "Go":

                val2 = input("Enter feet to convert to meters: ")
                if is_float(val2):
                    print(f"Conversion to meters is: {feet_to_meters(float(val2))} meters.")
                else:
                    print(Fore.RED + 'Error: Invalid input. Value is not a decimal '
                                     'or integer. Restart the function.\n' + "----------" + Style.RESET_ALL)
                nav = str(input("Restart? Type 'go' or 'Go' to run again. Type anything else to continue: "))

            hub = str(input("Type any of these letters to select a function:\n" +
                            "'1' -->| Meters to Feet\n" +
                            "'2' -->| Feet to Meters\n" +
                            "'3' -->| Kilograms to Pounds \n" +
                            "'4' -->| Pounds to Kilograms\n" +
                            "'5' -->| Celsius to Fahrenheit\n" +
                            "'6' -->| Fahrenheit to Celsius\n" +
                            "'7' -->| Hours to Minutes\n" +
                            "'8' -->| Minutes to Hours\n" +
                            "'9' -->| Kmph to Mph\n" +
                            "'10'-->| Mph to Kmph\n"
                            "'Quit' or 'quit': Quit the program\n"
                            "Enter: "))

        elif hub == '3':
            nav = "go"
            while nav == "go" or nav == "Go":

                val3 = input("Enter kilograms to convert to pounds: ")
                if is_float(val3):
                    print(f"Conversion to pounds is: {kg_to_pounds(float(val3))} pounds.")
                else:
                    print(Fore.RED + 'Error: Invalid input. Value is not a decimal '
                                     'or integer. Restart the function.\n' + "----------" + Style.RESET_ALL)
                nav = str(input("Restart? Type 'go' or 'Go' to run again. Type anything else to continue: "))

            hub = str(input("Type any of these letters to select a function:\n" +
                            "'1' -->| Meters to Feet\n" +
                            "'2' -->| Feet to Meters\n" +
                            "'3' -->| Kilograms to Pounds \n" +
                            "'4' -->| Pounds to Kilograms\n" +
                            "'5' -->| Celsius to Fahrenheit\n" +
                            "'6' -->| Fahrenheit to Celsius\n" +
                            "'7' -->| Hours to Minutes\n" +
                            "'8' -->| Minutes to Hours\n" +
                            "'9' -->| Kmph to Mph\n" +
                            "'10'-->| Mph to Kmph\n"
                            "'Quit' or 'quit': Quit the program\n"
                            "Enter: "))

        elif hub == '4':
            nav = "go"
            while nav == "go" or nav == "Go":

                val4 = input("Enter pounds to convert to kilograms: ")
                if is_float(val4):
                    print(f"Conversion to kilograms is: {pounds_to_kg(float(val4))} kilograms.")
                else:
                    print(Fore.RED + 'Error: Invalid input. Value is not a decimal '
                                     'or integer. Restart the function.\n' + "----------" + Style.RESET_ALL)
                nav = str(input("Restart? Type 'go' or 'Go' to run again. Type anything else to continue: "))

            hub = str(input("Type any of these letters to select a function:\n" +
                            "'1' -->| Meters to Feet\n" +
                            "'2' -->| Feet to Meters\n" +
                            "'3' -->| Kilograms to Pounds \n" +
                            "'4' -->| Pounds to Kilograms\n" +
                            "'5' -->| Celsius to Fahrenheit\n" +
                            "'6' -->| Fahrenheit to Celsius\n" +
                            "'7' -->| Hours to Minutes\n" +
                            "'8' -->| Minutes to Hours\n" +
                            "'9' -->| Kmph to Mph\n" +
                            "'10'-->| Mph to Kmph\n"
                            "'Quit' or 'quit': Quit the program\n"
                            "Enter: "))

        elif hub == '5':
            nav = "go"
            while nav == "go" or nav == "Go":

                val5 = input("Enter celsius to convert to fahrenheit: ")
                if is_float(val5):
                    print(f"Conversion to fahrenheit is: {celsius_to_fahrenheit(float(val5))} degrees fahrenheit.")
                else:
                    print(Fore.RED + 'Error: Invalid input. Value is not a decimal '
                                     'or integer. Restart the function.\n' + "----------" + Style.RESET_ALL)
                nav = str(input("Restart? Type 'go' or 'Go' to run again. Type anything else to continue: "))

            hub = str(input("Type any of these letters to select a function:\n" +
                            "'1' -->| Meters to Feet\n" +
                            "'2' -->| Feet to Meters\n" +
                            "'3' -->| Kilograms to Pounds \n" +
                            "'4' -->| Pounds to Kilograms\n" +
                            "'5' -->| Celsius to Fahrenheit\n" +
                            "'6' -->| Fahrenheit to Celsius\n" +
                            "'7' -->| Hours to Minutes\n" +
                            "'8' -->| Minutes to Hours\n" +
                            "'9' -->| Kmph to Mph\n" +
                            "'10'-->| Mph to Kmph\n"
                            "'Quit' or 'quit': Quit the program\n"
                            "Enter: "))

        elif hub == '6':
            nav = "go"
            while nav == "go" or nav == "Go":

                val6 = input("Enter fahrenheit to convert to celsius: ")
                if is_float(val6):
                    print(f"Conversion to celsius is: {fahrenheit_to_celsius(float(val6))} degrees celsius.")
                else:
                    print(Fore.RED + 'Error: Invalid input. Value is not a decimal '
                                     'or integer. Restart the function.\n' + "----------" + Style.RESET_ALL)
                nav = str(input("Restart? Type 'go' or 'Go' to run again. Type anything else to continue: "))

            hub = str(input("Type any of these letters to select a function:\n" +
                            "'1' -->| Meters to Feet\n" +
                            "'2' -->| Feet to Meters\n" +
                            "'3' -->| Kilograms to Pounds \n" +
                            "'4' -->| Pounds to Kilograms\n" +
                            "'5' -->| Celsius to Fahrenheit\n" +
                            "'6' -->| Fahrenheit to Celsius\n" +
                            "'7' -->| Hours to Minutes\n" +
                            "'8' -->| Minutes to Hours\n" +
                            "'9' -->| Kmph to Mph\n" +
                            "'10'-->| Mph to Kmph\n"
                            "'Quit' or 'quit': Quit the program\n"
                            "Enter: "))

        elif hub == '7':
            nav = "go"
            while nav == "go" or nav == "Go":

                val7 = input("Enter hours to convert to minutes: ")
                val8 = input("Enter any remaining minutes to add: ")
                val9 = input("Enter any remaining seconds to add: ")
                if is_float(val7) and is_float(val8) and is_float(val9):
                    print(f"Conversion to minutes is: {hours_to_minutes(float(val7), float(val8), float(val9))} minutes.")
                else:
                    print(Fore.RED + 'Error: Invalid input. Value(s) are not decimals '
                                     'or integers. Restart the function.\n' + "----------" + Style.RESET_ALL)
                nav = str(input("Restart? Type 'go' or 'Go' to run again. Type anything else to continue: "))

            hub = str(input("Type any of these letters to select a function:\n" +
                            "'1' -->| Meters to Feet\n" +
                            "'2' -->| Feet to Meters\n" +
                            "'3' -->| Kilograms to Pounds \n" +
                            "'4' -->| Pounds to Kilograms\n" +
                            "'5' -->| Celsius to Fahrenheit\n" +
                            "'6' -->| Fahrenheit to Celsius\n" +
                            "'7' -->| Hours to Minutes\n" +
                            "'8' -->| Minutes to Hours\n" +
                            "'9' -->| Kmph to Mph\n" +
                            "'10'-->| Mph to Kmph\n"
                            "'Quit' or 'quit': Quit the program\n"
                            "Enter: "))

        elif hub == '8':
            nav = "go"
            while nav == "go" or nav == "Go":

                val10 = input("Enter minutes to convert to hours: ")
                val11= input("Enter any remaining seconds to add to minutes: ")
                val12 = input("Enter any remaining hours to add: ")
                if is_float(val10) and is_float(val11) and is_float(val12):
                    print(f"Conversion to hours is: {minutes_to_hours(float(val10), float(val11), float(val12))} hours.")
                else:
                    print(Fore.RED + 'Error: Invalid input. Value(s) are not decimals '
                                     'or integers. Restart the function.\n' + "----------" + Style.RESET_ALL)
                nav = str(input("Restart? Type 'go' or 'Go' to run again. Type anything else to continue: "))

            hub = str(input("Type any of these letters to select a function:\n" +
                            "'1' -->| Meters to Feet\n" +
                            "'2' -->| Feet to Meters\n" +
                            "'3' -->| Kilograms to Pounds \n" +
                            "'4' -->| Pounds to Kilograms\n" +
                            "'5' -->| Celsius to Fahrenheit\n" +
                            "'6' -->| Fahrenheit to Celsius\n" +
                            "'7' -->| Hours to Minutes\n" +
                            "'8' -->| Minutes to Hours\n" +
                            "'9' -->| Kmph to Mph\n" +
                            "'10'-->| Mph to Kmph\n"
                            "'Quit' or 'quit': Quit the program\n"
                            "Enter: "))

        elif hub == '9':
            nav = "go"
            while nav == "go" or nav == "Go":

                val13 = input("Enter kilometers/hour to convert to miles/hour: ")
                if is_float(val13):
                    print(f"Conversion to mph is: {kmph_to_mph(float(val13))} mph.")
                else:
                    print(Fore.RED + 'Error: Invalid input. Value is not a decimal '
                                     'or integer. Restart the function.\n' + "----------" + Style.RESET_ALL)
                nav = str(input("Restart? Type 'go' or 'Go' to run again. Type anything else to continue: "))

            hub = str(input("Type any of these letters to select a function:\n" +
                            "'1' -->| Meters to Feet\n" +
                            "'2' -->| Feet to Meters\n" +
                            "'3' -->| Kilograms to Pounds \n" +
                            "'4' -->| Pounds to Kilograms\n" +
                            "'5' -->| Celsius to Fahrenheit\n" +
                            "'6' -->| Fahrenheit to Celsius\n" +
                            "'7' -->| Hours to Minutes\n" +
                            "'8' -->| Minutes to Hours\n" +
                            "'9' -->| Kmph to Mph\n" +
                            "'10'-->| Mph to Kmph\n"
                            "'Quit' or 'quit': Quit the program\n"
                            "Enter: "))

        elif hub == '10':
            nav = "go"
            while nav == "go" or nav == "Go":

                val14 = input("Enter miles/hour to convert to kilometers/hour: ")
                if is_float(val14):
                    print(f"Conversion to kmph is: {mph_to_kmph(float(val14))} kmph.")
                else:
                    print(Fore.RED + 'Error: Invalid input. Value is not a decimal '
                                     'or integer. Restart the function.\n' + "----------" + Style.RESET_ALL)
                nav = str(input("Restart? Type 'go' or 'Go' to run again. Type anything else to continue: "))

            hub = str(input("Type any of these letters to select a function:\n" +
                            "'1' -->| Meters to Feet\n" +
                            "'2' -->| Feet to Meters\n" +
                            "'3' -->| Kilograms to Pounds \n" +
                            "'4' -->| Pounds to Kilograms\n" +
                            "'5' -->| Celsius to Fahrenheit\n" +
                            "'6' -->| Fahrenheit to Celsius\n" +
                            "'7' -->| Hours to Minutes\n" +
                            "'8' -->| Minutes to Hours\n" +
                            "'9' -->| Kmph to Mph\n" +
                            "'10'-->| Mph to Kmph\n"
                            "'Quit' or 'quit': Quit the program\n"
                            "Enter: "))

        elif hub == "Quit" or hub == 'quit':
            break

        else:

            print(Fore.RED + 'Error : Invalid input. Try again.\n' + "----------" + Style.RESET_ALL)

            hub = str(input("Type any of these letters to select a function:\n" +
                            "'1' -->| Meters to Feet\n" +
                            "'2' -->| Feet to Meters\n" +
                            "'3' -->| Kilograms to Pounds \n" +
                            "'4' -->| Pounds to Kilograms\n" +
                            "'5' -->| Celsius to Fahrenheit\n" +
                            "'6' -->| Fahrenheit to Celsius\n" +
                            "'7' -->| Hours to Minutes\n" +
                            "'8' -->| Minutes to Hours\n" +
                            "'9' -->| Kmph to Mph\n" +
                            "'10'-->| Mph to Kmph\n"
                            "'Quit' or 'quit': Quit the program\n"
                            "Enter: "))

    # Clean up the lockfile on exit
    cleanup_lockfile()

    print("Type 'exit' if on windows32 or linux consoles to close the console, and if on darwin, type "
          "osascript -e 'tell application \"Terminal\" to close (front window)'")

    if len(sys.argv) > 1 and sys.argv[1] == "no_console":
        if sys.platform == "win32":
            os.system("exit")
        elif sys.platform == "darwin":
            os.system("osascript -e 'tell application \"Terminal\" to close (front window)'")
        elif sys.platform == "linux":
            os.system("exit")


if __name__ == '__main__':
    main()
