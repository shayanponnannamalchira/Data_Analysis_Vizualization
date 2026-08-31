"""
Q7. Employee Attendance Program
Write a Python program to calculate an employee's attendance percentage based on the number of
days present and total working days. Include appropriate comments explaining each major step.

Topics: Syntax, Indentation, Comments, Variables, Arithmetic operators.
"""

# Step 1: Define the number of days the employee was present
days_present = 22

# Step 2: Define the total number of working days in the period
total_working_days = 26

# Step 3: Calculate attendance percentage
# Formula: (days present / total working days) * 100
attendance_percentage = (days_present / total_working_days) * 100

# Step 4: Display the results
print("Days Present: ", days_present)
print("Total Working Days: ", total_working_days)
print("Attendance Percentage: {:.2f}%".format(attendance_percentage))
