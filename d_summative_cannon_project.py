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


### PROCESSING


### OUTPUTS
def intro():
    '''
    tells the user what the program does and provides an introduction
    :return: (none)
    '''
    print ('''
    ___
   |   \\
   |    \\
   |     \\
   return 
   
    
    ''')


# --- MAIN PROGRAM --- #

intro()