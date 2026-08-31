"""
Q34. College Attendance Analyzer
A college maintains attendance information for students.
Write a Python program that:
Stores student names and attendance percentages in a dictionary.
Displays students with attendance below 75%.
Calculates the average attendance.
Finds the student with the highest attendance.
Uses a function to determine whether a student is eligible to appear for the examination.

Topics: Dictionary + Functions + Loops + Conditions + Built-in functions.
"""

attendance = {
    "Amit": 82,
    "Ravi": 68,
    "Priya": 91,
    "John": 74,
    "Kiran": 55,
    "Anita": 88,
}


def is_eligible(percentage, minimum_required=75):
    """Determine whether a student is eligible to appear for the exam."""
    return percentage >= minimum_required


# Display students with attendance below 75%
print("Students with attendance below 75%:")
for name, percentage in attendance.items():
    if percentage < 75:
        print(f"{name}: {percentage}%")

# Calculate the average attendance
average_attendance = sum(attendance.values()) / len(attendance)
print(f"\nAverage attendance: {average_attendance:.2f}%")

# Find the student with the highest attendance
top_student = max(attendance, key=attendance.get)
print(f"Student with the highest attendance: {top_student} ({attendance[top_student]}%)")

# Check exam eligibility for all students
print("\nExamination Eligibility:")
for name, percentage in attendance.items():
    status = "Eligible" if is_eligible(percentage) else "Not Eligible"
    print(f"{name}: {percentage}% -> {status}")
