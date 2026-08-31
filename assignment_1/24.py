"""
Q24. Employee Record
Store an employee's ID, name, department, and salary as a tuple.
Write a Python program to access individual elements and display the employee information.
Explain why a tuple may be preferred when the employee record should not be modified.

Topics: Tuples, Indexing, Variables.
"""

employee = (101, "Ravi Kumar", "Finance", 55000)

emp_id = employee[0]
emp_name = employee[1]
emp_department = employee[2]
emp_salary = employee[3]

print("Employee Record")
print("----------------")
print("ID:", emp_id)
print("Name:", emp_name)
print("Department:", emp_department)
print("Salary: ₹", emp_salary)

print(
    "\nWhy use a tuple?\n"
    "A tuple is immutable, meaning its elements cannot be changed once created.\n"
    "Since an employee record like ID, name, department, and salary should not\n"
    "be accidentally modified after creation, storing it as a tuple protects the\n"
    "data from unintended changes and keeps the record consistent and reliable."
)
