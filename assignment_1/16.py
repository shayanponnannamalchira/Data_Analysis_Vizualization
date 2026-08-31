"""
Q16. Daily Sales Analysis
A shop records sales for 7 days. Write a Python program using a for loop to calculate:
Total sales
Average sales
Number of days with sales above ₹10,000

Topics: Lists, for loop, arithmetic operators, conditions.
"""

# Sales recorded for 7 days
daily_sales = [8500, 12300, 9800, 15600, 11200, 7600, 13400]

total_sales = 0
days_above_10000 = 0

# Using a for loop to calculate total sales and count days above ₹10,000
for sale in daily_sales:
    total_sales += sale
    if sale > 10000:
        days_above_10000 += 1

# Calculate average sales
average_sales = total_sales / len(daily_sales)

print("Daily Sales: ", daily_sales)
print("Total Sales: ₹", total_sales)
print("Average Sales: ₹", round(average_sales, 2))
print("Number of days with sales above ₹10,000: ", days_above_10000)
