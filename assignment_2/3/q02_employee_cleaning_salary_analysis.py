"""
U3 Q2 - Employee Dataset: Data Cleaning and Salary Analysis
An organization maintains an employee dataset containing Employee_ID,
Department, Gender, Age, Salary, and Experience with missing values and
duplicate entries.

Using Pandas:
1. Identify missing values and display the count per column.
2. Fill missing Age with mean age, missing Salary with median salary.
3. Fill missing Experience using an appropriate statistical value.
4. Remove duplicate employee records.
5. Filter employees with salary > 50,000, sorted descending.
6. Group by Department, calculate average salary and average experience.
7. Create Salary_Per_Year_Experience = Salary / Experience.
8. Encode Gender as numerical values.
9. Rename Employee_ID as Emp_ID.
"""
import pandas as pd
import numpy as np

data = {
    "Employee_ID": ["E101", "E102", "E103", "E104", "E105", "E106", "E105"],
    "Department": ["IT", "HR", "IT", "Sales", "IT", "HR", "IT"],
    "Gender": ["Male", "Female", "Female", "Male", "Male", "Female", "Male"],
    "Age": [25, 29, np.nan, 35, 31, 28, 31],
    "Salary": [45000, 52000, 60000, np.nan, 58000, 50000, 58000],
    "Experience": [2, 4, 5, 8, 6, np.nan, 6],
}
df = pd.DataFrame(data)

# 1. Missing values
print("Missing values per column:")
print(df.isnull().sum())

# 2 & 3. Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df["Experience"] = df["Experience"].fillna(df["Experience"].median())

# 4. Remove duplicates
print(f"\nDuplicate records: {df.duplicated().sum()}")
df = df.drop_duplicates()

# 5. Filter and sort
high_earners = df[df["Salary"] > 50000].sort_values("Salary", ascending=False)
print("\nEmployees with salary > 50,000 (sorted desc):")
print(high_earners)

# 6. Group by department
print("\nAverage salary and experience by department:")
print(df.groupby("Department")[["Salary", "Experience"]].mean())

# 7. New feature
df["Salary_Per_Year_Experience"] = df["Salary"] / df["Experience"]

# 8. Encode Gender
df["Gender_encoded"] = df["Gender"].map({"Male": 0, "Female": 1})

# 9. Rename
df = df.rename(columns={"Employee_ID": "Emp_ID"})

print("\nFinal cleaned dataset:")
print(df)
