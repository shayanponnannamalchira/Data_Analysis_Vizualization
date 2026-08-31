"""
Q38. Customer Purchase Analyzer
An e-commerce company records customer purchases.
Develop a Python program that stores customer names and purchase amounts in a dictionary.
The program should:
Calculate total revenue.
Find the highest-spending customer.
Find the average purchase amount.
Display customers who spent more than the average.
Give a "Gold" status to customers spending above ₹50,000.
Give a "Silver" status to customers spending between ₹20,000 and ₹50,000.
Give a "Regular" status to others.

Topics: Dictionaries + Loops + Conditions + Functions + Descriptive Analytics.
"""

customer_purchases = {
    "Amit": 62000,
    "Ravi": 15000,
    "Priya": 48000,
    "John": 8000,
    "Kiran": 75000,
    "Anita": 25000,
}


def calculate_total_revenue(purchases):
    return sum(purchases.values())


def find_highest_spending_customer(purchases):
    return max(purchases, key=purchases.get)


def calculate_average_purchase(purchases):
    return sum(purchases.values()) / len(purchases)


def assign_status(amount):
    """Assign a customer status based on their spending amount."""
    if amount > 50000:
        return "Gold"
    elif 20000 <= amount <= 50000:
        return "Silver"
    else:
        return "Regular"


total_revenue = calculate_total_revenue(customer_purchases)
top_customer = find_highest_spending_customer(customer_purchases)
average_purchase = calculate_average_purchase(customer_purchases)

print("Customer Purchases:", customer_purchases)
print(f"\nTotal Revenue: ₹{total_revenue}")
print(f"Highest-Spending Customer: {top_customer} (₹{customer_purchases[top_customer]})")
print(f"Average Purchase Amount: ₹{average_purchase:.2f}")

print("\nCustomers who spent more than the average:")
for name, amount in customer_purchases.items():
    if amount > average_purchase:
        print(f"{name}: ₹{amount}")

print("\nCustomer Status:")
for name, amount in customer_purchases.items():
    status = assign_status(amount)
    print(f"{name}: ₹{amount} -> {status}")
