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
    
-------------------------------------------------------------------------------------------------------------------------------------------
|                                  |                                  |                                  |                                |
|      Scenario 1:                 |         Scenario 2:              |         Scenario 3:              |         Scenario 4:            |
|        ____                      |             ___                  |            ____                  |            ____                |
|        |   \\                     |            /   \\                 |           /    \\                 |           /    \\               |   
|        |    \\                    |           /     \\                |          |      \\                |          /      \\              |   
|        |     \\                   |          /       \\               |                  \\               |         /                      |
|       Horizontal to the water    |     Parabolic to a level boat    |    Parabolic to a smaller boat   |   Parabolic to a larger boat   |
|                                  |                                  |    boat far away                 |   far away                     |
-------------------------------------------------------------------------------------------------------------------------------------------
    ''')

    CHOICE = input("Select a scenario you'd like to calculate: ")
    CHOICE = checkChoice(CHOICE)  # sends the value to the checkChoice function, to see if the input is an integer (1, 2, 3, etc.)
    CHOICE = validChoice(CHOICE)
    return CHOICE
def checkChoice(NUMBER):
    '''
    Verifies the CHOICE is an integer
    :param NUMBER: (str)
    :return: (int)
    '''
    if NUMBER.isnumeric():
        return int(NUMBER)
    else:
        print(f"{NUMBER} is not a valid option")
        NEW_NUM = input("Please select a scenario from 1 to 4: ")
        # It now takes the new imput (or new number) and returns it to checkChoice. It then runs the new number into checkChoice. If the new input isn't an integer, itll run this program again
        return checkChoice(NEW_NUM)
def validChoice(CHOICE):
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
        return validChoice(CHOICE)
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
        print("You did not enter a number! " )
        NEW_NUM = input("Please enter a number: ")
        return isNum(NEW_NUM)

def checkNeg(NUMBER):
    '''
    Checks if the number is a negative or not
    :param NUMBER: (float)
    :return: (float)
    '''
    NUMBER = float(NUMBER)
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
        NEW_ANGLE = input("Please enter an angle from 1 to 89, or else the cannonball will either go straight up or go in the opposite direction. ")
        return checkAngle(NEW_ANGLE)


def askContinue():
    '''
    Asks user whether to continue the program.
    :return: (bool) # True/false
    '''
    AGAIN = input("""
Calculate Again (y/n)? """)
    if AGAIN == "y" or AGAIN == "Y" or AGAIN == "":
        return True
    elif AGAIN == "n" or AGAIN == "N":
        return False
    else:
        print("Please select (y/n). ")
        return askContinue()

def direction(DISTANCE):
    '''
    Determines the direction the cannonball
    :param DISTANCE: (float)
    :return: (str)
    '''
    try:
        if DISTANCE >= 0: #if number is positive
            DIRECTION = str("N") #direction is north
            return DIRECTION
        else: #if number is negative
            DIRECTION = str("S") #direction is south
            return DIRECTION
    except TypeError: #this is specifically for scenario 4
        print("Your cannonball wasn't shot fast enough to reach the ship! Please retry with New numbers")
        if not askContinue():
            exit()
        return ""

### --- PROCESSING ---###
## SCENARIO 1
def timeCal(HEIGHT, GRAVITY): #SCENARIO 1
    '''
    Calculating the amount of time it is in the air
    :param HEIGHT: (str)
    :return: (float)
    '''
    SOLVE =  2 * HEIGHT / GRAVITY #Uses the height the user inputted and puts it into formula
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

## SCENARIO 2&3&4
def velocityX(VELOCITY, ANGLE):
    '''
    calculate the horizontal velocity for scenario
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
    '''
    calculates vertical velocity
    :param VELOCITY: (float)
    :param ANGLE: (float)
    :return: (float)
    '''
    RADIANSY = math.radians(ANGLE)
    RADIANSY = float(math.sin(RADIANSY))
    VELOCITY = float(VELOCITY)
    VELOCITYY = VELOCITY * RADIANSY
    return VELOCITYY


