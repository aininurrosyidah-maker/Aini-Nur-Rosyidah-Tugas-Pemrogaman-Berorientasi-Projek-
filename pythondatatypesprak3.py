#Python Numbers, Type Conversion and Mathematics
#Python Numeric Data Type
num1 = 9
print(num1, 'is of type', type(num1))

num2 = 9.54
print(num2, 'is of type', type(num2))

num3 = 8+2j
print(num3, 'is of type', type(num3))
print()


#Number System 
print(0b1101011)  # prints 107

print(0xFB + 0b10)  # prints 253

print(0o15)  # prints 13
print()



#type conversion in python
print(1 + 5.0) # prints 6.0
print(1 + int(5.0)) # prints 6
print(1 + float(5)) # prints 6.0
print()

num1 = int(2.3)
print(num1)  # prints 2

num2 = int(-2.8)
print(num2)  # prints -2

num3 = float(5)
print(num3) # prints 5.0

num4 = complex('3+5j')
print(num4)  # prints (3 + 5j)
print()



#Random Module
import random

print(random.randrange(10, 20))

list1 = ['a', 'b', 'c', 'd', 'e']

# get random item from list1
print(random.choice(list1))

# Shuffle list1
random.shuffle(list1)

# Print the shuffled list1
print(list1)

# Print random element
print(random.random())
print ()    


#python Mathematics
import math

print(math.pi)

print(math.cos(math.pi))

print(math.exp(10))

print(math.log10(1000))

print(math.sinh(1))

print(math.factorial(6))
print()


#Python List
#creating a lis
cart = ["Book", "Pencil", "Rules"]
print(cart)

# A list of mixed data types
my_list = [11, "Hello Word", 3.98]
print(my_list)

# Empty list
my_list = []
print(my_list)
print ()

vowels = "AIUEO"

# Convert a string to a list
vowels_list = list(vowels)
print(vowels_list)
print ()    


#Accessing List Items
languages = ["Python", "Swift", "C++"]

# Access the first item
print(f"languages[0] = {languages[0]}")

# Access the third item
print(f"languages[2] = {languages[2]}")
print ()


#Negativ Indexing
languages = ["Python", "Swift", "C++"]

# Access the last item
print('languages[-1] =', languages[-1])

# Access the third last item
print('languages[-3] =', languages[-3]) 
print()


#Adding and Updating ITems
cart[1] = ["T-shirt", "Lamp", "Pen"]

# Update second item to "Shoes"
cart[1] = "Shoes"

print(cart)    # ['T-shirt', 'Shoes', 'Pen']
print ()



#Remove Items From a List
cart = ["T-shirt", "Lamp", "Pen", "Book"]

# Remove "Pen" from the list
cart.remove("Pen")    # ['T-shirt', 'Lamp', 'Book']

# Remove the last item
last_item = cart.pop()
print(cart)   # ['T-shirt', 'Lamp']
print(last_item)    # Book

# Clear the list
cart.clear()
print(cart) 



#Copying a list
cart = ['T-shirt', 'Lamp', 'Pen', 'Book']

# Delete the third item (index 2)
del cart[2]
print(cart)    # ['T-shirt', 'Lamp', 'Book']

# Delete the list itself
del cart [2]
print(cart)    # NameError: name 'cart' is not defined
print ()

favorite_items = ["T-shirt", "Lamp", "Pen"]

# Copying a list
cart = favorite_items.copy()

# Add an item to favorite_items list
favorite_items.append("Book")

print(f"favorite_items = {favorite_items}")
print(f"cart = {cart}")
print ()


#Python List Method
#The len() Function
favorite_items = ["T-shirt", "Lamp", "Pen"]

size = len(favorite_items)
print(size)   # 3
print ()

#List Membership Test
cart = ["T-shirt", "Lamp", "Pen"]

result = "Lamp" in cart
print(result)   # True

result = "Book" in cart
print(result)   # False
print ()

#Iterating Through a List
cart_items = ["T-shirt", "Lamp", "Pen"]

for item in cart_items:
    print(item)
    print ()


#Python Tuples
#Creating a Tuple

# empty tuple
my_tuple = ()

# tuple having integers
my_tuple = (1, 2, 3)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# tuple can be created without parentheses
# also called tuple packing
my_tuple = 3, 4.6, "dog"
# tuple unpacking is also possible
a, b, c = my_tuple
print ()


#Iterating Through a Tuple
for name in ('John','Kate'):
    print("Hello",name)
    print()
    
    


#Python Strings
#Python Multiline Strings
message = """To avoid pain, they avoid pleasure.
To avoid death, they avoid life."""

print(message)
print ()



#Access String Characters
model = 'ChatGPT'

# Access the first character
print(model[0])    # Output: C

# Access the fifth character
print(model[4])    # Output: G

model = 'ChatGPT'
print(model)       
print ()



#Strings are Immutable
model = 'ChatGPT'

model = "W" + model[1:]
print(model) 
print()


#Python String Methods
text = "ChatGPT is great."

# Replace "ChatGPT" with "Claude"
new_text = text.replace("ChatGPT", "Claude")

print(new_text)  # Output: Claude is great.
print()


#String Membership Test
print('Chat' in 'ChatGPT')        # True
print('Claude' not in 'ChatGPT')  # True
print()


#Iterate Through a String
model = 'Opus'

for c in model:
    print(c)
    print()
    


#Python String Length
model = 'Opus'

# Count the number of characters
print(len(model))   # Output: 4
print ()


#Escape Sequences
# escape double quotes
example = "He said, \"What's there?\""

# escape single quotes
example = 'He said, "What\'s there?"'

print(example)
print ()


#String Formatting (f-Strings)
company = 'Google'
field = 'AI'

message = f'{company} is an {field} company.'
print(message)
print ()



#Python Dictionary
# creating a dictionary
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "England": "London"
}

# printing the dictionary
print(country_capitals)
print()


#Access Dictionary Items
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "England": "London"
}

# access the value of keys
print(country_capitals["Germany"])    # Output: Berlin
print(country_capitals["England"])    # Output: London
print ()


#Add Items to a Dictionary
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
}

# add an item with "Italy" as key and "Rome" as its value
country_capitals["Italy"] = "Rome"

print(country_capitals)
print ()



#Remove Dictionary Items
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
}

# delete item having "Germany" key
del country_capitals["Germany"]

print(country_capitals)
print()



#Change Dictionary Items
country_capitals = {
  "Germany": "Berlin", 
  "Italy": "Naples", 
  "England": "London"
}

# change the value of "Italy" key to "Rome"
country_capitals["Italy"] = "Rome"

print(country_capitals)
print()



#Iterate Through a Dictionary
country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome" 
}

# print dictionary keys one by one
for country in country_capitals:
    print(country)

print()

# print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)
    print ()
    
    
#Find Dictionary Length
country_capitals = {"England": "London", "Italy": "Rome"}

print(len(country_capitals))   

numbers = {10: "ten", 20: "twenty", 30: "thirty"}
print(len(numbers))            
countries = {}
print(len(countries))          
print ()



#Dictionary Membership Test
file_types = {
    ".txt": "Text File",
    ".pdf": "PDF Document",
    ".jpg": "JPEG Image",
}

print(".pdf" in file_types)       
print(".mp3" in file_types)       
print(".mp3" not in file_types)   

