"""
U4 Q8. Renaming Columns - Sales Dataset
A retail company has received a sales DataFrame with unclear column names
such as cust_id, prod, qty, and amt.

a) Rename the columns as Customer_ID, Product, Quantity, and Amount.
b) Display only the Product, Quantity, and Amount columns.
c) Sort the records based on Amount from highest to lowest.
"""
import pandas as pd

df = pd.DataFrame({
    "cust_id": [1, 2, 3, 4],
    "prod": ["Pen", "Notebook", "Bag", "Pencil"],
    "qty": [10, 5, 2, 20],
    "amt": [100, 250, 800, 60],
})

# a
df = df.rename(columns={"cust_id": "Customer_ID", "prod": "Product", "qty": "Quantity", "amt": "Amount"})
print("a) Renamed DataFrame:")
print(df)

# b
print("\nb) Product, Quantity, Amount columns only:")
print(df[["Product", "Quantity", "Amount"]])

# c
sorted_df = df.sort_values("Amount", ascending=False)
print("\nc) Sorted by Amount (highest to lowest):")
print(sorted_df)
