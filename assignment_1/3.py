"""
Q3. Why Python for Analytics?
A company wants to analyze employee salaries stored in a Python collection.
Write a Python program that calculates the average salary and identifies employees earning above the average.
Explain why Python is suitable for this type of data analysis.

Topics: Python for analytics, Lists, Loops, Conditions, Functions.
"""

# Dictionary storing employee names and their salaries
employee_salaries = {
    "Amit": 45000,
    "Priya": 62000,
    "Rahul": 38000,
    "Sneha": 71000,
    "Karan": 54000,
    "Divya": 49000
}


def calculate_average(salaries):
    """Returns the average of a list of salaries."""
    return sum(salaries) / len(salaries)


def employees_above_average(emp_dict, average):
    """Returns a list of (name, salary) for employees earning above average."""
    above_avg = []
    for name, salary in emp_dict.items():
        if salary > average:
            above_avg.append((name, salary))
    return above_avg


# Calculate average salary
salary_list = list(employee_salaries.values())
average_salary = calculate_average(salary_list)

# Identify employees earning above average
above_average_employees = employees_above_average(employee_salaries, average_salary)

print("Employee Salaries:", employee_salaries)
print("Average Salary: ", round(average_salary, 2))
print("\nEmployees earning above average salary:")
for name, salary in above_average_employees:
    print(f"  {name}: {salary}")

print("""
Why Python is suitable for this type of data analysis:
1. Simple, readable syntax makes it easy to write and maintain analytical code.
2. Built-in data structures (lists, dictionaries) handle collections of data naturally.
3. Rich ecosystem of libraries (NumPy, Pandas, Matplotlib) for advanced analytics.
4. Strong support for functions and reusable code, useful for repeated calculations.
5. Free, open-source, and widely supported across platforms and communities.
""")
