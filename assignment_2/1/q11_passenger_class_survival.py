"""
Q11. Passenger Class and Survival
A researcher asks: "Did passenger class influence survival?"

Create a cross-tabulation between class and survived. Calculate the survival
percentage for each passenger class and interpret the results.
"""
import seaborn as sns
import pandas as pd

df = sns.load_dataset("titanic")

cross_tab = pd.crosstab(df["class"], df["survived"])
print("Cross-tabulation of class vs survived:")
print(cross_tab)

survival_pct = pd.crosstab(df["class"], df["survived"], normalize="index") * 100
print("\nSurvival percentage by class:")
print(survival_pct.round(2))

print("\nInterpretation: First-class passengers had the highest survival rate, followed by")
print("second class, with third class having the lowest survival rate - suggesting passenger")
print("class was strongly associated with likelihood of survival.")
