"""
Q14. Student Grade Calculator
Write a Python program that accepts marks and assigns grades according to the following:
Marks       Grade
90–100      A+
80–89       A
70–79       B
60–69       C
50–59       D
Below 50    F

Also display whether the student has passed or failed.

Topics: if, elif, else, Comparison operators.
"""

# Marks obtained by the student
marks = 72

# Assign grade based on marks
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

# Determine pass/fail status
result = "Pass" if marks >= 50 else "Fail"

print("Marks: ", marks)
print("Grade: ", grade)
print("Result: ", result)
