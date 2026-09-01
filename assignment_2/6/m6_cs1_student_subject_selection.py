"""
Module 6, Case Study 1: Student Subject Selection
A school collects data about subjects chosen by students: Mathematics,
Science, English, Computer Science.

a) Which Seaborn plot will best represent the number of students choosing
   each subject?
b) Justify your choice of visualization.
c) Write a Seaborn program to plot this graph.
d) Mention two insights the school can gain from this visualization.
"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

print("""
a) A Count Plot (sns.countplot) / Bar Chart is best suited.

b) Justification: Subject choice is categorical data, and a count plot directly shows the
   frequency of each category as bars, making it easy to compare how many students chose
   each subject at a glance.
""")

# c
data = pd.DataFrame({
    "Subject": ["Mathematics", "Science", "English", "Computer Science"] * 1
    + ["Mathematics", "Science", "Mathematics", "Computer Science", "English", "Computer Science"]
})

plt.figure(figsize=(7, 5))
sns.countplot(data=data, x="Subject", order=data["Subject"].value_counts().index, palette="viridis")
plt.title("Number of Students Choosing Each Subject")
plt.xlabel("Subject")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("m6_cs1_subject_selection.png")
print("Saved count plot to m6_cs1_subject_selection.png")

print("""
d) Insights:
1. The school can identify which subjects are most and least popular, helping allocate
   teachers, classrooms, and resources accordingly.
2. Consistently low enrollment in a subject (e.g., Computer Science) could prompt the
   school to investigate reasons (awareness, perceived difficulty) and take corrective action.
""")
