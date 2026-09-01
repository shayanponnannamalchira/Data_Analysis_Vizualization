"""
Module 5, Q7. What is a Scatter Plot? Explain how it helps in understanding
the relationship between two variables. Give a real-life example.
"""
import matplotlib.pyplot as plt
import numpy as np

print("""
A Scatter Plot displays individual data points on a two-dimensional grid, with one
variable on the x-axis and another on the y-axis. Each point represents one observation's
combination of the two variable values.

How it helps: It visually reveals the relationship (or lack thereof) between two numeric
variables - whether it's positive, negative, or no correlation, whether the relationship
is linear or non-linear, and it helps spot clusters and outliers.

Real-life example: Plotting advertising expenditure (x-axis) against sales revenue
(y-axis) for several months to see whether higher spending tends to correspond with
higher sales.
""")

np.random.seed(0)
ad_spend = np.linspace(1000, 10000, 30) + np.random.normal(0, 500, 30)
sales = ad_spend * 3 + np.random.normal(0, 2000, 30)

plt.figure(figsize=(7, 5))
plt.scatter(ad_spend, sales, color="#55a868", alpha=0.7)
plt.title("Advertising Expenditure vs Sales")
plt.xlabel("Advertising Expenditure (Rs)")
plt.ylabel("Sales Revenue (Rs)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("m5_q07_scatter_plot.png")
print("Saved scatter plot to m5_q07_scatter_plot.png")
