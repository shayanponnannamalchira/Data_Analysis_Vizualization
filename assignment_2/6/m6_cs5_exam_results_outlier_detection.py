"""
Module 6, Case Study 5: Exam Results Outlier Detection
Marks of students in English are recorded.

a) Which Seaborn plot helps identify outliers clearly?
b) Explain how this plot shows outliers.
c) Write a Seaborn program to draw this plot.
d) Mention two actions a teacher can take after identifying outliers.
"""
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

print("""
a) A Box Plot (sns.boxplot) most clearly highlights outliers.

b) A box plot draws whiskers extending to 1.5 times the IQR beyond Q1 and Q3; any data
   points beyond these whiskers are plotted individually as distinct dots, making outliers
   immediately visible and easy to distinguish from the main bulk of the data.
""")

np.random.seed(5)
marks = np.concatenate([np.random.normal(70, 8, 45), [20, 25, 98, 99]])

plt.figure(figsize=(6, 5))
sns.boxplot(y=marks, color="#55a868")
plt.title("English Marks - Outlier Detection")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("m6_cs5_english_marks_outliers.png")
print("Saved box plot to m6_cs5_english_marks_outliers.png")

print("""
d) Actions a teacher can take:
1. Investigate very low-scoring outliers to identify students who may need extra academic
   support or who may have faced issues during the exam.
2. Recognize/encourage very high-scoring outliers, and separately verify that no data
   entry errors caused an implausible score before including it in official records.
""")
