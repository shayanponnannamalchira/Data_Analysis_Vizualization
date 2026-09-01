"""
U3 Q6 - Comprehensive 10-Mark Question: Retail Sales Transactions
You are a Data Analyst for a retail company with customer transaction data
containing Customer_ID, Customer_Name, Gender, Category, Quantity,
Unit_Price, Payment_Method. The data must be cleaned and transformed.

1. Identify and display missing values.
2. Handle missing values using dropna/fillna, justify the choice.
3. Remove duplicate customer transaction records.
4. Filter transactions where Quantity > 2, sort by Unit_Price.
5. Rename Unit_Price -> Price and Payment_Method -> Payment.
6. Create Total_Amount = Quantity * Price.
7. Encode Gender into numerical values.
8. Group by Category, calculate total sales and average sales.
9. Perform a final data-quality check.
"""
import pandas as pd
import numpy as np

sales = pd.DataFrame({
    "Customer_ID": [1, 2, 3, 4, 5, 5, 6],
    "Customer_Name": ["A", "B", "C", "D", "E", "E", "F"],
    "Gender": ["Male", "Female", "Female", "Male", np.nan, np.nan, "Male"],
    "Category": ["Electronics", "Furniture", "Electronics", "Furniture", "Electronics", "Electronics", "Furniture"],
    "Quantity": [3, 1, 5, 2, 4, 4, 3],
    "Unit_Price": [1500, 8000, 200, 12000, 25000, 25000, 500],
    "Payment_Method": ["Card", "UPI", "Cash", "Card", "UPI", "UPI", np.nan],
})

# 1. Missing values
print("Missing values per column:")
print(sales.isnull().sum())

# 2. Handle missing values
# Gender: categorical, fill with mode; Payment_Method: fill with mode.
# Justification: dropping rows would lose otherwise-valid transaction data,
# so mode-fill is preferred for these low-missing categorical columns.
sales["Gender"] = sales["Gender"].fillna(sales["Gender"].mode()[0])
sales["Payment_Method"] = sales["Payment_Method"].fillna(sales["Payment_Method"].mode()[0])

# 3. Duplicates
print(f"\nDuplicate records: {sales.duplicated().sum()}")
sales = sales.drop_duplicates()

# 4. Filter and sort
filtered = sales[sales["Quantity"] > 2].sort_values("Unit_Price")
print("\nTransactions with Quantity > 2, sorted by Unit_Price:")
print(filtered)

# 5. Rename
sales = sales.rename(columns={"Unit_Price": "Price", "Payment_Method": "Payment"})

# 6. Total_Amount
sales["Total_Amount"] = sales["Quantity"] * sales["Price"]

# 7. Encode Gender
sales["Gender_encoded"] = sales["Gender"].map({"Male": 0, "Female": 1})

# 8. Group by category
print("\nTotal and average sales by category:")
print(sales.groupby("Category")["Total_Amount"].agg(["sum", "mean"]))

# 9. Final data-quality check
print(f"\nRemaining missing values: {sales.isnull().sum().sum()}")
print(f"Remaining duplicates: {sales.duplicated().sum()}")
print(f"Unique categorical values check - Gender: {sales['Gender'].unique()}")
