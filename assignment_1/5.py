"""
Q5. Predictive Analytics — Customer Purchase
A company records the number of products purchased by customers during the last five months.
Write a simple Python program that calculates the average monthly purchase and predicts the
expected purchase quantity for the next month based on the average.

Topics: Predictive analytics, Lists, Arithmetic operators, Functions.
"""

# Number of products purchased in the last 5 months
monthly_purchases = [120, 135, 150, 128, 142]


def calculate_average(data):
    """Calculates and returns the average of a list of numbers."""
    return sum(data) / len(data)


def predict_next_month(data):
    """Predicts next month's purchase quantity using the average of past data."""
    return calculate_average(data)


average_purchase = calculate_average(monthly_purchases)
predicted_purchase = predict_next_month(monthly_purchases)

print("Monthly Purchases (last 5 months):", monthly_purchases)
print("Average Monthly Purchase: ", round(average_purchase, 2))
print("Predicted Purchase for Next Month: ", round(predicted_purchase, 2))
