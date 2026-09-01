"""
U3 Q1 - Titanic Dataset: Passenger Data Cleaning and Transformation
A travel analytics company wants to analyze passenger information from the
Titanic dataset. Using Pandas, perform the following operations:
1. Load the Titanic dataset, display basic info, identify missing values per
   column, and handle missing values in Age and Embarked using fillna.
2. Filter passengers in 1st class with fare > 50, sort by fare descending,
   and rename sex, age, fare to Gender, Age, Ticket_Fare.
3. Group by passenger class and calculate average age and average fare.
4. Create FamilySize = sibsp + parch + 1.
5. Identify and remove duplicate records.
6. Encode the categorical column sex into numerical values.
"""
import seaborn as sns
import pandas as pd

df = sns.load_dataset("titanic")

# 1. Basic info & missing values
print("Basic info:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

df["age"] = df["age"].fillna(df["age"].median())
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])

# 2. Filter, sort, rename
filtered = df[(df["pclass"] == 1) & (df["fare"] > 50)].sort_values("fare", ascending=False)
filtered = filtered.rename(columns={"sex": "Gender", "age": "Age", "fare": "Ticket_Fare"})
print("\nFiltered 1st class, fare > 50, sorted by fare desc:")
print(filtered[["Gender", "Age", "Ticket_Fare"]].head())

# 3. Group by class
print("\nAverage age and fare by class:")
print(df.groupby("pclass")[["age", "fare"]].mean())

# 4. FamilySize
df["FamilySize"] = df["sibsp"] + df["parch"] + 1
print("\nFamilySize sample:")
print(df[["sibsp", "parch", "FamilySize"]].head())

# 5. Duplicates
print(f"\nDuplicate records: {df.duplicated().sum()}")
df = df.drop_duplicates()

# 6. Encode sex
df["sex_encoded"] = df["sex"].map({"male": 0, "female": 1})
print("\nEncoded sex sample:")
print(df[["sex", "sex_encoded"]].head())
