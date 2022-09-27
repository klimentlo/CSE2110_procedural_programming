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

def validNum(NUMBER):
    '''
    Checks if the number inputted by the user is a number between 1 and 4
    :param NUMBER: (int)
    :return:
    '''
    if NUMBER < 1 and NUMBER > 4:
        print(f"{NUMBER} isn't an option. Please select a valid number! ")
    else:

        return NUMBER
def checkInt(NUMBER):
    '''
    Verifies the number is an integer
    :param NUMBER: (str)
    :return: (int)
    '''
    if NUMBER.isnumeric():
        return int(NUMBER)
    else:
        print(f"{NUMBER} is not a valid option")
        NEW_NUM = input("Please select a scenario from 1 to 4: ")
        # It now takes the new imput (or new number) and returns it to checkInt. It then runs the new number into checkint. If the new imput isn't        an integer, itll run this program again
        return checkInt(NEW_NUM)

def isNum(NUMBER):
    '''
    Checks if the input is a number or not
    :param NUMBER: (float)
    :return: (float)
    '''
    try:
        NUMBER = float(NUMBER)
        return NUMBER
    except ValueError:
        print("""
You did not enter a number! """ )
        NEW_NUM = input("Please enter a number: ")
        return isNum(NEW_NUM)

def validNum(CHOICE):
    '''
    Verifies the number is in the number range
    :param CHOICE: (str)
    :return: (int)
    '''
    if CHOICE > 0 and CHOICE < 5:
        return int(CHOICE)
    else:
        print("That is not one of the options! ")
        NEW_CHOICE = input("Please select a scenario from 1 to 4: ")
        CHOICE = int(NEW_CHOICE) #The newly inputted answer is turned into an integer, and CHOICE
        return validNum(CHOICE)


def checkNeg(NUMBER):
    '''
    Checks if the number is a negative or not
    :param NUMBER: (float)
    :return: (float)
    '''
    if NUMBER >= 0:
        return NUMBER
    else:
        NEW_NUMBER = input("This value can't be a negative. Please enter a positive number! ")
        NEW_NUMBER = isNum(NEW_NUMBER)
        return checkNeg(NEW_NUMBER)


def checkAngle(ANGLE):
    '''
    Checks if the angle is between 1 and 89, or else the cannon ball will either go straight upwards or backwards
    :param ANGLE: (float)
    :return:(float)
    '''
    ANGLE = isNum(ANGLE)
    if ANGLE > 0 and ANGLE < 90:
        return float(ANGLE)
    else:
        NEW_ANGLE = input("Please enter an angle from 1 to 89, or else the cannonball will either go straight up or go in the opposite direction :( ")
        return checkAngle(NEW_ANGLE)


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

def direction(DISTANCE):
    if DISTANCE >= 0:
        DIRECTION = str("N")
        return DIRECTION
    else:
        DIRECTION = str("S")
        return DIRECTION
### PROCESSING
def timeCal(HEIGHT): #SCENARIO 1
    '''
    Calculating the amount of time it is in the air
    :param HEIGHT: (str)
    :return: (float)
    '''
    HEIGHT = isNum(HEIGHT)
    HEIGHT = checkNeg(HEIGHT)
    HEIGHT = float(HEIGHT)
    SOLVE =  2 * HEIGHT / 9.81 #Uses the height the user inputted and puts it into formula
    TIME = SOLVE ** 0.5 #Squares the value, so we can get the ACTUAL time
    return TIME #inputs TIME as the value of timeCal(HEIGHT)


def distanceCal(TIME, VELOCITY): #SCENARIO 1
    '''
    Calculates the distance traveled using the time value that we got from previous calculation
    :param TIME: (int) #for now at least, i want it to be a float but it wont let me
    :return: (float)
    '''
    VELOCITY = isNum(VELOCITY)
    DISTANCE = TIME * VELOCITY
    return DISTANCE


def velocityX(VELOCITY, ANGLE):
    '''
    calculate the horizontal velocity for scenario2
    :param VELOCITY: (floaT)
    :param ANGLE: (float)
    :return: (float
    '''
    RADIANSX = math.radians(ANGLE)
    RADIANSX = float(math.cos(RADIANSX))
    VELOCITY = float(VELOCITY)
    VELOCITYX = VELOCITY * RADIANSX
    return VELOCITYX


def velocityY(VELOCITY, ANGLE):
    RADIANSY = math.radians(ANGLE)
    RADIANSY = float(math.sin(RADIANSY))
    VELOCITY = float(VELOCITY)
    VELOCITYY = VELOCITY * RADIANSY
    return VELOCITYY


def timeCal2(VELOCITYY):
    TIME = VELOCITYY * 2 /9.81
    if TIME < 0:
        TIME *= -1
    return float(TIME)