def timeCal2(VELOCITYY, GRAVITY):
    '''
    calculates total time that it's in the air
    :param VELOCITYY: (float)
    :param GRAVITY: (float)
    :return: (float)
    '''
    TIME = VELOCITYY * 2 /GRAVITY
    if TIME < 0:
        TIME *= -1
    return float(TIME)

def distanceCal2(VELOCITYX, TIME):
    '''
    calculates total distance
    :param VELOCITYX: (float)
    :param TIME: (float)
    :return: (float)
    '''
    DISTANCE = VELOCITYX * TIME
    return DISTANCE

##SCENARIO 3&4
def timePeak(VELOCITYY, GRAVITY):
    '''
    calculates the time it takes for the ball to hit its max height
    :param VELOCITYY: (float)
    :param GRAVITY: (float)
    :return: (float)
    '''
    TIMEPEAK = VELOCITYY/GRAVITY
    return TIMEPEAK

def maxHeight(VELOCITYY, GRAVITY):
    '''
    calculates height peak of cannonball
    :param VELOCITYY: (float)
    :param GRAVITY: (float)
    :return: (float)
    '''
    MAXHEIGHT = (VELOCITYY ** 2) / (2 * GRAVITY)
    return MAXHEIGHT

def totHeight (MAXHEIGHT, SHIPHEIGHT):
    '''
    calculates the distance the ball will fall
    :param MAXHEIGHT: (float)
    :param SHIPHEIGHT: (float)
    :return: (float)
    '''
    MAXHEIGHT = isNum(MAXHEIGHT)
    SHIPHEIGHT = isNum(SHIPHEIGHT)
    HEIGHTTOTAL = MAXHEIGHT + SHIPHEIGHT
    return HEIGHTTOTAL

def fallTime(TOTHEIGHT, GRAVITY):
    '''
    calculates the time it takes for the ball to fall from that distance
    :param TOTHEIGHT: (float)
    :param GRAVITY: (float)
    :return: (float)
    '''
    TIMEFALL = ((TOTHEIGHT * 2) / GRAVITY) ** 0.5
    return TIMEFALL

def distanceCal(VELOCITYX, TOTALTIME):
    '''
    calculates total distance traveled
    :param VELOCITYX: (float)
    :param TOTALTIME: (float)
    :return: (float)
    '''
    DISTANCE = VELOCITYX * TOTALTIME
    return DISTANCE

def totHeight4 (MAXHEIGHT, SHIPHEIGHT):
    '''
    calculates the total height traveled for scenario 4, since calculation for scenario 3 and 4 are different by a single operation sign LOL
    :param MAXHEIGHT: (float)
    :param SHIPHEIGHT: (float)
    :return: (float)
    '''
    MAXHEIGHT = isNum(MAXHEIGHT)
    SHIPHEIGHT = isNum(SHIPHEIGHT)
    HEIGHTTOTAL = MAXHEIGHT - SHIPHEIGHT
    return HEIGHTTOTAL

def checkPossible(SHIPHEIGHT, MAXHEIGHT):
    '''
    checks if the ball can even hit the ship in the first place
    :param SHIPHEIGHT: (float)
    :param MAXHEIGHT: (float)
    :return: (float)
    '''
    SHIPHEIGHT = isNum(SHIPHEIGHT)
    SHIPHEIGHT = checkNeg(SHIPHEIGHT)

    if SHIPHEIGHT > MAXHEIGHT: #if ball can't even reach the ship
        NEW_SHIPHEIGHT = input(f"The shipheight is too high for the cannonball to reach! Please input a new enemy ship height that is lower than {MAXHEIGHT}:")
        return checkPossible(NEW_SHIPHEIGHT, MAXHEIGHT)
    else:
        return SHIPHEIGHT

def totalTimeCal(TIMEPEAK, FALLTIME):
    '''
    calculates the total time it is in the air
    :param TIMEPEAK: (float)
    :param FALLTIME: (float)
    :return: (float)
    '''
    if TIMEPEAK < 0:
        TIMEPEAK *= -1
    if FALLTIME < 0:
        FALLTIME *= -1
    TOTALTIME = FALLTIME * TIMEPEAK
    return TOTALTIME
