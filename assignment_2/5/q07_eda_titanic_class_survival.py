"""
U3&U4 Stats Q7. EDA Using Titanic Dataset
"Did passengers in higher classes have a better survival rate?"

a) Calculate the survival rate for each passenger class using Pandas.
b) Identify the class having the highest survival rate.
c) Give a one-line interpretation of the finding.
"""
import seaborn as sns

df = sns.load_dataset("titanic")

# a
survival_rate = df.groupby("class", observed=True)["survived"].mean()
print("a) Survival rate by class:")
print(survival_rate)

# b
best_class = survival_rate.idxmax()
print(f"\nb) Class with the highest survival rate: {best_class}")

# c
print(f"\nc) Interpretation: Passengers in {best_class} class had the best chance of survival,")
print("   supporting the idea that higher passenger class was associated with better survival.")
