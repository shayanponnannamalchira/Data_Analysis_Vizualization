"""
Module 6, Case Study 3: Comparing Performance of Two Groups
A teacher wants to compare the marks of boys and girls in Science.

a) Which Seaborn plot is best to compare the distribution of marks?
b) Why is this plot better than a box plot in this case?
c) Write a Seaborn program to create this visualization.
d) Mention two observations from the graph.
"""
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("""
a) A Violin Plot (sns.violinplot) is well suited for comparing the distribution of marks
   between boys and girls.

b) A violin plot is better than a plain box plot here because it shows the full shape/
   density of the distribution (e.g., whether marks are bimodal, skewed, or concentrated)
   for each group, in addition to the summary statistics a box plot alone provides -
   giving a richer comparison between the two groups.
""")

np.random.seed(3)
boys = np.random.normal(65, 10, 50)
girls = np.random.normal(72, 8, 50)
df = pd.DataFrame({
    "Marks": np.concatenate([boys, girls]),
    "Gender": ["Boys"] * 50 + ["Girls"] * 50,
})

plt.figure(figsize=(7, 5))
sns.violinplot(data=df, x="Gender", y="Marks", palette="Set2")
plt.title("Distribution of Science Marks: Boys vs Girls")
plt.tight_layout()
plt.savefig("m6_cs3_boys_vs_girls.png")
print("Saved violin plot to m6_cs3_boys_vs_girls.png")

print(f"""
d) Observations:
1. Girls' median marks ({np.median(girls):.1f}) are higher than boys' median marks
   ({np.median(boys):.1f}) in this sample.
2. The spread (variability) of marks differs between the two groups - one group's
   distribution is visibly wider/narrower than the other's, indicating more/less
   consistency in performance.
""")
