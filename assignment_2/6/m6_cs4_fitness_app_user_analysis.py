"""
Module 6, Case Study 4: Fitness App User Analysis
A fitness app collects: Daily steps count, Calories burned, Gender of users.

a) Which plot will help show the distribution of steps taken?
b) Which plot can compare calories burned between genders?
c) Write a Seaborn program to plot both visualizations.
d) Explain how these plots help users improve fitness.
"""
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("""
a) A Histogram (sns.histplot) or KDE plot is best to show the distribution of daily
   steps taken across users.

b) A Box Plot (sns.boxplot) or Violin Plot can effectively compare calories burned
   between male and female users.
""")

np.random.seed(4)
n = 100
df = pd.DataFrame({
    "Steps": np.random.normal(7000, 1500, n).astype(int),
    "Calories": np.random.normal(300, 60, n),
    "Gender": np.random.choice(["Male", "Female"], n),
})

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.histplot(df["Steps"], bins=20, kde=True, color="#4c72b0", ax=axes[0])
axes[0].set_title("Distribution of Daily Steps")

sns.boxplot(data=df, x="Gender", y="Calories", palette="Set2", ax=axes[1])
axes[1].set_title("Calories Burned by Gender")

plt.tight_layout()
plt.savefig("m6_cs4_fitness_app.png")
print("Saved plots to m6_cs4_fitness_app.png")

print("""
d) These plots help users improve fitness by letting them see where they stand relative to
   typical activity levels (e.g., whether their step count is below the common range) and
   by revealing gender-based differences in calorie burn, which can guide more personalized
   and realistic fitness goals rather than generic targets.
""")
