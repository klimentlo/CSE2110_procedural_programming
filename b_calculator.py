#_calculator2.py

'''
title: Calculator using functions
author: Kliment Lo
date-created: 2022-09-19
'''

'''
1. display a welcome message for the user that gives instructions OUTPUT
2. ask user for the operation they would like to perform INPUT
3. ask user for the first number INPUT
4. ask user for the second number *if applicable INPUT
5. calculate the answer PROCESSING
6. display the answer OUTPUT
7. ask user if they would like to perform another calculation INPUT
'''
# comment to test if push
import math

# --- FUNCTIONS --- #



### INPUTS
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
        return checkInt(NEW_NUM)


def checkFloat(NUMBER):
    '''
    Verify the string is a number
    :param NUMBER: (str)
    :return: (float
    '''
    try:
        NUMBER = float(NUMBER)
        return NUMBER
    except ValueError:
        print(" You did not enter a number!" )
        NEW_NUM = input("Please enter a number: ")
        return checkFloat(NEW_NUM)


def menu():
    '''
    User selects which math operation to perform
    :return:
    '''
    print('''
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Sin(x)
    ''')
    CHOICE = input("Choose an operation to perform: ")
    CHOICE = checkInt(CHOICE)
    if CHOICE > 0 and CHOICE < 6:
        return CHOICE
    else:
        print("Please select a valid number! ")
        return menu()


def askNum(ORDER, UNIT = ""):
    '''
    Asks user for a number
    :param ORDER: (str)
    :param UNIT: (str)
    :return: (float)
    '''
    NUMBER = input(f"Please enter the {ORDER} number: {UNIT} ")
    return checkFloat(NUMBER)
### PROCESSING
def addNum(NUM1, NUM2):
    '''
    adds two numbers together
    :param NUM1: (float)
    :param NUM2: (float)
    :return: (float)
    '''
    ANSWER = NUM1 + NUM2
    return ANSWER

def subNum(NUM1, NUM2):
    '''
    subtracts two numbers together
    :param NUM1: (float)
    :param NUM2: (float)
    :return: (float)
    '''
    ANSWER = NUM1 - NUM2
    return ANSWER

def mulNum(NUM1, NUM2):
    '''
    multiplies two numbers together
    :param NUM1: (float)
    :param NUM2: (float)
    :return: (float)
    '''
    ANSWER = NUM1 * NUM2
    return ANSWER

def divNum(NUM1, NUM2):
    '''
    divides two numbers together
    :param NUM1: (float)
    :param NUM2: (float)
    :return: (float)
    '''
    ANSWER = NUM1 / NUM2
    return ANSWER

def calcSine(NUMBER):
    '''
    Calculate the Sine trig ratio of an angle
    :param NUMBER: (float) degrees
    :return: (float)
    '''
    # sin function in the math library uses radians, but we asked for the input in degrees  (because people use degrees)
    RADIANS = math.radians(NUMBER)
    # this uses the radians function from the library to convert NUMBER from its original units of degrees into radians
    RESULT = math.sin(RADIANS)
    return RESULT

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

### OUTPUTS
def intro():
    '''
    displays program instructions to the user
    :return: (none)
    '''
    print ('''
Welcome to Calculator! 
    ''')

def displayAnswer (RESULT):
    '''
    displays answer for user
    :param RESULT: (float)
    :return: (none)
    '''

    if RESULT == int(RESULT):
        RESULT = int(RESULT)
    else:
        RESULT = round(RESULT, 2)
        #this rounds result to 2 decimal places
    print(f"The answer is {RESULT}. ")
        #add to main() by replacing print(RESULT) with displayAnswer(RESULT)
# --- MAIN PROGRAM === #
def main():
    '''
    main is the function that contains all of our functions
    :return: (none)
    '''
    intro()
    while True:
        OPERATION = menu()

        if OPERATION < 5:
            NUMBER1 = askNum("first")
            NUMBER2 = askNum ("second")
            if OPERATION == 4 and NUMBER2 == 0:
                print("You cannot divide by zero. ")
                NUMBER2 = askNum("second")
            print(NUMBER1, NUMBER2)
            # askNum has two params, ORDER and UNIT
            # here we only providing one: ORDER
            # this is allowed because in the function, UNIT = "" so UNIT will always have a value even if we don't provide one
        else:
            NUMBER1 = askNum("first", "(Degrees) ")
            print(NUMBER1)
            # in this case we are providing two arguments so both the ORDER and UNIT params have new values
        if OPERATION == 1:
            RESULT = addNum(NUMBER1, NUMBER2)
        elif OPERATION == 2:
            RESULT = subNum(NUMBER1, NUMBER2)
        elif OPERATION == 3:
            RESULT = mulNum(NUMBER1, NUMBER2)
        elif OPERATION == 4:
            RESULT = divNum(NUMBER1, NUMBER2)
        else:
            RESULT = calcSine(NUMBER1)
        displayAnswer(RESULT)
        if not askContinue():
            exit()
        #if not means "if the function is False"
        # for something to happen if askContinue is True, you could use if askContinue() instead of if not askContinue()

print(__name__)
# --- MAIN PROGRAM CODE --- #
if __name__ == "__main__":
    main()
#we will discuss this lander in notes about magic variable
# essentially it allows you to use a program like a library without running the risk of executing the program
