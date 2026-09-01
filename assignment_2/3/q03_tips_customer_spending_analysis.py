"""
U3 Q3 - Restaurant Tips Dataset: Customer Spending Analysis
A restaurant wants to understand customer spending patterns using the Tips
dataset available through Seaborn.

1. Load Tips dataset, identify rows, columns, and missing values.
2. Handle missing values with dropna/fillna if present.
3. Filter customers with total_bill > $30, sorted descending.
4. Group by day, calculate total bill, average bill, and average tip.
5. Create Tip_Percentage = tip / total_bill * 100.
6. Encode sex and smoker categorical columns numerically.
7. Check for and remove duplicate records.
8. Rename total_bill and tip to Total_Bill and Tip.
"""
import seaborn as sns
import pandas as pd

df = sns.load_dataset("tips")

# 1. Rows, columns, missing values
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print("\nMissing values:")
print(df.isnull().sum())

# 2. Handle missing values (none expected in this dataset, but code is defensive)
df = df.dropna()

# 3. Filter and sort
big_bills = df[df["total_bill"] > 30].sort_values("total_bill", ascending=False)
print("\nCustomers with total_bill > $30 (sorted desc):")
print(big_bills.head())

# 4. Group by day
print("\nTotal bill, average bill, average tip by day:")
print(df.groupby("day", observed=True).agg(
    total_bill_sum=("total_bill", "sum"),
    avg_bill=("total_bill", "mean"),
    avg_tip=("tip", "mean"),
))

# 5. Tip percentage
df["Tip_Percentage"] = df["tip"] / df["total_bill"] * 100

# 6. Encode categorical columns
df["sex_encoded"] = df["sex"].map({"Male": 0, "Female": 1})
df["smoker_encoded"] = df["smoker"].map({"No": 0, "Yes": 1})

# 7. Duplicates
print(f"\nDuplicate records: {df.duplicated().sum()}")
df = df.drop_duplicates()

# 8. Rename
df = df.rename(columns={"total_bill": "Total_Bill", "tip": "Tip"})

print("\nFinal dataset sample:")
print(df.head())
