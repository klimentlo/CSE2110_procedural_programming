# a_pancakes.py

'''
title: Pancake Calculator
author: Kliment Lo
date-created: 2022-09-22
'''

# --- SUBROUTINES --- #

### INPUTS
def getFlour():
    '''
    Ask user for amount of flour in cups
    :return: (float)
    '''
    FLOUR = float(input("How many cups of flour do you have? "))
    return FLOUR

def getEggs():
    '''
    Ask user for  number of eggs
    :return: (int)
    '''
    EGGS = int(input("How many eggs do you have? "))
    return EGGS

def getMilk():
    '''
    Ask user for amount of milk in cups
    :return: (float)
    '''
    MILK = float(input("How many cups of milk do you have?"))
    return MILK

def getIngredients():
    '''
    Ask user for Flour (cups), Milk (cups), Eggs (amount)
    :return: (float), (float), (int)
    '''
    FLOUR = float(input("How many cups of flour do you have?"))
    MILK = float(input("How many cups of milk do you have "))
    EGGS = int(input("How many eggs do you have? "))
    return FLOUR, MILK, EGGS
### PROCESSING

def  makePancakes(FLOUR, MILK, EGGS):
    '''
    Calculates how many pancakes can be made
    :param FLOUR: (float)
    :param MILK: (float)
    :param EGGS: (int)
    :return: (int) Number of servings
    '''
    # A serving of pancakes requires 1.5 cups flour, 1 cup milk, and 2 eggs

    if FLOUR < 1.5 or MILK < 1 or EGGS < 2:
        return 0
    else:
        FLOUR_SERVINGS = FLOUR // 1.5
        # FLOUR_SERVINGS is the whole number amount of servings worth of flour
        MILK_SERVINGS = int(MILK)
        # if MILK = 1.9, int(MILK) = 1
        EGGS_SERVINGS = EGGS // 2

    SERVINGS = FLOUR_SERVINGS
    if MILK_SERVINGS < SERVINGS:
        SERVINGS = MILK_SERVINGS
    if EGGS_SERVINGS < SERVINGS:
        SERVINGS = EGGS_SERVINGS

    return int(SERVINGS)
    #returning a variable is similar to giving an outputttt

def lowIngredient(FLOUR,MILK):
    '''
    Determine which ingredient the user doesn't have enough of
    :param FLOUR: (float)
    :param MILK: (float)
    :param EGGS: (int)
    :return: LOW (string)
    '''
    if FLOUR < 1.5:
        LOW = "flour"
    elif MILK < 1:
        LOW = "milk"
    else:
        LOW = "eggs"
    return LOW
    ### OUTPUTS

def displayPancakeDozen(DOZEN, LOW):
    '''
    display how many dozen of pancakes the user can make
    :param DOZEN: (int)
    :return: (none)
    '''
    if DOZEN == 0:
        print(f"You don't have enough ingredients to make any pancakes. Go get {LOW} then come back. ")
    else:
        print(f"You can make {DOZEN} dozens of pancakes! :D")
        # print(f"string") lets you insert variables into a string without needing to separate the string into several strings
# --- MAIN PROGRAM CODE ##
### INPUTS
'''
FLOUR = getFlour()
MILK = getMilk()
EGGS = getEggs()
'''

FLOUR, MILK, EGGS = getIngredients()
# It's important to make sure the variables are in the same order as the outputs from the function

print (FLOUR, MILK, EGGS)
### PROCESSING
SERVINGS = makePancakes(FLOUR, MILK, EGGS)
if SERVINGS == 0:
    LOW = lowIngredient(FLOUR, MILK)
else:
    LOW = ""

# to have a return give an output, the variable must be made = to the function (the variable and the return do not need the same name
print(SERVINGS)

### OUTPUTS
displayPancakeDozen(SERVINGS, LOW)
# SERVINGS is a global variable that can be used as an argument for any function... in this case it is the argument for the parameter "DOZEN" inside of displayPancakesDozen (DOZEN is a local variable)
# local variables allows multiple functions to use the same variable names without interfering with one another... if you're working on a large project and use the variable name NUMBER, problems could arise if all variables were global variables because another function would likely also have a variable called number