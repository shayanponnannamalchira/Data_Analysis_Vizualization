"""
Q14. Age and Fare Relationship
A researcher wants to determine whether older passengers generally paid higher fares.

Calculate the correlation between age and fare.
Interpret the strength and direction of the relationship.
"""
import seaborn as sns
import pandas as pd

df = sns.load_dataset("titanic")

corr = df["age"].corr(df["fare"])
print(f"Correlation between age and fare: {corr:.3f}")

print("\nInterpretation: The correlation is close to zero (weak positive), meaning there is")
print("little to no linear relationship between a passenger's age and the fare they paid.")
print("Older passengers did not generally pay noticeably higher fares.")
