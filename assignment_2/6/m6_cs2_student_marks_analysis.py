"""
Module 6, Case Study 2: Analysis of Student Marks
Marks obtained by 80 students in Mathematics are recorded.

a) Identify the most suitable distribution plot to visualize the marks.
b) Explain how a box plot helps in understanding this data.
c) Write a Seaborn program to draw: Histogram, Box plot.
d) State two conclusions that can be drawn from these plots.
"""
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

print("""
a) A Histogram (sns.histplot), optionally with a KDE overlay, is the most suitable
   distribution plot to visualize how 80 students' marks are spread out.

b) A box plot helps by summarizing the data through five key statistics (minimum, Q1,
   median, Q3, maximum) in one compact visual, making it easy to see the central tendency,
   spread, skewness, and any outliers beyond the whiskers - all at a glance.
""")

np.random.seed(2)
marks = np.clip(np.random.normal(68, 12, 80), 0, 100)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.histplot(marks, bins=15, kde=True, color="#4c72b0", ax=axes[0])
axes[0].set_title("Histogram of Mathematics Marks")

sns.boxplot(y=marks, color="#dd8452", ax=axes[1])
axes[1].set_title("Box Plot of Mathematics Marks")

plt.tight_layout()
plt.savefig("m6_cs2_student_marks.png")
print("Saved plots to m6_cs2_student_marks.png")

print(f"""
d) Conclusions:
1. The marks appear to be approximately normally distributed around a mean of about
   {marks.mean():.1f}, with most students scoring within one standard deviation of the mean.
2. The box plot shows whether there are any outlier students scoring unusually high or low
   compared to their peers, which can be useful for identifying students needing support
   or recognition.
""")
