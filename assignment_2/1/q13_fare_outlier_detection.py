"""
Q13. Fare Outlier Detection
A data analyst wants to identify passengers who paid unusually high fares.

Use the IQR method to identify outliers in the fare column.
Display the passenger records corresponding to the detected outliers.
"""
import seaborn as sns
import pandas as pd

df = sns.load_dataset("titanic")

Q1 = df["fare"].quantile(0.25)
Q3 = df["fare"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["fare"] < lower_bound) | (df["fare"] > upper_bound)]

print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
print(f"Lower bound: {lower_bound}, Upper bound: {upper_bound}")
print(f"Number of fare outliers: {len(outliers)}")
print(outliers[["sex", "age", "class", "fare", "survived"]].head(20))
