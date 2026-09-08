# Python fundamentals
#Python Variables and Literals

# assign value to site_name variable
site_name = 'programiz.pro'

print(site_name)
print ()


#Changing the Value of a Variable in Python
site_name = 'Hello World'
print(site_name)

# assigning a new value to site_name
site_name = 'andi welcome to programiz'

print(site_name)
print ()

#Assigning multiple values to multiple variables 
a, b, c = 5, 3.2, 'Hello all'

print (a)  # prints 5
print (b)  # prints 3.2
print (c)  # prints Hello all
print ()

site1 = site2  = 'Hello World'

print (site1)  # prints Hello World
print (site2)  # prints Hello World
print ()




#Python Type Conversion
#Converting integer to float
integer_number = 234
float_number = 2.34

new_number = integer_number + float_number

# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))
print ()


#Addition of string and integer Using Explicit Conversion
num_string = '13'
num_integer = 25

print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))
print ()



#Python Basic Input and Output
#Python Output
print('Python is powerful')
print ()

#Python Print Statement
print('konnichiwa!')
print('Ogenki desu ka?')
print('Watashi wa genki desu!')
print ()


#Python print() with end Parameter
print('Ohayou Gozaimasu!', end= ' ')

print('Kyou wa harete iru ne')
print() 


#Python print() with sep Parameter
print('New Year', 2023, 'See you soon!', sep= '. ')
print ()



#Print Python Variables and Literals
number = -10.6

name = "Hello World"

# print literals     
print(5)

# print variables
print(number)
print(name)
print ()

print('Hello World is ' + 'awesome.') 
print('Python is ' + 'great.')
print('Python ' + 'is ' + 'fun.')
print()



#Print Concatenated Strings
print('Programiz is ' + 'awesome.')
print('Python is ' + 'great.')
print('Python ' + 'is ' + 'fun.')
print()

#Output formatting
x = 10
y = 15

print('The value of x is {} and y is {}'.format(x,y))
print('The value of x is {1} and y is {0}'.format(x,y))
print('The value of x is {x} and y is {y}'.format(x=x,y=y))
print()


#Python User Input
# using input() to take user input
num = input('Enter a number: ')

print('You Entered:', num)

print('Data type of num:', type(num))
print()



#Python Operators
#Python Arithmetic Operators
x = 10
y = 5
print('x + y = ',x+y)
print('x - y = ',x-y)
print('x * y = ',x*y)
print('x / y = ',x/y)
print('x // y = ',x//y)
print('x ** y = ',x**y)
print('x % y = ',x%y)
print()


#Comparison operators
x = 8
y = 12
print('x > y  is',x>y)
print('x < y  is',x<y)
print('x == y is',x==y)
print('x != y is',x!=y)
print('x >= y is',x>=y)
print('x <= y is',x<=y)
print()


#Logical operators
x = True
y = False
print('x and y is',x and y) 
print('x or y is',x or y)
print('not x is',not x)
print('not y is',not y)
print() 


#Bitwise operators
x = 10
y = 4
print('x & y =',x & y)
print('x | y =',x | y)
print('x ^ y =',x ^ y)
print('~x =',~x)
print('x << 2 =',x << 2)
print('x >> 2 =',x >> 2)
print ()


#Assignment operators
x = 5
print('x =',x)
x += 3
print('x += 3 is',x)
x -= 3
print('x -= 3 is',x)
x *= 3
print('x *= 3 is',x)
x /= 3
print('x /= 3 is',x)
print('x //= 3 is',x)
x **= 3
print('x **= 3 is',x)
print('x %= 3 is',x)
print()


#Special operators
#Identity operators
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)
print(x3 is not y3)
print()

#Membership operators
x = 'Hello world'
y = {1:'a',2:'b'}
print('H' in x)
print('hello' not in x)
print(1 in y)
print('a' in y)
print('b' not in y)
print()





