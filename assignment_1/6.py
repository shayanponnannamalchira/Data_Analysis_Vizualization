"""
Q6. Prescriptive Analytics — Inventory Management
A supermarket has 100 units of a product in stock.
The minimum required stock is 30 units. Write a Python program that checks the current stock
and recommends:
"No action required" if stock is above 60.
"Monitor stock" if stock is between 30 and 60.
"Place an order" if stock is below 30.

Topics: Prescriptive analytics, Variables, Comparison operators, if-elif-else.
"""

current_stock = 100
minimum_required_stock = 30

print("Current Stock: ", current_stock)

if current_stock > 60:
    recommendation = "No action required"
elif current_stock >= minimum_required_stock:  # between 30 and 60 (inclusive of 30)
    recommendation = "Monitor stock"
else:
    recommendation = "Place an order"

print("Recommendation: ", recommendation)
