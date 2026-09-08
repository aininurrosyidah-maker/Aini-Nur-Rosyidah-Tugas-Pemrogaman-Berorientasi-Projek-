
#Indentation
task = input("Task: ")

while task != "q":
    print("Task done!")
    task = input("Task: ")

# This statement is outside the loop
print("All tasks completed")
print()


#Print Numbers from 1 to n
n = 10
i = 1

while i <= n:
    print(i)
    i += 1 
print() 

n = 10

# Iterate from i = 1 to n
for i in range(1, n+1):
    print(i)
print()
    
    
#Sum Numbers Until User Enters Zero
total = 0
n = float(input("Enter a number (0 to stop): "))

while n != 0.0:
    total += n
    n = float(input("Enter a number (0 to stop): "))

print(f"Sum: {total}")
print()


#Break and Continue Statements
#The break Statement
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    print(number)
    print()
    
    
#The continue Statement
i = 0

while i <= 10:
    i += 1
    
    # Skip odd numbers
    if i % 2 != 0:
        continue

    print(i)
    print()
    
    
#While Loop with Else Clause
attempts = 3

while attempts > 0:
    pin = input("Enter PIN: ")

    if pin == "1212":
        print("Access granted.")
        break

    attempts -= 1
    print(f"Wrong PIN. {attempts} tries left.")
else:
    print("Account locked. Too many failed attempts.")
    print()
    
    
    
#Python break and continue
#Python break Statement, Example: break in for Loop
number = int(input("Enter a number: "))
for i in range(1, 6):

    # Terminate the loop if i equals number
    if i == number:
        break
    print(i)
    print()
    
    
#break in while loop 
while True:
    number = int(input("Enter a number: "))
    if number < 0:
        break
    print(f"You entered {number}")
    print()
    
    
#Python continue Statement, Example: continue in for Loop
for i in range(1, 11):

    # Condition to check if a number is even
    if i % 2 == 0:
        continue
    print(i)
    print()
    
    
#Sum of Only Positive Numbers
total = 0

while True:
    number = int(input("Enter a number (0 to stop): "))

    # Skip negative numbers
    if number < 0:
        continue

    # End the loop if the user enters 0
    if number == 0:
        break

    total += number

print(f"Sum of positive numbers: {total}")
print()


#Loop with else Clause
stock = ['Laptop', 'Keyboard', 'Mouse']

order = input("Enter the product you want to buy: ")

for product in stock:
    if product == order:
        print(f"{order} is available. Adding to cart.")
        break
else:
    print(f"Sorry, {order} is out of stock.")
    print() 
    
    
#Python pass Statement
#pass Statement
for i in range(1, 5):
    if i == 3:
        pass  # Placeholder for future code
    else:
        print(i)
        print()
        
is_valid = True

if is_valid:
    pass
else:
    print("Login invalid. Redirect to form.")
    print()