"""
Q29. Product Inventory System
A supermarket maintains inventory using a dictionary:
inventory = {
    "Rice": 50,
    "Sugar": 30,
    "Oil": 20,
    "Dal": 40
}

Write a Python program that allows the user to:
Search for a product.
Display its stock.
Update stock after a sale.
Display products whose stock is below 25.

Topics: Dictionaries, Conditions, Loops, Dictionary operations.
"""

inventory = {
    "Rice": 50,
    "Sugar": 30,
    "Oil": 20,
    "Dal": 40
}


def search_product(product_name):
    if product_name in inventory:
        print(f"{product_name} is available. Stock: {inventory[product_name]}")
    else:
        print(f"{product_name} not found in inventory.")


def update_stock(product_name, quantity_sold):
    if product_name in inventory:
        if inventory[product_name] >= quantity_sold:
            inventory[product_name] -= quantity_sold
            print(f"Sold {quantity_sold} units of {product_name}. "
                  f"Remaining stock: {inventory[product_name]}")
        else:
            print(f"Not enough stock for {product_name}. "
                  f"Available: {inventory[product_name]}")
    else:
        print(f"{product_name} not found in inventory.")


def display_low_stock(threshold=25):
    print(f"\nProducts with stock below {threshold}:")
    for product, stock in inventory.items():
        if stock < threshold:
            print(f"{product}: {stock}")


def main():
    print("Current Inventory:", inventory)

    # Search for a product
    product = input("\nEnter product name to search: ")
    search_product(product)

    # Update stock after a sale
    product = input("\nEnter product name to sell: ")
    quantity = int(input("Enter quantity sold: "))
    update_stock(product, quantity)

    # Display products whose stock is below 25
    display_low_stock()

    print("\nFinal Inventory:", inventory)


if __name__ == "__main__":
    main()
