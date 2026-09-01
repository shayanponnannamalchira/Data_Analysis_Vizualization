"""
U4 Q1. Missing Data - Titanic Dataset
Some passenger records have missing values.

a) Identify the number of missing values in each column.
b) Fill the missing values in the Age column using an appropriate statistical value.
c) Remove rows where the Embarked value is missing using dropna().
"""
import seaborn as sns

df = sns.load_dataset("titanic")

# a
print("a) Missing values per column:")
print(df.isnull().sum())

# b
df["age"] = df["age"].fillna(df["age"].median())
print(f"\nb) Missing Age values after fillna(median): {df['age'].isnull().sum()}")

# c
print(f"\nRows before dropping missing Embarked: {len(df)}")
df = df.dropna(subset=["embarked"])
print(f"c) Rows after dropping missing Embarked: {len(df)}")
