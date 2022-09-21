# c_multi_file.py
'''
title: working with multiple files
author: kliment lo
date-created: 2022-09-21
'''

import b_calculator
# this imports all the functions from the calculator program we just wrote

def calcExponent(NUMBER1, NUMBER2):
    '''
    Calculate the number value of ome number to the power of another number
    :param NUMBER1: (int)
    :param NUMBER2: (int)
    :return: (int)
    '''
    RESULT = NUMBER1 ** NUMBER2
    # ** is for "to the power of" so 2 ** 3 = 8, and 3 ** 2 = 9
    return RESULT

def menu():
    print('''
    1. Calculate exponents
    ''')
    CHOICE = input("Please enter a number, from the hundreds of options above. ")
    CHOICE = b_calculator.checkInt(CHOICE)
    return CHOICE
OPERATION = menu()

if OPERATION == 1:
    NUM1 = b_calculator.askNum("first")
    NUM2 = b_calculator.askNum("second")
    ANSWER = calcExponent(NUM1, NUM2)
    b_calculator.displayAnswer(ANSWER)

















