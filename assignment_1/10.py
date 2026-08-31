"""
Q10. Product Billing System
A customer purchases a product. Store the product name, quantity, price per unit, and whether the
customer is a member of the store. Calculate the total amount.
If the customer is a member, display that a discount is applicable.

Topics: Variables, Data types, Boolean, Arithmetic operators, Conditions.
"""

# Product and customer details
product_name = "Wireless Mouse"
quantity = 3
price_per_unit = 799.0
is_member = True

# Calculate total amount before any discount
total_amount = quantity * price_per_unit

print("Product Name: ", product_name)
print("Quantity: ", quantity)
print("Price per Unit: ₹", price_per_unit)
print("Total Amount: ₹", total_amount)

# Check membership status and apply discount info
if is_member:
    discount_rate = 0.10  # 10% discount for members
    discount_amount = total_amount * discount_rate
    final_amount = total_amount - discount_amount
    print("Membership Status: Member")
    print("A discount of 10% is applicable.")
    print("Discount Amount: ₹", discount_amount)
    print("Final Amount Payable: ₹", final_amount)
else:
    print("Membership Status: Non-Member")
    print("No discount applicable. Final Amount Payable: ₹", total_amount)
