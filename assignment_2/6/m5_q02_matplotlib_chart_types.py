"""
Module 5, Q2. What is Matplotlib? Explain any five types of charts available in
Matplotlib with suitable examples.
"""
import matplotlib.pyplot as plt
import numpy as np

print("""
Matplotlib is a widely used Python library for creating static, animated, and interactive
visualizations. It provides a flexible, low-level API (pyplot) for building a wide range
of chart types and is the foundation for many other visualization libraries (like Seaborn).

Five common chart types in Matplotlib:
1. Line chart  - plt.plot()      -> shows trends over a continuous variable (e.g., time).
2. Bar chart   - plt.bar()       -> compares quantities across discrete categories.
3. Histogram   - plt.hist()      -> shows the distribution of a single numerical variable.
4. Scatter plot- plt.scatter()   -> shows the relationship between two numerical variables.
5. Pie chart   - plt.pie()       -> shows proportion/percentage share of categories in a whole.
""")

x = np.arange(1, 6)
y = [10, 24, 18, 30, 22]

fig, axes = plt.subplots(2, 3, figsize=(15, 8))
axes[0, 0].plot(x, y, marker="o"); axes[0, 0].set_title("Line Chart")
axes[0, 1].bar(x, y, color="#4c72b0"); axes[0, 1].set_title("Bar Chart")
axes[0, 2].hist(np.random.normal(50, 10, 200), bins=20); axes[0, 2].set_title("Histogram")
axes[1, 0].scatter(x, y); axes[1, 0].set_title("Scatter Plot")
axes[1, 1].pie(y, labels=[f"Cat{i}" for i in x], autopct="%1.1f%%"); axes[1, 1].set_title("Pie Chart")
axes[1, 2].axis("off")
plt.tight_layout()
plt.savefig("m5_q02_matplotlib_chart_types.png")
print("Saved example charts to m5_q02_matplotlib_chart_types.png")
