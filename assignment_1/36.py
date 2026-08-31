"""
Q36. Sales Data Analyzer
A company stores monthly sales data:
sales = [45000, 52000, 48000, 61000, 72000, 68000,
         75000, 81000, 79000, 85000, 92000, 98000]

Develop a Python program to:
Calculate total annual sales.
Calculate average monthly sales.
Find the highest and lowest sales.
Display months where sales exceeded the average.
Display the first six months using slicing.
Create a function to calculate sales statistics.
Categorize the yearly performance as "Low", "Moderate", or "High".

Topics: Lists + Slicing + Functions + Loops + Conditions + Descriptive Analytics.
"""

sales = [45000, 52000, 48000, 61000, 72000, 68000,
         75000, 81000, 79000, 85000, 92000, 98000]

month_names = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]


def calculate_sales_statistics(sales_data):
    """Return a dictionary of total, average, highest, and lowest sales."""
    stats = {
        "total": sum(sales_data),
        "average": sum(sales_data) / len(sales_data),
        "highest": max(sales_data),
        "lowest": min(sales_data),
    }
    return stats


def categorize_performance(total_sales):
    """Categorize yearly performance based on total annual sales."""
    if total_sales < 600000:
        return "Low"
    elif total_sales <= 900000:
        return "Moderate"
    else:
        return "High"


stats = calculate_sales_statistics(sales)

print("Monthly Sales:", sales)
print(f"\nTotal Annual Sales: ₹{stats['total']}")
print(f"Average Monthly Sales: ₹{stats['average']:.2f}")
print(f"Highest Sales: ₹{stats['highest']}")
print(f"Lowest Sales: ₹{stats['lowest']}")

# Display months where sales exceeded the average
print("\nMonths where sales exceeded the average:")
for month, amount in zip(month_names, sales):
    if amount > stats["average"]:
        print(f"{month}: ₹{amount}")

# Display the first six months using slicing
first_six_months_sales = sales[:6]
print("\nFirst six months' sales:", first_six_months_sales)

# Categorize the yearly performance
performance_category = categorize_performance(stats["total"])
print(f"\nYearly Performance: {performance_category}")
