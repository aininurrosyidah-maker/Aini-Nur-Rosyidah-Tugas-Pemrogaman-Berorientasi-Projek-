#Python Functions
def greet():
    print('Hello World!')

# call the function
greet()

print('Outside function')
print()

#functions arguments
def greet(name):
    print("Hello", name)

# pass argument
greet("John")
print ()


#Function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)

# function call with two values
add_numbers(5, 19)
print()

#The return Statement
# function definition
def find_square(num):
    result = num * num
    return result

# function call
square = find_square(3)

print('Square:', square)
print()


#Python Library Function
import math

# sqrt computes the square root
square_root = math.sqrt(4)

print("Square Root of 4 is",square_root)

# pow() comptes the power
power = pow(2, 3)

print("2 to the power 3 is",power)
print()


#Python Function Arguments
def add_numbers(a, b):
    sum = a + b
    print('Sum:', sum)

add_numbers(2, 3)
print()


#Function Argument with Default Values
def add_numbers( a = 7,  b = 8):
    sum = a + b
    print('Sum:', sum)


# function call with two arguments
add_numbers(2, 3)

#  function call with one argument
add_numbers(a = 2)

# function call with no arguments
add_numbers()
print ()


#Python Keyword Argument
def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

display_info(last_name = 'Cartman', first_name = 'Eric')
print ()


#Python Function With Arbitrary Arguments
# program to find sum of multiple numbers 

def find_sum(*numbers):
    result = 0
    
    for num in numbers:
        result = result + num
    
    print("Sum = ", result)

# function call with 3 arguments
find_sum(1, 2, 3)

# function call with 2 arguments
find_sum(4, 9)
print()


#Python Variable Scope
def greet():
    message = 'Hello'
    print('Local', message)
greet()

print(message)
print()


#Python Global Variables
message = 'Hello'
def greet():
    # declare local variable
    print('Local', message)
greet()

print('Global', message)
print()

#Python Nonlocal Variables
def outer():
    message = 'local'

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)
outer()
print()


#Python Global Keyword
c = 1 # global variable

def add():
    print(c)

add()
# global variable
c = 1 

def add():

     # increment c by 2
    c = c + 2

    print(c)

add()
print()


#Python Recursion
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))
print()

def recursor():
    recursor()
recursor()
print()


#Python Modules
#Import Python Standard Library Modules
import math
# use math.pi to get value of pi
print("The value of pi is", math.pi)
print()

#Python import with Renaming
# import module by renaming it
import math as m

print(m.pi)
print()


#Python from...import statement
#import only pi from math module
from math import pi

print(pi)
print()


#Import all names
# import all names from the standard module math
from math import *

print("The value of pi is", pi)
print()


#The dir() built-in function
print(dir(example))

['__builtins__',
'__cached__',
'__doc__',
'__file__',
'__initializing__',
'__loader__',
'__name__',
'__package__',
'add']
print()


a = 1
b = "hello"

import math

print(dir())

['__builtins__', '__doc__', '__name__', 'a', 'b', 'math', 'pyscripter']
print()


#Python Main function
#Using if conditional with __name__
def main():
    print("Hello World")

if __name__=="__main__":
    main()
print()


