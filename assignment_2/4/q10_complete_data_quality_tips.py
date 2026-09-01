"""
U4 Q10. Complete Data Quality Check - Tips Dataset
Before performing customer spending analysis, a restaurant wants to ensure
its dataset is reliable.

a) Check whether the dataset contains missing values.
b) Check for duplicate records.
c) Check whether total_bill and tip contain valid positive values.
d) Display the cleaned dataset after performing the necessary corrections.
"""
import seaborn as sns

df = sns.load_dataset("tips")

# a
print("a) Missing values per column:")
print(df.isnull().sum())

# b
print(f"\nb) Duplicate records: {df.duplicated().sum()}")
df = df.drop_duplicates()

# c
invalid_bill = (df["total_bill"] <= 0).sum()
invalid_tip = (df["tip"] <= 0).sum()
print(f"\nc) Invalid (non-positive) total_bill values: {invalid_bill}")
print(f"   Invalid (non-positive) tip values: {invalid_tip}")

df = df[(df["total_bill"] > 0) & (df["tip"] > 0)]

# d
print("\nd) Cleaned dataset sample:")
print(df.head())
print(f"Final shape: {df.shape}")
