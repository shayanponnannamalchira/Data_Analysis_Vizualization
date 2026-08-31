"""
Q30. Customer Contact Analysis
A company stores customer names in a list. Write a Python program to:
Display the first three customers.
Display the last three customers.
Display customers at even positions.
Reverse the list.

Topics: Lists, Indexing, Slicing.
"""

customers = ["Amit", "Ravi", "Priya", "John", "Kiran", "Anita", "Suresh", "Meena"]

print("All customers:", customers)

# Display the first three customers
first_three = customers[:3]
print("\nFirst three customers:", first_three)

# Display the last three customers
last_three = customers[-3:]
print("Last three customers:", last_three)

# Display customers at even positions (0, 2, 4, ...)
even_position_customers = customers[::2]
print("Customers at even positions:", even_position_customers)

# Reverse the list
reversed_customers = customers[::-1]
print("Reversed list of customers:", reversed_customers)
