#creating variables

name = "Joshua Pina" 
age = 31
height = 6.1
is_muscular = True

# printing variables
print(f"My name is {name}, I am {age} years old, my height is {height} feet tall, and yes it is {is_muscular} that I am jacked.")

#basic math

a = 7
b = 11
print()
print(f"A = {a}, B = {b}")
print("\nHere is an example of some basic math operations ->")
print("Addition:", a + b)
print(f"Addition of {a} and {b} is {a + b}")
print()
print("Subtraction:", a - b)
print(f"Subtraction of {a} and {b} is {a - b}")
print()
print("Floor Division:", a // b)
print(f"Floor Division of {a} and {b} is {a // b}")
print()
print("Exponentiation:", a ** b)
print(f"Exponentiation of {a} to the power of {b} is {a ** b}")
print()
print("Modulus:", a % b)
print(f"Modulus of {a} and {b} is {a % b}")
print("-" * 35)
# Resetting variables

print("\nResetting variables...enter your information")
name = input("Please enter a name: ")
age = input("Please enter an age: ")
height = input("Please enter a height in feet: ")
is_muscular = input("Are you jacked? (True/False): ")
favorite_number = input("Please enter your favorite number: ")
print()

# Printing reset variables
print(f"\nAfter reset: \nMy name is {name}, I am {age} years old. my favorite number is {favorite_number}, my height is {height} feet tall, and yes it is {is_muscular} that I am jacked.")
print()

# Basic math reset
a = int(input("Please enter a number for A: "))
b = int(input("Please enter a number for B: "))

print("After reset: \n")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

#Basic Paycheck Calculation
print("\nLet's guestimate your paycheck!")
pay_type = input("Please enter 'salaried' or 'hourly': ").strip().lower()
if pay_type == 'salaried':
    annual_salary = float(input("Please enter your annual salary: "))
    weeks_per_year = 52
    weekly_pay = annual_salary / weeks_per_year
    print(f"Your estimated weekly paycheck is: ${weekly_pay:.2f}")
elif pay_type == 'hourly':
    hourly_wage = float(input("Please enter your hourly wage: "))
    hours_per_week = float(input("Please enter the number of hours you work per week: "))
    weekly_pay = hourly_wage * hours_per_week
    print(f"Your estimated weekly paycheck is: ${weekly_pay:.2f}")
else:
    print("Invalid input. Please enter 'salaried' or 'hourly'.")

print(f"{name}, you are {age} years old, {height} feet tall, and {'jacked' if is_muscular.lower() == 'true' else 'not jacked'}.\n Your estimated weekly paycheck is: ${weekly_pay:.2f}")