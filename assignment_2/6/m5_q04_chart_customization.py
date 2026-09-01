"""
Module 5, Q4/Q5. What is chart customization? Explain the importance of the
following elements in a graph: Title, X-axis label, Y-axis label, Legend,
Colors, Gridlines.
"""
import matplotlib.pyplot as plt

print("""
Chart customization refers to adjusting the visual elements of a chart (titles, labels,
colors, styles, gridlines, etc.) to make it clearer, more accurate, and more informative
for the intended audience, rather than relying on default settings.

Importance of each element:
- Title: Tells the viewer at a glance what the chart is about.
- X-axis label: Clarifies what the horizontal axis represents (units, categories, time).
- Y-axis label: Clarifies what the vertical axis measures (units, scale).
- Legend: Distinguishes multiple data series/categories shown in the same chart.
- Colors: Help differentiate categories, highlight important data, and improve readability
  (but should be used purposefully, not decoratively).
- Gridlines: Make it easier to read exact values and compare data points precisely.
""")

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 25, 30]
y2 = [5, 15, 10, 20, 22]

plt.figure(figsize=(7, 5))
plt.plot(x, y1, label="Product A", color="#4c72b0", marker="o")
plt.plot(x, y2, label="Product B", color="#dd8452", marker="s")
plt.title("Sales Comparison: Product A vs Product B")
plt.xlabel("Month")
plt.ylabel("Sales (units)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("m5_q04_chart_customization.png")
print("Saved customized chart to m5_q04_chart_customization.png")
