"""
Q17. ATM Withdrawal System
Write a Python program that repeatedly asks a customer to enter a withdrawal amount.
Continue accepting transactions until the customer enters 0. Display the total amount withdrawn.

Topics: while loop, variables, conditions, arithmetic operators.
"""

total_withdrawn = 0

print("=== ATM Withdrawal System ===")
print("Enter withdrawal amount (enter 0 to stop):")

while True:
    amount = float(input("Enter withdrawal amount: "))

    # Stop the loop when the customer enters 0
    if amount == 0:
        break

    total_withdrawn += amount
    print(f"Withdrawn: ₹{amount}. Running total: ₹{total_withdrawn}")

print("\nTransaction ended.")
print("Total amount withdrawn: ₹", total_withdrawn)