### --- OUTPUTS --- ###
def intro():

    '''
    tells the user what the program does and provides an introduction
    :return: (none)
    '''
    print('''
Welcome to the cannonball trajectory calculator!
This program will help you calculate the course of a cannonball depending on the scenario you select!
In this program, North will be positive, and South will be negative!
In addition, gravity is a value that you provide. Here are some different gravities you could play around with! 
(But for realistic calculations, use earth's gravity.)

Mercury: 3.70     Jupiter: 24.8
Venus: 8.87       Saturn: 10.4
Earth: 9.81       Uranus: 8.87
Mars: 3.71        Neptune: 11.2
(values are in m/s)

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
        # if the user requested for scenario 1, the horizontal cannon
        if SCENARIO == 1:
            VELOCITY = input("What is the velocity of the cannonball when it leaves the cannon (in m/s)? ")
            VELOCITY = isNum(VELOCITY) #checks if input is a number
            HEIGHT = input("How high above the water is the cannon located (in meters)? ")
            HEIGHT = isNum(HEIGHT)
            HEIGHT = checkNeg(HEIGHT)
            GRAVITY = input("What is the magnitude of gravity? ")
            GRAVITY = isNum(GRAVITY)  # checks if input is a number
            GRAVITY = checkNeg(GRAVITY)  # checks if input is a negative, cause in this calculator gravity isn't inputted as a negative
            HEIGHT = timeCal(HEIGHT, GRAVITY)  # calculates the time it is in the air using the height
            TIME = HEIGHT #Puts the time into the TIME value to avoid confusion (even though its already confusing LOL)
            DISTANCE = distanceCal(TIME, VELOCITY) # for the distanceCal parameters, we're putting the the time value as the first parameter, and then the requested value as the second parameter
            TIME = round(TIME,2)  # rounds to 2 decimal places, we round it after all the calculations so it can't affect the distance calculation
            DISTANCE = round(DISTANCE, 2)  # rounds the distance to two decimal places
            DIRECTION = direction(DISTANCE) #checks if the number is a positive or negative. If it is positive, it will display north. If it is negative, it will display south
            print(f"The cannonball will be in the air for a total of {TIME} seconds, traveling a total distance of {DISTANCE} meters {[DIRECTION]}. ") #after calculation, displays the answer to the user
        if SCENARIO == 2: #if the user requested for scenario 2, the angled cannon towards parallel ship
            VELOCITY2 = input("What is the velocity of the cannonball as it leaves the cannon (m/s)?" )
            VELOCITY2= isNum(VELOCITY2) #checks if it is a number
            #Requests for and calculates for angle
            ANGLE = input("What is the angle of the cannon to the ground? ")
            ANGLE = checkAngle(ANGLE) #checks if the angle is between 0 and 90
            #Converts the Velocity and anglegiven into velocityX and velocityY
            VELOCITYX = velocityX(VELOCITY2, ANGLE)
            VELOCITYY = velocityY(VELOCITY2, ANGLE)
            GRAVITY = input("What is the magnitude of gravity? ") #Requests for gravity
            GRAVITY = isNum(GRAVITY) #check if gravity num
            GRAVITY = checkNeg(GRAVITY) #check if gravity is negative or not (it shouldn't be negative)
            TIME = timeCal2(VELOCITYY, GRAVITY) #calculates total time in air
            DISTANCE2 = distanceCal2(VELOCITYX, TIME) #calculates total distance
            DIRECTION = direction(DISTANCE2) #determines direction based on if positive or negative
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
            ANGLE3 = input("What is the angle of the cannon to the ground? ")
            ANGLE3 = checkAngle(ANGLE3)
            SHIPHEIGHT = input("How much higher is the your ship compared to the enemies? ")
            SHIPHEIGHT = isNum(SHIPHEIGHT)
            SHIPHEIGHT = checkNeg(SHIPHEIGHT)
            GRAVITY = input ("What is the magnitude of gravity? ")
            GRAVITY = isNum(GRAVITY)
            GRAVITY = checkNeg(GRAVITY)
            VELOCITYX = velocityX(VELOCITY3, ANGLE3)
            VELOCITYY = velocityY(VELOCITY3, ANGLE3)
            TIMEPEAK = timePeak(VELOCITYY, GRAVITY)
            MAXHEIGHT = maxHeight(VELOCITYY, GRAVITY)
            TOTHEIGHT = totHeight(MAXHEIGHT, SHIPHEIGHT)
            FALLTIME = fallTime(TOTHEIGHT, GRAVITY)
            TOTALTIME = TIMEPEAK + FALLTIME
            DISTANCE3 = distanceCal(VELOCITYX, TOTALTIME)
            DISTANCE3 = round(DISTANCE3, 2)  # rounds the distance to two decimal places
            VELOCITYX = round(VELOCITYX, 2)  # rounds the velocityx to two decimal places
            VELOCITYY = round(VELOCITYY, 2)  # rounds the velocityy to two decimal places
            TOTALTIME = round(TOTALTIME, 2)  # rounds the time to two decimal places
            DIRECTION = direction(DISTANCE3)
            print(f"""
The cannonball is moving at {VELOCITYX}m/s horizontally and {VELOCITYY}m/s vertically, being in the air for a total of {TOTALTIME} seconds. 
The total distance the cannonball traveled was {DISTANCE3} meters {[DIRECTION]}. """)
        if SCENARIO == 4:
            VELOCITY4 = input("What is the velocity of the cannonball as it leaves the cannon (m/s)?")
            VELOCITY4 = isNum(VELOCITY4)
            ANGLE4 = input("What is the angle of the cannon to the ground? ")
            ANGLE4 = checkAngle(ANGLE4)
            VELOCITYY = velocityY(VELOCITY4, ANGLE4)
            SHIPHEIGHT = input("How much higher is the enemy ship compared to yours? ")
            SHIPHEIGHT = isNum(SHIPHEIGHT)
            SHIPHEIGHT = checkNeg(SHIPHEIGHT)
            GRAVITY = input("What is the magnitude of gravity? ")
            GRAVITY = isNum(GRAVITY)
            GRAVITY = checkNeg(GRAVITY)
            MAXHEIGHT = maxHeight(VELOCITYY, GRAVITY)
            SHIPHEIGHT = checkPossible(SHIPHEIGHT, MAXHEIGHT) #checks if the cannonball can even reach the ship in the first place
            VELOCITYX = velocityX(VELOCITY4, ANGLE4) #calculates horizontal velocity
            TIMEPEAK = timePeak(VELOCITYY, GRAVITY) #calculates the time it takes to hit its peak
            TOTHEIGHT = totHeight4(MAXHEIGHT, SHIPHEIGHT) #calculates the height from the cannonball to the enemy ship
            FALLTIME = fallTime(TOTHEIGHT, GRAVITY) #calculates the time it takes to fall from that time
            TOTALTIME = totalTimeCal(TIMEPEAK, FALLTIME) #calculates the total time the ball is in the air
            DISTANCE4 = distanceCal(VELOCITYX, TOTALTIME) # calculates the total distance traveled
            DIRECTION = direction(DISTANCE4) #gives it a "north" or "south" direction (read the intro)
            DISTANCE4 = round(DISTANCE4, 2)  # rounds the distance to two decimal places
            VELOCITYX = round(VELOCITYX, 2)  # rounds the velocityx to two decimal places
            VELOCITYY = round(VELOCITYY, 2)  # rounds the velocityy to two decimal places
            TOTALTIME = round(TOTALTIME, 2)  # rounds the time to two decimal places
            print(f"""     
The cannonball is moving at {VELOCITYX}m/s horizontally and {VELOCITYY}m/s vertically, being in the air for a total of {TOTALTIME} seconds. 
The total distance the cannonball traveled was {DISTANCE4} meters {[DIRECTION]}. """)
        if not askContinue():
            exit()

main()