"""
Q31. Transaction Analysis
A bank stores transaction amounts in a list:
transactions = [1200, -500, 3000, -700, 2500, -200, 1800]

Positive values represent deposits and negative values represent withdrawals.
Use indexing, slicing, and list operations to analyze selected transactions.

Topics: Lists, Indexing, Slicing, Arithmetic.
"""

transactions = [1200, -500, 3000, -700, 2500, -200, 1800]

print("All transactions:", transactions)

# Indexing examples
first_transaction = transactions[0]
last_transaction = transactions[-1]
print("\nFirst transaction:", first_transaction)
print("Last transaction:", last_transaction)

# Slicing: first three and last three transactions
first_three = transactions[:3]
last_three = transactions[-3:]
print("\nFirst three transactions:", first_three)
print("Last three transactions:", last_three)

# Separate deposits and withdrawals
deposits = [amount for amount in transactions if amount > 0]
withdrawals = [amount for amount in transactions if amount < 0]

total_deposits = sum(deposits)
total_withdrawals = sum(withdrawals)
net_balance = sum(transactions)

print("\nDeposits:", deposits)
print("Withdrawals:", withdrawals)
print("Total deposits:", total_deposits)
print("Total withdrawals:", total_withdrawals)
print("Net balance:", net_balance)

# Middle transactions using slicing
middle_transactions = transactions[2:5]
print("\nMiddle transactions (index 2 to 4):", middle_transactions)
