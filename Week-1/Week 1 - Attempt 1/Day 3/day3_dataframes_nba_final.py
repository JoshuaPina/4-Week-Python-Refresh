#Final Version of my Day 3 pandas application, I used NBA Playoff data.
#Some minor Matplotlib application to show the data.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Load the NBA playoff data

df = pd.read_csv('/Users/joshuapina/Library/CloudStorage/OneDrive-GeorgiaStateUniversity/' \
'4-Week-Python-Refresh/Week 1/Day 3/NBA_2025_Playoffs_Top10.csv')

print(df.describe())
print()
print("Lets clean this up just a little bit")
print(df.describe().round(2))
print()

pd.set_option("display.max_columns", None)     # Show all columns
pd.set_option("display.float_format", "{:.2f}".format)  # Format floats nicely
pd.set_option("display.max_rows", 100)         # Show more rows
print(df.describe().round(2))
print()
df.info()
print()

top10 = df.sort_values("PTS", ascending=True).head(10)
top10.plot(x="Player", y="PTS", kind="barh", figsize=(10, 6), color="skyblue")
# Sort by Team alphabetically
df.sort_values("Team", inplace=True)

# Sort by Position
df.sort_values("POS", inplace=True)

# Sort by Total Points scored, descending
df.sort_values("PTS", ascending=False, inplace=True)

# Filter for Point Guards
pg_only = df[df["POS"] == "PG"]

# Filter for players with at least 20 PPG
over_20_ppg = df[df["PTS"] / df["GP"] >= 20]
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Top 10 scorers by total points
top10 = df.sort_values("PTS", ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(data=top10, x="PTS", y="Player", palette="coolwarm_r")
plt.title("Top 10 Scorers by PPG - 2025 NBA Playoffs ")
plt.xlabel("PPG")
plt.ylabel("Player")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
barplot = sns.barplot(data=top10, x="PTS", y="Player", palette="coolwarm_r")
for index, value in enumerate(top10["PTS"]):
    barplot.text(value + 0.5, index, f"{value:.1f}", va='center')
plt.tight_layout()
plt.show()
