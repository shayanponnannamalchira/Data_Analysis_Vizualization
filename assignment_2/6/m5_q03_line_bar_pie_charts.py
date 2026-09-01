"""
Module 5, Q3. Describe the following charts in detail: Line chart, Bar chart,
Pie chart. Explain when each chart should be used with real-life examples.
"""
import matplotlib.pyplot as plt

print("""
Line Chart: Connects data points with a continuous line, ideal for showing trends over
time or an ordered continuous variable. Real-life example: tracking a company's monthly
revenue over a year to see growth/decline trends.

Bar Chart: Uses rectangular bars to compare values across discrete categories. Real-life
example: comparing the number of units sold by different product categories in a store.

Pie Chart: Divides a circle into slices to represent proportions of a whole (percentages
that sum to 100%). Real-life example: showing the market share of different smartphone
brands. Best used with only a few (e.g., <=6) categories, otherwise it becomes cluttered.

When to use each:
- Line chart: continuous/time-series data, trend analysis.
- Bar chart: comparing discrete categories or groups.
- Pie chart: showing part-to-whole composition with few categories.
""")

months = ["Jan", "Feb", "Mar", "Apr", "May"]
revenue = [10000, 12000, 9000, 15000, 17000]

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
axes[0].plot(months, revenue, marker="o"); axes[0].set_title("Line Chart: Monthly Revenue")
axes[1].bar(months, revenue, color="#55a868"); axes[1].set_title("Bar Chart: Monthly Revenue")
axes[2].pie(revenue, labels=months, autopct="%1.1f%%"); axes[2].set_title("Pie Chart: Revenue Share")
plt.tight_layout()
plt.savefig("m5_q03_line_bar_pie.png")
print("Saved example charts to m5_q03_line_bar_pie.png")
