#Data Structures

#List = Ordered, mutable, Dupes -> Stores items in order
#Tuple = Ordered, immutable, Dupes -> Fixed data grouping
#Set = Unordered, mutable, No dupes -> Unique items only
#Dictionary = Unordered, mutable, No dupes -> Key-value pairs

#Lists:
print("-" * 50)
siblings = ["Rico", "Lyndsay", "Jen"]
print()
print("The first element is: ", siblings[0])  # Accessing the first element
print("The second element is: ", siblings[1])  # Accessing the second element
print("The third element is: ", siblings[2])  # Accessing the third element
print()
print("-" * 50)
print("\n")

print(f"My siblings names are {siblings[0]}, {siblings[1]}, and {siblings[2]}.")
print()
print("The full list is ", siblings)
print()
siblings.append("Fake Name")
print("After appending a name to the end of the list, we have: ", siblings)  # After appending a new element
print()
siblings.remove("Fake Name")  # Removing the last element
print("After removing the name from the end of the list, we have: ", siblings)  # After removing the last element
print()
print("The length of the list is: ", len(siblings))  # Length of the list
print()
print("-" * 50)

#Tuples:
print("\n")
print("-" * 50)
print()

person = ("Josh", 31, "Muscular")
print("A tuple is an ordered, immutable container that allows duplicates. "
      "\nThis is mine: ", person)
print()
print("The first element of my tuple is: ", person[0])
print("The second element of my tuple is: ", person[1])
print("The third element of my tuple is: ", person[2])
print("The length of my tuple is: ", len(person))
print("\n")
print("-" * 50)
print()

#Sets:

nums = {1, 2, 3, 4, 5}
print()
print("A set is an unordered, mutable container that does not allow duplicates. "
      "\nThis is my set: ", nums)
print()
print("The first element of my set is: ", list(nums)[0])  # Converting to list to access elements
print("The second element of my set is: ", list(nums)[1])  # Converting to list to access elements
print("The third element of my set is: ", list(nums)[2])  # Converting to list to access elements
print()
print("The length of my set is: ", len(nums))
print()
nums.add(6)
print("After adding a new element, we have: ", nums)  # After adding a new element
nums.discard(6)  # Removing the last element
print("After removing the last element, we have: ", nums)  # After removing the last element
nums.remove(1)  # Removing an element
print("After removing element '1', we have: ", nums)  # After removing an element
print()
print("The length of my set is now: ", len(nums))  # Length of the set after modifications
print("\n")
print("-" * 50) 
print()

#Dictionaries:
profile = {
    "Name": "Josh",
    "Age": 31,
    "Height": "6'2\"",
    "Weight": 225
}

print("A dictionary is an unordered, mutable container that does not allow duplicates. "
      "\nThis is my dictionary-based profile: ", profile)
print(profile["Name"])  # Accessing the value associated with the key "name"
print()
profile["Age"] = 32  # Accessing the value associated with the key "age"
profile["City"] = "Columbus"
print(f"My updated profile: {profile}")  # Accessing the value associated with the key "height"
print("The length of my dictionary is: ", len(profile))  # Length of the dictionary
print()
for key, value in profile.items():
    print(f"{key.title():<6} |  {value}")  # Iterating through the dictionary to print key-value pairs
print("\n")
print("-" * 50) 
print()