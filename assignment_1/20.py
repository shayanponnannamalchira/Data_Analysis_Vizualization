"""
Q20. Student Result Function
Create a function calculate_grade(marks) that accepts marks and returns the student's grade.
Use the function for five students and display their names, marks, and grades.

Topics: User-defined functions, Lists, Conditions, Loops.
"""


def calculate_grade(marks):
    """Accepts marks and returns the corresponding grade."""
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


# Data for five students
students = ["Aarav", "Isha", "Rohan", "Meera", "Vikram"]
marks_list = [92, 76, 58, 84, 41]

print(f"{'Name':<10}{'Marks':<10}{'Grade':<10}")
print("-" * 30)

# Loop through each student and calculate their grade
for name, marks in zip(students, marks_list):
    grade = calculate_grade(marks)
    print(f"{name:<10}{marks:<10}{grade:<10}")
