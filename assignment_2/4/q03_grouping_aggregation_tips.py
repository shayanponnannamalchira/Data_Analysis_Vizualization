"""
U4 Q3. Grouping and Aggregation - Tips Dataset
A restaurant manager wants to compare customer spending across different days.

a) Group the records based on day.
b) Calculate the average total_bill for each day.
c) Calculate the maximum tip received on each day.
"""
import seaborn as sns

df = sns.load_dataset("tips")

# a & b
print("a & b) Average total_bill per day:")
print(df.groupby("day", observed=True)["total_bill"].mean())

# c
print("\nc) Maximum tip per day:")
print(df.groupby("day", observed=True)["tip"].max())
