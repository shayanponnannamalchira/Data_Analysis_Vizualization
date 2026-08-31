"""
Q13. Online Shopping Eligibility
An e-commerce website provides free delivery if the order amount is above ₹1,000 OR the customer
is a premium member.
Write a Python program that accepts the order amount and membership status and determines whether
free delivery is available.

Topics: Boolean, Comparison operators, Logical operators, Conditions.
"""

# Order details
order_amount = 850
is_premium_member = True

# Free delivery if order amount > 1000 OR customer is a premium member
if order_amount > 1000 or is_premium_member:
    print("Free delivery is available for this order.")
else:
    print("Free delivery is NOT available. Delivery charges will apply.")

print(f"Order Amount: ₹{order_amount}, Premium Member: {is_premium_member}")
