#Reminder > 

"""
Lists store and access sequences of data.
Dictionaries store key-value pairs, good for categorized data.
Tuples are immutable sequences, useful for fixed collections of items.
Sets store unique items, useful for membership tests and removing duplicates.
Functions are reusable blocks of code that perform specific tasks.

"""

#We will upgrade the Budget Tracker today to include more features and functionality.

def add_expenses(expenses_dictionary):
    item = input("Enter the expense (or 'done' to finish): ")
    if item.lower() == 'done':
        return False
    
    category = input("Enter the expense category: ")
    amount = float(input("Enter amount: $"))

    if category not in expenses_dictionary:
        expenses_dictionary[category] = []

    expenses_dictionary[category].append((item, amount))
    return True 

def calculate_total(expenses_dict):
    total = 0
    for entries in expenses_dict.values():
        total += sum(amount for _, amount in entries)
    return total

def print_summary(expenses_dict):
    print("\n -- Expense Report by Category --")
    for category, entries in expenses_dict.items():
        print(f"\n{category.capitalize()}:")
        for item, amount in entries:
            print(f" {item}: ${amount:.2f}")
    print(f"\nTotal Spent: ${calculate_total(expenses_dict):.2f}")




def print_table(expenses_dict):
    print("\n -- Expense Table --")
    print(f"{'Category':<15} {'Item':<20} {'Amount ($)':>10}")
    print("-" *50)
    for category, entries in expenses_dict.items():
        for item, amount in entries:
            print(f"{category:<15} {item:<20} ${amount:>10.2f}")
    print("-" *50)
    total = calculate_total(expenses_dict)
    print(f"{'Total' :<35} ${total:>10.2f}")

expenses = {}
while add_expenses(expenses):
    continue
print_summary(expenses)
print_table(expenses)
print("\nHere's how things are looking mate...")