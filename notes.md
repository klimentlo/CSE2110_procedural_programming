#CSE2110 Procedural Programming 1 Notes

## Procedures and Functions
Subroutines contain two different categories: procedures a nd functions. Procedures are a series of steps, like following the steps of a recipe or a lab investigation. Functions, however, take some data as inputs (called _arguments_) and they __transform__ the arguments into new data. The new data can then be returned at the end of the function (or simply printed at the end of the function). The __main difference__ between procedures and functions is that functions have their own __inputs and outputs_.

## Ex. 1 - Math Functions
Functions in programming are similar to functions in mathematics. There are processes where data is inputted ino the function and a new result exits function. Therefore, an individual function can be considered a sub-program within the program. It will have its own inputs, processing, and variables.

f(x) = 4x + 5
```
| INPUTS | Processing | OUTPUTS
|   0    | 4(0) + 5   |    5
|   1    | 4(1) + 5   |    9
|   1    | 4(2) + 5   |    13
|   1    | 4(3) + 5   |    17
```
Inputs are like know variables, processing is like showing your work/solving an equation, and an output is like the answer to an equation.

## Structure of a Function
```python
# python version of the equation

def myFunction(x):
    # x is a PARAMETER which is similar to an input
    # myFunction is transformation code for the values (ARGUMENTS) inputted to the PARAMETERS
    y = 4 * x + 5
    return y

print(myFunction(4))
# 4 is the argument and the parameter x = 4
# myFunction(5) makes the parameter, x, equal to the argument, 5

"""
or:
y = myFunction(4)
print(y)
"""
```

Creating a function uses the same statement as creating a procedural subroutine ```def```. However, functions also include __parameters__ within the parenthesis following the function name. 

__Arguments__ are the external data (numbers, string, variable, data structure, etc.) values that are inputted into the parameter from the rest of the program (the parameter is equal to the argument). The data is stored inside the function using the parameter name instead of the argument name outside the function. (the parameter is INSIDE nad the argument is OUTSIDE)

Once the function completes its processing with the input values, it can __return__ a value back to the main program. The main program will then need to store the returned value in a variable if it is needed further along in the program. Return variables can also include a statement that occurs in a single line. For examples, printing (```return print (x)```) or typecasting (``` return int (VAR) ```)

__A function must have _either_ an input or an output. It does not require both__ 

### Variables in a Function
There are two categories of variables: global and local. Global variables are in the main program and local variables are within a particular subroutine and do not exist in the main program. 

However, a subroutine can call a global variable using the global statement within the subroutine

## Advantages of Functional Programming
1. __Repeatability__. which means that once the function is written, it can be used multiple times in different section of the program without needing to rewrite the same lines over and over again
2. __Modularity__, which means you can make changes to a function or replace one function with another without the potential for breaking the rest of the program
3. __Debugging and Testing__, if a program isn't working properly, functions can be isolated to help locate the problem 
4. __Collaboration__ , because local variables don't affect the rest of the main program. Multiple developers can be creating different functions and don't need to coordinate variable names or data structures

## Returning Multiple Values From a Function
A function can return multiple variables. In order to store all return values, separate variables must be used (or more complex data structure).

```python 
#return multiple values

def myFunction():
    return VALUE1, VALUE2

VARIABLE1, VARIABLE2 = myFunction()
#this would make VARIABLE1 (global) equal to VALUE1 (local to myFunction()) and would make VARIABLE2 equal to VALUE2
# empty comment
```

## Recursive Functions
Recursive functions are functions that return to the same function. This return value will only have in certain instances and there is _always_ a return value that is not in the function. 

```python
NUM = input("Please enter a number. ")
def checkInt(NUM):
    if NUM.isnumeric():
        return int(NUM)
    else:
        print("Please enter a NUMBER!!!!! >:( ")
        NEW_NUM = input ("Number: ")
        return checkINT (NEW_NUM)
```

ASIDE: It is possible to call one function within a different function, but using this technique does not follow the IPO formatting we use so ... try not to, unless you need to

## Default Parameters 
A function can have default arguments in the event that no arguments are passed into the function. Default parameters are often optional and are usually placed at the end of the function's parameters in descending order of importance

```python
# function with default arguments
def myFunction(param1 = True):
    return param1

print(myFunction()) # print True
print(myFunction(False)) # print False
```

Note: The function cannot skip the default parameters. If there is a parameter lower in the list of parameters, all default parameters must have arguments supplies to reach the desired parameter

```python
def myOtherFunction(param1, param2 = "", param3 = ""):
    print(param1)
    print(param2)
    print(param3)

myOtherFunction(1,3)
```

## Using Multiple Files
Subroutines can be stored in separate files to organize the functions and improve collaboration. For example, if you make a program to make sales at a coffee shop, functions can be organized into payments, transactions, and reports. Each of these categories can be in a separate file imported into the main file. in this scenario, developers can work on separate features of the program without disrupting other developers.

In order to link multiple files together, python uses the ```import``` statement. Files must be in the same folder as (or a sub-folder of) the main program file.

The filename of the secondary files must follow variable and naming conventions including being alphanumeric (but not starting with a number) and only using hyphens and underscores as special characters (NO SPACES!)

### The \_\_name\_\_ magic variable

When python runs a file, it associates the "\_\_main\_\_" value to the \_\_name\_\_ magic variable for the file that runs. All other files imported into the running program will use their filename as the \_\_main\_\_ magic variable. __Magic Variables__ are predetermined variables on the backend of the programming language that help program run. Oftentimes, programs don't need to modify these values in the program.

Magic variables are indicated by two underscores before and after the next (we need to use slashes to separate the underscores in notes.md because underscores in the md files apply text formatting). They are sometimes called "double underscore variables" or "dunder variables". Since python automatically updates the \_\_name\_\_ magic variable, a check can be included to ensure that code runs only is the given file is run, and not when it's imported. This check  allows subroutines and functions can be tested in the respective files without the tests being imported into the main program.

```python
def someFunction(PARAM):
    VALUE = PARAM * PARAM
    return VALUE

if __name__ == "__main__":
#this section wil only run if this file is run, not imported into another file
    print(someFunction(VAR1))
```
