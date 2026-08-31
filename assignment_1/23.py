"""
Q23. Product Price Analysis
A store maintains product prices in a list. Write a Python program to:
Display all products costing more than ₹5,000.
Add a new product price.
Remove a discontinued product.
Sort the prices in ascending order.

Topics: Lists, Indexing, Loops, List operations.
"""

prices = [2500, 6200, 4800, 7500, 3200, 9999, 1500]

print("Original prices:", prices)

# Display all products costing more than ₹5,000
print("\nProducts costing more than ₹5,000:")
for price in prices:
    if price > 5000:
        print(price)

# Add a new product price
new_price = 4300
prices.append(new_price)
print(f"\nAdded new product price: {new_price}")
print("Updated prices:", prices)

# Remove a discontinued product
discontinued_price = 1500
if discontinued_price in prices:
    prices.remove(discontinued_price)
    print(f"\nRemoved discontinued product price: {discontinued_price}")
print("Updated prices:", prices)

# Sort the prices in ascending order
prices.sort()
print("\nPrices sorted in ascending order:", prices)
