"""
Q28. Student Marks Dictionary
Create a dictionary containing student names and their marks. Write a Python program to:
Display all students.
Find the student with the highest marks.
Calculate the average marks.
Display students scoring above 75.

Topics: Dictionaries, Loops, Conditions, Functions/Built-in functions.
"""

student_marks = {
    "Amit": 82,
    "Ravi": 65,
    "Priya": 91,
    "John": 74,
    "Kiran": 58,
    "Anita": 88,
}

# Display all students
print("All students and their marks:")
for name, marks in student_marks.items():
    print(f"{name}: {marks}")

# Find the student with the highest marks
topper = max(student_marks, key=student_marks.get)
print(f"\nStudent with the highest marks: {topper} ({student_marks[topper]})")

# Calculate the average marks
average_marks = sum(student_marks.values()) / len(student_marks)
print(f"Average marks: {average_marks:.2f}")

# Display students scoring above 75
print("\nStudents scoring above 75:")
for name, marks in student_marks.items():
    if marks > 75:
        print(f"{name}: {marks}")
