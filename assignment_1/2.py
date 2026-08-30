"""
Q2. Sales Analysis — Descriptive Analytics
A shop records its daily sales for one week:
[12500, 15800, 14300, 17600, 19200, 16500, 21000]
Write a Python program to determine:
Total weekly sales
Average daily sales
Highest sales day
Lowest sales day
Number of days where sales exceeded the weekly average

Topics: Descriptive analytics, Lists, Operators, Loops, Conditional statements.
"""
import pandas as pd
import numpy as np

sales = [12500, 15800, 14300, 17600, 19200, 16500, 21000]

total = np.sum(sales)
average = np.mean(sales)
highest_sales = np.max(sales)
lowest_sales = np.min(sales)
exceed=sum(1 for sale in sales if sale>average) # Count of days where sales exceeded the weekly average

print("Total weekly sales: ", total)
print("Average daily sales: ", average)
print("Highest sales day: ", highest_sales)
print("Lowest sales day: ", lowest_sales)
print("Number of days where sales exceeded the weekly average: ", exceed)