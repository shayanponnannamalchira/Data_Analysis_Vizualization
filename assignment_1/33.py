"""
Q33. Online Shopping Cart
Develop a Python program for an online shopping cart.
The program should:
Store product names and prices in a dictionary.
Allow the user to select products.
Calculate the total bill.
Apply a 10% discount if the bill exceeds ₹5,000.
Apply free delivery if the customer is a premium member or the bill exceeds ₹1,000.
Display the final bill.

Topics: Dictionary + Loops + Conditions + Boolean + Operators.
"""

products = {
    "Laptop Bag": 1500,
    "Wireless Mouse": 800,
    "Keyboard": 1200,
    "Headphones": 2500,
    "Monitor": 7000,
    "USB Cable": 300,
}

DELIVERY_CHARGE = 150


def display_products():
    print("Available Products:")
    for name, price in products.items():
        print(f"{name}: ₹{price}")


def calculate_bill(cart, is_premium_member):
    total = 0
    for item in cart:
        if item in products:
            total += products[item]
        else:
            print(f"'{item}' is not available and will be skipped.")

    original_total = total

    # Apply 10% discount if the bill exceeds ₹5,000
    discount = 0
    if total > 5000:
        discount = total * 0.10
        total -= discount

    # Apply free delivery if premium member or bill exceeds ₹1,000
    free_delivery = is_premium_member or total > 1000
    delivery_charge = 0 if free_delivery else DELIVERY_CHARGE
    total += delivery_charge

    return original_total, discount, delivery_charge, total


def main():
    display_products()

    cart = []
    n = int(input("\nHow many products do you want to buy? "))
    for i in range(n):
        item = input(f"Enter product {i + 1} name: ")
        cart.append(item)

    membership = input("Are you a premium member? (yes/no): ").strip().lower()
    is_premium_member = membership == "yes"

    original_total, discount, delivery_charge, final_bill = calculate_bill(
        cart, is_premium_member
    )

    print("\n--- Bill Summary ---")
    print(f"Cart items: {cart}")
    print(f"Subtotal: ₹{original_total:.2f}")
    print(f"Discount applied: ₹{discount:.2f}")
    print(f"Delivery charge: ₹{delivery_charge}")
    print(f"Final Bill: ₹{final_bill:.2f}")


if __name__ == "__main__":
    main()
