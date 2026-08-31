"""
Q39. Employee Salary Analytics
An organization stores employee salary information using a dictionary.
Write a Python program to:
Calculate average salary.
Identify employees earning above average.
Find the highest-paid employee.
Count employees earning below ₹30,000.
Assign salary categories using conditions.
Create a function to perform the salary analysis.

Topics: Dictionaries + Functions + Conditions + Loops + Operators.
"""

employee_salaries = {
    "Amit": 45000,
    "Ravi": 28000,
    "Priya": 62000,
    "John": 25000,
    "Kiran": 38000,
    "Anita": 21000,
}


def categorize_salary(salary):
    """Assign a salary category based on the amount earned."""
    if salary >= 50000:
        return "High"
    elif salary >= 30000:
        return "Medium"
    else:
        return "Low"


def analyze_salaries(salaries):
    """Perform a complete salary analysis and return the results."""
    average_salary = sum(salaries.values()) / len(salaries)

    above_average = {}
    below_30000_count = 0
    categories = {}

    for name, salary in salaries.items():
        if salary > average_salary:
            above_average[name] = salary
        if salary < 30000:
            below_30000_count += 1
        categories[name] = categorize_salary(salary)

    highest_paid = max(salaries, key=salaries.get)

    return {
        "average_salary": average_salary,
        "above_average": above_average,
        "highest_paid": highest_paid,
        "below_30000_count": below_30000_count,
        "categories": categories,
    }


results = analyze_salaries(employee_salaries)

print("Employee Salaries:", employee_salaries)
print(f"\nAverage Salary: ₹{results['average_salary']:.2f}")

print("\nEmployees earning above average:")
for name, salary in results["above_average"].items():
    print(f"{name}: ₹{salary}")

print(f"\nHighest-Paid Employee: {results['highest_paid']} "
      f"(₹{employee_salaries[results['highest_paid']]})")

print(f"\nNumber of employees earning below ₹30,000: {results['below_30000_count']}")

print("\nSalary Categories:")
for name, category in results["categories"].items():
    print(f"{name}: {category}")
