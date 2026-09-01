"""
Q9. Passenger Age Analysis
A historian wants to understand the age distribution of passengers on the Titanic.

Calculate the mean, median, and mode of passenger age.
Which measure would you use to represent the typical passenger age, and why?
"""
import seaborn as sns
import pandas as pd

df = sns.load_dataset("titanic")

mean_age = df["age"].mean()
median_age = df["age"].median()
mode_age = df["age"].mode()[0]

print(f"Mean age  : {mean_age:.2f}")
print(f"Median age: {median_age:.2f}")
print(f"Mode age  : {mode_age:.2f}")

print("\nInterpretation: Age has missing values and some skew from a long right tail (a few")
print("elderly passengers), so the median is the better representative of a 'typical'")
print("passenger age since it is less affected by outliers/skew than the mean.")
