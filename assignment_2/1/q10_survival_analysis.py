"""
Q10. Survival Analysis
A researcher wants to understand whether passenger survival differed between
males and females.

Create a cross-tabulation between sex and survived. Interpret the results.
"""
import seaborn as sns
import pandas as pd

df = sns.load_dataset("titanic")

cross_tab = pd.crosstab(df["sex"], df["survived"])
print("Cross-tabulation of sex vs survived:")
print(cross_tab)

cross_tab_pct = pd.crosstab(df["sex"], df["survived"], normalize="index") * 100
print("\nSurvival percentage by sex:")
print(cross_tab_pct.round(2))

print("\nInterpretation: A much higher percentage of female passengers survived compared to")
print("male passengers, consistent with the 'women and children first' evacuation policy.")
