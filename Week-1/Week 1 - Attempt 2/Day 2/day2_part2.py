age = int(input("Please enter your age: "))

if age >= 21:
    print("You are old enough to drink alcohol in the US.")
elif age >= 18:
    print("You are old enough to vote in the US, but not old enough to drink alcohol.")
else:
    print("Dang, you can't do anything yet.")

print("-" * 50
      )
#For Loops:

for i in range(5):
    print("i = ", i)
print("-" * 50)

#While Loops:

count = 0
while count < 5:
    print("count = ", count)
    count += 1
print("-" * 50) 

# List Operations:
my_list = [1, 2, 3, 4, 5]               
print("Original List:", my_list)
my_list.append(6)  # Adding an element
print("List after appending 6:", my_list)
my_list.remove(2)  # Removing an element
print("List after removing 2:", my_list)
my_list.sort()  # Sorting the list
print("Sorted List:", my_list)
print("-" * 50)

# Age-based message
age = int(input("Please enter your age: "))

if age >1 and age <4:
    print("You're a toddler.")
elif age < 13:
    print("You're a child.")
elif age < 18:
    print("You're a teen.")
elif age >= 18 and age < 27:    
    print("You're a young adult.")
else:
    print("You're an adult.")
print("-" * 50)

for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
print("-" * 50)

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
print("-" * 50)

import random
# Random number guessing game
secret = random.randint(1,10)
guess = None

while guess != secret:
    guess = int(input("Guess the number (1-10): "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Dude! You've guessed the number!")
