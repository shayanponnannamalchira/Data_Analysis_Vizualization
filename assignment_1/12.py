"""
Q12. Student Eligibility Checker
A student can participate in a scholarship program if:
CGPA is at least 8.0, and
Attendance is at least 75%.
Write a Python program to check whether the student is eligible.

Topics: Comparison operators, Logical operators, Conditions.
"""

# Student details
cgpa = 8.5
attendance_percentage = 80

# Check eligibility using logical AND
if cgpa >= 8.0 and attendance_percentage >= 75:
    print("The student is ELIGIBLE for the scholarship program.")
else:
    print("The student is NOT ELIGIBLE for the scholarship program.")

print(f"CGPA: {cgpa}, Attendance: {attendance_percentage}%")
