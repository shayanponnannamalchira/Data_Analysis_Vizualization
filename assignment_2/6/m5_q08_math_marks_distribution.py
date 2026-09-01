"""
Module 5, Q8. A dataset contains students' marks in Mathematics collected
from 100 students. Which type of graph will you use to show the distribution
of marks? Explain why this graph is suitable. Mention how you will customize
the graph for better understanding.
"""
import numpy as np
import matplotlib.pyplot as plt

print("""
Recommended graph: Histogram (optionally paired with a box plot).

Why it's suitable: A histogram groups continuous numeric marks into bins and shows how
many students fall into each range, revealing the overall shape of the distribution
(e.g., normal, skewed, bimodal), central tendency, and spread - which is exactly what's
needed to understand how 100 students' marks are distributed.

Customizations for better understanding:
- Choose an appropriate number of bins (not too few/many) to reveal the true shape.
- Add a title ("Distribution of Mathematics Marks") and axis labels (Marks, Number of
  Students).
- Overlay a KDE (density curve) to smooth out the shape.
- Add gridlines and a vertical line marking the mean/median for quick reference.
- Use a clear, single color with light edge lines on bars for readability.
""")

np.random.seed(1)
marks = np.clip(np.random.normal(65, 15, 100), 0, 100)

plt.figure(figsize=(7, 5))
plt.hist(marks, bins=12, color="#4c72b0", edgecolor="black", alpha=0.8)
plt.axvline(marks.mean(), color="red", linestyle="--", label=f"Mean = {marks.mean():.1f}")
plt.title("Distribution of Mathematics Marks (100 Students)")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig("m5_q08_math_marks_distribution.png")
print("Saved histogram to m5_q08_math_marks_distribution.png")
