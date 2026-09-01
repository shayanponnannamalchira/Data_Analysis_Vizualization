"""
U4 Q7. Duplicate and Data Quality Check - Employee Dataset
An HR department has received an employee dataset with repeated records and
inconsistent department names such as CSE, cse, and Cse.

a) Identify duplicate employee records and display their count.
b) Remove the duplicate records.
c) Standardize the Department column so CSE/cse/Cse are treated consistently.
d) Verify that the cleaned dataset contains no duplicates.
"""
import pandas as pd

df = pd.DataFrame({
    "Employee_ID": ["E1", "E2", "E3", "E2", "E4"],
    "Department": ["CSE", "cse", "ECE", "cse", "Cse"],
    "Salary": [50000, 55000, 48000, 55000, 52000],
})

# a
dup_count = df.duplicated().sum()
print(f"a) Number of duplicate records: {dup_count}")

# b
df = df.drop_duplicates()
print("\nb) After removing duplicates:")
print(df)

# c
df["Department"] = df["Department"].str.upper().str.strip()
print("\nc) Standardized Department column:")
print(df)

# d
print(f"\nd) Duplicates remaining: {df.duplicated().sum()}")
