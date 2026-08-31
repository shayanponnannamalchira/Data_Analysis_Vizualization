"""
Q4. Descriptive vs Diagnostic Analytics
A retail store has the following monthly sales:
Month     Sales
January   50,000
February  55,000
March     48,000
April     42,000
May       65,000

Write a Python program to:
Find the average sales.
Identify the month with the highest and lowest sales.
Identify months where sales decreased compared with the previous month.
Display possible observations from the data.

Topics: Descriptive analytics, Diagnostic analytics, Lists, Loops, Conditions.
"""

months = ["January", "February", "March", "April", "May"]
sales = [50000, 55000, 48000, 42000, 65000]

# Descriptive analytics: average sales
average_sales = sum(sales) / len(sales)

# Descriptive analytics: highest and lowest sales month
highest_index = sales.index(max(sales))
lowest_index = sales.index(min(sales))

print("Average Sales: ", average_sales)
print(f"Highest Sales Month: {months[highest_index]} ({sales[highest_index]})")
print(f"Lowest Sales Month: {months[lowest_index]} ({sales[lowest_index]})")

# Diagnostic analytics: months where sales decreased compared to previous month
print("\nMonths where sales decreased compared to the previous month:")
decreased_months = []
for i in range(1, len(sales)):
    if sales[i] < sales[i - 1]:
        decreased_months.append(months[i])
        print(f"  {months[i]}: dropped from {sales[i-1]} to {sales[i]}")

if not decreased_months:
    print("  None")

# Observations
print("\nObservations:")
print(f"1. Sales peaked in {months[highest_index]}, indicating strong performance that month.")
print(f"2. Sales were lowest in {months[lowest_index]}, which may need investigation.")
if decreased_months:
    print(f"3. Sales declined in {', '.join(decreased_months)} compared to the prior month, "
          f"suggesting possible seasonal dips or reduced demand.")
print("4. Overall, sales fluctuate month to month, so further diagnostic analysis "
      "(e.g., marketing spend, seasonality, competitor activity) could explain the causes.")
