"""
Q15. Loan Eligibility System
A bank considers a customer eligible for a loan if their salary is at least ₹30,000 and their
credit score is at least 700.
Write a Python program to check loan eligibility and display an appropriate message.

Topics: Variables, Comparison operators, Logical operators, if-else.
"""

# Customer details
salary = 35000
credit_score = 720

# Check eligibility using logical AND
if salary >= 30000 and credit_score >= 700:
    print("Congratulations! You are eligible for the loan.")
else:
    print("Sorry, you are not eligible for the loan.")

print(f"Salary: ₹{salary}, Credit Score: {credit_score}")
