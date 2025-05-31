import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("Week 1/Day 3/NBA_2025_Playoff_Top50_FULL.csv")
# DataFrame operations
#Additional Operations -
#df["Amount"] = df["Amount"].astype(float) - Fix column types
#df.groupby("Category")["Amount"].sum()
#df["Amount"].mean()
# df["Amount"].plot(kind="bar")

df.head()         # First 5 rows
df.tail()         # Last 5 rows
        # Column types + nulls
   # Stats summary
df.columns = df.columns.str.strip()  # Remove leading/trailing whitespace
df.dropna()                          # Drop missing values
df.fillna(0)                         # Replace nulls with 0

df.info() 
print()
print(df.head())  # Display first 5 rows of the DataFrame
print()
print(df.tail())  # Display last 5 rows of the DataFrame
print()
print(df.describe())
print()
print("Lets clean this up just a little bit")
print(df.describe().round(2))  # Round the summary statistics to 3 decimal places
print()

#Plotting the dataset

top10 = df.sort_values(by="PPG", ascending=False).head(10)
top10.plot(x="Player", y="PPG", kind="bar", legend=False)
plt.title("Top 10 NBA Players by Points Per Game (PPG)")
plt.xlabel("Player")
plt.ylabel("Points Per Game (PPG)")
plt.xticks(rotation=45) # Rotate x-axis labels for better readability

print("Here are the top 10 scorers this postseason:\n ", top10)
print()
top10rbd = df.sort_values(by = "RPG", ascending=False).head(10)
print("Here are the top 10 rebounders this postseason: \n", top10rbd)
print()
top10ast = df.sort_values(by = "APG", ascending=False).head(10)
print("Here are the top 10 assist leaders this postseason: \n", top10ast)
plt.show()  # Show the plot

top10 = df.sort_values(by="PPG", ascending=False).head(10)

# Plot
plt.figure(figsize=(12, 6))
plt.bar(top10["Player"], top10["PPG"], color="skyblue")
plt.title("Top 10 NBA Playoff Scorers - 2025", fontsize=16)
plt.xlabel("Player")
plt.ylabel("Points Per Game (PPG)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.grid(axis="y", linestyle="--", alpha=0.5)

# Show the plot
plt.show()