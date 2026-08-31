"""
Q11. Employee Salary Calculation
An employee has a basic salary of ₹40,000. HRA is 20% of basic salary and DA is 10%.
Write a Python program to calculate the gross salary.

Topics: Variables, Float, Arithmetic operators.
"""

# Basic salary
basic_salary = 40000.0

# HRA: 20% of basic salary
hra = basic_salary * 0.20

# DA: 10% of basic salary
da = basic_salary * 0.10

# Gross salary = Basic + HRA + DA
gross_salary = basic_salary + hra + da

print("Basic Salary: ₹", basic_salary)
print("HRA (20%): ₹", hra)
print("DA (10%): ₹", da)
print("Gross Salary: ₹", gross_salary)
