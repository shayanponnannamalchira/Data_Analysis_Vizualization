"""
U4 Q9. Concatenating Data - Monthly Sales
A company maintains sales data separately for January and February.

a) Combine both DataFrames vertically using concat().
b) Reset the index of the combined DataFrame.
c) Display the total number of sales transactions after combining.
"""
import pandas as pd

jan_sales = pd.DataFrame({
    "Transaction_ID": [1, 2, 3],
    "Amount": [1000, 1500, 2000],
})

feb_sales = pd.DataFrame({
    "Transaction_ID": [4, 5],
    "Amount": [1200, 1800],
})

# a
combined = pd.concat([jan_sales, feb_sales])
print("a) Combined (vertical concat):")
print(combined)

# b
combined = combined.reset_index(drop=True)
print("\nb) After resetting index:")
print(combined)

# c
print(f"\nc) Total number of sales transactions: {len(combined)}")
