# d_summative_cannon_project.py
'''
title: cannon operator
author: kliment lo
date-created: 2022-09-21
'''
# --- FUNCTIONS --- #

### INPUTS
def menu():
    '''
    User selects which Scenario they want to calculate
    :return:
    '''
    print('''
Scenario 1:
    ____
    |   \\
    |    \\
    |     \\
    Horizontal to the water
    
Scenario 2:
       ___
      /   \\
     /     \\
    /       \\
    Parabolic to a level boat
    
    
Scenario 3:    
      ____
     /    \\
    |      \\
    |       \\
    Parabolic to a smaller boat far away
    ''')

    CHOICE = input("Select a scenario you'd like to calculate: ")
    CHOICE = checkInt(CHOICE) #sends the value to the checkInt function, to see if the input is an integer (1, 2, 3, etc.)
    if CHOICE > 0 and CHOICE < 5:
        return menu()
    else:
        CHOICE = validNum(CHOICE)
        print("Please select a valid number! ")
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
        print ("That is not a number! ")
        NEW_NUM = input("Please enter a valid number: ")
        #It now takes the new imput (or new number) and returns it to checkInt. It then runs the new number into checkint. If the new imput isn't        an integer, itll run this program again
        return checkInt(NEW_NUM)
### PROCESSING


### OUTPUTS
def intro():
    '''
    tells the user what the program does and provides an introduction
    :return: (none)
    '''
    print ('''
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
        OPERATION = menu()
        print(OPERATION())
main()