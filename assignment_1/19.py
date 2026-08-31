"""
Q19. Reusable Sales Calculator
Create a user-defined function calculate_sales() that accepts a list of sales values and returns:
Total sales
Average sales
Maximum sales
Call the function using different sets of sales data.

Topics: Functions, Lists, Built-in functions.
"""


def calculate_sales(sales_list):
    """Accepts a list of sales values and returns total, average, and maximum sales."""
    total = sum(sales_list)
    average = total / len(sales_list)
    maximum = max(sales_list)
    return total, average, maximum


# First dataset - Store A weekly sales
store_a_sales = [12000, 15500, 9800, 17200, 13400]
total_a, avg_a, max_a = calculate_sales(store_a_sales)
print("Store A Sales:", store_a_sales)
print(f"  Total: ₹{total_a}, Average: ₹{avg_a:.2f}, Maximum: ₹{max_a}\n")

# Second dataset - Store B weekly sales
store_b_sales = [8600, 9400, 10200, 7600, 11500, 9900]
total_b, avg_b, max_b = calculate_sales(store_b_sales)
print("Store B Sales:", store_b_sales)
print(f"  Total: ₹{total_b}, Average: ₹{avg_b:.2f}, Maximum: ₹{max_b}\n")

# Third dataset - Store C monthly sales
store_c_sales = [45000, 52000, 48000, 61000]
total_c, avg_c, max_c = calculate_sales(store_c_sales)
print("Store C Sales:", store_c_sales)
print(f"  Total: ₹{total_c}, Average: ₹{avg_c:.2f}, Maximum: ₹{max_c}")
