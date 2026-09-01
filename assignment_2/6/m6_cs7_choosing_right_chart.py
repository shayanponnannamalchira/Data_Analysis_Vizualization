"""
Module 6, Case Study 7: Choosing the Right Chart
A dataset contains:
- Type of transport used by students (Bus, Cycle, Walk, Car)
- Marks obtained by students
- Height and weight of students

a) Match each data type with the correct Seaborn visualization.
b) Justify each choice.
c) Write a Seaborn program to plot any one of the selected visualizations.
d) Explain the importance of choosing the correct chart.
"""
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("""
a) & b) Matching data types to visualizations:

1. Type of transport (categorical) -> Count Plot (sns.countplot)
   Justification: shows the frequency of each transport category, ideal for comparing
   how many students use each mode of transport.

2. Marks obtained by students (single numeric variable) -> Histogram / KDE plot
   (sns.histplot)
   Justification: shows the distribution/shape of the marks across all students.

3. Height and weight of students (two numeric variables) -> Scatter Plot (sns.scatterplot)
   Justification: shows the relationship/correlation between two continuous variables like
   height and weight.
""")

# c - example: count plot for transport type
np.random.seed(6)
transport = np.random.choice(["Bus", "Cycle", "Walk", "Car"], 60, p=[0.4, 0.2, 0.25, 0.15])
df = pd.DataFrame({"Transport": transport})

plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Transport", order=df["Transport"].value_counts().index, palette="pastel")
plt.title("Mode of Transport Used by Students")
plt.xlabel("Transport Type")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("m6_cs7_transport_countplot.png")
print("Saved count plot to m6_cs7_transport_countplot.png")

print("""
d) Importance of choosing the correct chart: The right chart accurately conveys the
   nature of the data (categorical vs. continuous, single variable vs. relationship
   between variables) without misleading the viewer. An incorrect chart choice (e.g., a
   pie chart for continuous height/weight data) can obscure patterns, confuse the
   audience, or lead to wrong conclusions, whereas the correct chart makes insights clear,
   accurate, and quick to grasp.
""")
