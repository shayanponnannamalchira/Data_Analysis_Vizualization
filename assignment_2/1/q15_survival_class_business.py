"""
Q15. Survival and Passenger Class - Business Question
A travel company is studying historical passenger data and asks:
"Was passenger class associated with the likelihood of survival?"

Perform an EDA using class, sex, age, fare, and survived. Use appropriate
statistical summaries, cross-tabulations, and visualizations to investigate
the question. Present at least three findings from your analysis.
"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

print("Descriptive statistics for age and fare:")
print(df[["age", "fare"]].describe())

print("\nSurvival rate by class:")
print(df.groupby("class")["survived"].mean().round(3))

print("\nSurvival rate by class and sex:")
print(df.groupby(["class", "sex"])["survived"].mean().round(3))

print("\nAverage fare by class:")
print(df.groupby("class")["fare"].mean().round(2))

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
df.groupby("class")["survived"].mean().plot(kind="bar", ax=axes[0], color="#4c72b0")
axes[0].set_title("Survival Rate by Class")
axes[0].set_ylabel("Survival Rate")

sns.boxplot(data=df, x="class", y="fare", ax=axes[1])
axes[1].set_title("Fare Distribution by Class")
plt.tight_layout()
plt.savefig("q15_class_survival_fare.png")

print("""
Findings:
1. First-class passengers had a much higher survival rate than second or third class.
2. Within every class, women survived at a higher rate than men - sex and class both matter.
3. First-class passengers paid substantially higher fares on average, and fare is strongly
   linked to class, so class (and the resources/deck location it implies) is associated
   with survival likelihood.
""")
