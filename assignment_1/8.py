"""
Q8. Electricity Bill Calculator
Write a Python program that accepts the number of electricity units consumed and calculates the
bill according to the following rules:
First 100 units → ₹2/unit
Next 100 units → ₹3/unit
Above 200 units → ₹5/unit
Use proper indentation and comments.

Topics: Syntax, Indentation, Comments, Variables, Conditions, Arithmetic operators.
"""

# Number of electricity units consumed
units = 250

# Initialize bill amount
bill = 0

# Case 1: Units within the first slab (0-100 units)
if units <= 100:
    bill = units * 2

# Case 2: Units within the second slab (101-200 units)
elif units <= 200:
    bill = (100 * 2) + (units - 100) * 3

# Case 3: Units above 200
else:
    bill = (100 * 2) + (100 * 3) + (units - 200) * 5

# Display the result
print("Units Consumed: ", units)
print("Total Electricity Bill: ₹", bill)
