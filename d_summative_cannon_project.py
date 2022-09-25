# d_summative_cannon_project.py
'''
title: cannon operator
author: kliment lo
date-created: 2022-09-21
'''

import math
# --- FUNCTIONS --- #

### INPUTS
def menu():
    '''
    User selects which Scenario they want to calculate
    :return:
    '''
    print('''
  Scenario 1:                 |        Scenario 2:                     |         Scenario 3:
    ____                      |            ___                         |            ____
    |   \\                     |           /   \\                        |           /    \\
    |    \\                    |          /     \\                       |          |      \\
    |     \\                   |         /       \\                      |          |       \\
    Horizontal to the water   |         Parabolic to a level boat      |          Parabolic to a smaller boat far away
    ''')

    CHOICE = input("Select a scenario you'd like to calculate: ")
    CHOICE = checkInt(CHOICE)  # sends the value to the checkInt function, to see if the input is an integer (1, 2, 3, etc.)
    CHOICE = validNum(CHOICE)
    return CHOICE

def checkInt(NUMBER):
    '''
    Verifies the number is an integer
    :param NUMBER: (str)
    :return: (int)
    '''
    if NUMBER.isnumeric():
        return int(NUMBER)
    else:
        print("That is not a number! ")
        NEW_NUM = input("Please enter a valid number: ")
        # It now takes the new imput (or new number) and returns it to checkInt. It then runs the new number into checkint. If the new imput isn't        an integer, itll run this program again
        return checkInt(NEW_NUM)

def checkFloat(NUMBER):
    '''
    Verify the number is a float
    :param NUMBER: (str)
    :return: (float)
    '''
    try:
        NUMBER = float(NUMBER)
        return NUMBER
    except ValueError:
        print(" You did not enter a number!" )
        NEW_NUM = input("Please enter a number: ")
        return checkFloat(NEW_NUM)


def validNum(CHOICE):
    '''
    Verifies the number is in the number range
    :param CHOICE: (str)
    :return: (int)
    '''
    if CHOICE > 0 and CHOICE < 5:
        return int(CHOICE)
    else:
        print("That's not one of the options! ")
        NEW_CHOICE = input("Please enter a number from 1 to 4: ")
        CHOICE = int(NEW_CHOICE) #The newly inputted answer is turned into an integer, and CHOICE
        return validNum(CHOICE)

def askContinue():
    '''
    Asks user whether to continue the program.
    :return: (bool) # True/false
    '''
    AGAIN = input("Calculate Again? (y/n) ")
    if AGAIN == "y" or AGAIN == "Y" or AGAIN == "":
        return True
    elif AGAIN == "n" or AGAIN == "N":
        return False
    else:
        print("Please choose y or n ")
        return askContinue()

### PROCESSING
def timeCal(HEIGHT): #SCENARIO 1
    '''
    Calculating the amount of time it is in the air
    :param HEIGHT: (str)
    :return: (float)
    '''
    SOLVE =  2 * HEIGHT / 9.81 #Uses the height the user inputted and puts it into formula
    SOLVE = int(SOLVE) #makes the value we got into an integer, cause in order to square it, it has to be an integer for some reason
    TIME = math.isqrt(SOLVE) #Squares the value, so we can get the ACTUAL time
    return TIME #inputs TIME as the value of timeCal(HEIGHT)

def distanceCal(TIME, VELOCITY): #SCENARIO 1
    '''
    Calculates the distance traveled using the time value that we got from previous calculation
    :param TIME: (int) #for now at least, i want it to be a float but it wont let me 
    :return: (float)
    '''
    DISTANCE = TIME * VELOCITY
    return DISTANCE

### OUTPUTS
def intro():
    '''
    tells the user what the program does and provides an introduction
    :return: (none)
    '''
    print('''
Welcome to the cannonball trajectory calculator! It can be used to calculate something depending on the scenario you select!
    ''')


# --- MAIN PROGRAM --- #
def main():
    '''
    the main program where everything runs
    :return:
    '''
    intro()
    while True:
        SCENARIO = menu()
        if SCENARIO == 1: #if the user requested for scenario 1, the horizontal cannon
            HEIGHT = float(input("""
How high above the water is the cannon located (in meters)? 
""" ))
            HEIGHT = timeCal(HEIGHT) #calculates the time it is in the air using the height
            VELOCITY = float(input("""How fast is the cannonball flying at when it leaves the cannon (in m/s)? 
"""))
            TIME = HEIGHT #Puts the time into the TIME value to avoid confusion (even though its already confusing LOL)
            DISTANCE = distanceCal(TIME, VELOCITY)
            print(f"The cannonball will be in the air for {TIME} seconds, having a total displacement of {DISTANCE}. ")
        if not askContinue():
            exit()

main()