def distanceCal2(VELOCITYX, TIME):
    DISTANCE = VELOCITYX * TIME
    return DISTANCE

def timeCal3(VELOCITYY):
    TIME = VELOCITYY / 9.81
    if TIME < 0:
        TIME *= -1
    return float(TIME)

def heightPeak(VELOCITYY):
    HEIGHTPEAK = (VELOCITYY ** 2) / (2 * 9.81)
    return HEIGHTPEAK

def heightTotalCal(HEIGHTPEAK, SHIPHEIGHT):
    HEIGHTPEAK = isNum(HEIGHTPEAK)
    SHIPHEIGHT = isNum(SHIPHEIGHT)
    HEIGHTTOTAL = HEIGHTPEAK + SHIPHEIGHT
    return HEIGHTTOTAL

def timeFallCal(HEIGHTTOT):
    TOTTIME = ((HEIGHTTOT)/9.81) ** 0.5
    return TOTTIME

def distanceCAl(TIMEFALL, TIME, VELOCITYX):
    DISTANCE = (TIMEFALL + TIME) * VELOCITYX
    return DISTANCE
### OUTPUTS
def intro():
    '''
    tells the user what the program does and provides an introduction
    :return: (none)
    '''
    print('''
Welcome to the cannonball trajectory calculator! It can be used to calculate something depending on the scenario you select! 
For the sake of this program, North is going to be considered  positive, and South is going to be considered negative.
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
            HEIGHT = input("""
How high above the water is the cannon located (in meters)? 
""" )
            HEIGHT = timeCal(HEIGHT) #calculates the time it is in the air using the height
            VELOCITY = input("""How fast is the cannonball flying at when it leaves the cannon (in m/s)?" 
""")
            TIME = HEIGHT #Puts the time into the TIME value to avoid confusion (even though its already confusing LOL)
            DISTANCE = distanceCal(TIME, VELOCITY) # for the distanceCal parameters, we're putting the the time value as the first parameter, and then the requested value as the second parameter
            TIME = round(TIME,2)  # rounds to 2 decimal places, we round it after all the calculations so it can't affect the distance calculation
            DISTANCE = round(DISTANCE, 2)  # rounds the distance to two decimal places
            DIRECTION = direction(DISTANCE) #checks if the number is a positive or negative. If it is positive, it will display north. If it is negative, it will display south
            print(f"The cannonball will be in the air for a total of {TIME} seconds, with a total distance of {DISTANCE} meters {[DIRECTION]}. ") #after calculation, displays the answer to the user
        if SCENARIO == 2: #if the user requested for scenario 2, the angled cannon towards parallel ship
            VELOCITY2 = input("What is the velocity of the cannonball as it leaves the cannon (m/s)?" )
            VELOCITY2= isNum(VELOCITY2)
            ANGLE = input("What is the angle of the cannon to the ground? ")
            ANGLE = checkAngle(ANGLE)
            VELOCITYX = velocityX(VELOCITY2, ANGLE)
            VELOCITYY = velocityY(VELOCITY2, ANGLE)
            TIME = timeCal2(VELOCITYY)
            DISTANCE2 = distanceCal2(VELOCITYX, TIME)
            DIRECTION = direction(DISTANCE2)
            DISTANCE2 = round(DISTANCE2, 2)  # rounds the distance to two decimal places
            VELOCITYX = round(VELOCITYX, 2)  # rounds the distance to two decimal places
            VELOCITYY = round(VELOCITYY, 2)  # rounds the distance to two decimal places
            TIME = round(TIME, 2)  # rounds the distance to two decimal places
            print(f""" 
The cannonball is moving at {VELOCITYX}m/s horizontally and {VELOCITYY}m/s vertically, being in the air for a total of {TIME} seconds. 
The total distance the cannonball traveled was {DISTANCE2} meters {[DIRECTION]}. """)
        if SCENARIO == 3:
            VELOCITY3 = input("What is the velocity of the cannonball as it leaves the cannon (m/s)?" )
            VELOCITY3 = isNum(VELOCITY3)
            ANGLE = input("What is the angle of the cannon to the ground? ")
            ANGLE = checkAngle(ANGLE)
            SHIPHEIGHT = input("How much lower is the enemy ship compared to yours? ")
            VELOCITYX = velocityX(VELOCITY3, ANGLE)
            VELOCITYY = velocityY(VELOCITY3, ANGLE)
            TIME = timeCal3(VELOCITYY)
            HEIGHT = heightPeak(VELOCITYY)
            HEIGHTTOTAL = heightTotalCal(HEIGHT, SHIPHEIGHT)
            TIMEFALL = timeFallCal(HEIGHTTOTAL)
            DISTANCE = distanceCAl(TIMEFALL, TIME, VELOCITYX)
            print(DISTANCE)

        if not askContinue():
            exit()

main()