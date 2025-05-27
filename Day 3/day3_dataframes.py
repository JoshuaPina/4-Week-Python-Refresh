#How to create a DataFrame

import pandas as pd

data = {
    "Data": ["2025-05-26", "2025-05-27"],
    "Vendor": ["Kroger", "Netflix"],
    "Amount": [-75.90, -15.99],
    "Category": ["Groceries", "Subscription"]

}

df = pd.DataFrame(data)
print()
print("=" * 50)
print(df)
print("=" * 50)
print()

try:
    df = pd.read_csv("testing_table.csv")
    print(df)
except FileNotFoundError:
    print("CSV file not found. Check the path!")