# Reclaiming momentum – Day 1 – [5/24/2025]

x= 10
print(x)
name = "Joshua"
print(name)
my_list = [1,2,3]
print()
print(my_list)
print()
for item in my_list:
    print(item)
print()
def greet(name):
    return f"Hello, {name}!"

print(greet(name), "Welcome to Python programming!\nThis is the start of The Primer 2.9")
print("-------------------------------------------------------------")

player_name = "Ronald Acuna Jr"
hits = 3
at_bats = 4

print (f"{player_name} went {hits}/ {at_bats} in the game.")

batting_avg = hits/at_bats
print(f"Batting Average: {batting_avg:.3f}")

runs_scored = 2
print("Runs + Hits: ", runs_scored + hits)
print()
print("The following stats are not relevant to actual baseball stats.\n")
print("Hits squared:", hits**2)
print("Hit remainder when divided by 2:", hits % 2)
print()

def print_stat_chart(player_name, hits, at_bats, runs, rbi):
    batting_avg = hits / at_bats if at_bats > 0 else 0
    print("\n==============Player Stats==============")
    print(f"{'Player Name:':<18} {player_name}")
    print(f"{'Hits:':<18} {hits}")
    print(f"{'At Bats:':<18} {at_bats}")
    print(f"{'Runs:':<18} {runs}")
    print(f"{'RBI:':<18} {rbi}")
    print(f"{'Batting Average:':<18} {batting_avg:.3f}")
    print("=========================================")

print_stat_chart("Ronald Acuna Jr", hits=3, at_bats=4, runs=2, rbi=1)
print()
print()
print("-------------------------------------------------------------")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Player': ['Ronald Acuna Jr', 'Ozzie Albies', 'Austin Riley'],
    'Hits': [3, 2, 1],
    'At Bats': [4, 4, 4],
    'Runs': [2, 1, 0],
    'RBI': [1, 0, 0],
    'Batting Average': [f'{hits/at_bats:.3f}' for hits, at_bats in zip([3, 2, 1], [4, 4, 4])]
}

df = pd.DataFrame(data)
print(df)
print("-------------------------------------------------------------")
print()

print()

name1 = "Rose"
age = "32"
is_student = False

#Lists and Loop
expenses = [15.99, 45.00, 23.50]
for cost in expenses: 
    print(f"Spent: ${cost}")

#function
def greeting(user1):
    return f"Hello, {user1}! Welcome to your PRIME!"

print(greeting(name1))

target_run = {
    "toothbrush": 15.99,
    "phone case": 45.00,
    "socks": 23.50,
}

print()
df = pd.DataFrame(list(target_run.items()), columns=['Item', 'Price'])
print(df)
print("-------------------------------------------------------------")