"""
Module 5, Q6. Explain the difference between Bar chart and Histogram. Write
at least five differences and give one example for each.
"""
import matplotlib.pyplot as plt
import numpy as np

print("""
Differences between Bar Chart and Histogram:

1. Data type:
   Bar chart - used for categorical (discrete) data.
   Histogram - used for continuous numerical data.

2. Spacing between bars:
   Bar chart - bars are separated by gaps.
   Histogram - bars (bins) are adjacent with no gaps, showing continuity.

3. What the bars represent:
   Bar chart - each bar represents a distinct category.
   Histogram - each bar represents a range/bin of values.

4. Order of bars:
   Bar chart - order can be rearranged freely (e.g., alphabetical, by value).
   Histogram - order is fixed since it follows the numeric range of the data.

5. Purpose:
   Bar chart - compares quantities across categories.
   Histogram - shows the distribution/shape (skew, spread) of a numeric variable.

Example - Bar chart: Number of students choosing Math, Science, English, Computer Science.
Example - Histogram: Distribution of exam scores of 100 students.
""")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
subjects = ["Math", "Science", "English", "CS"]
counts = [30, 25, 20, 25]
axes[0].bar(subjects, counts, color="#4c72b0")
axes[0].set_title("Bar Chart: Subject Choice")

scores = np.random.normal(70, 10, 100)
axes[1].hist(scores, bins=15, color="#dd8452", edgecolor="black")
axes[1].set_title("Histogram: Exam Score Distribution")
plt.tight_layout()
plt.savefig("m5_q06_bar_vs_histogram.png")
print("Saved comparison chart to m5_q06_bar_vs_histogram.png")
