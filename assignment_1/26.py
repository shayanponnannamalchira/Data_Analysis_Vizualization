"""
Q26. Unique Course Registration
Two groups of students register for courses:
group_A = {"Amit", "Ravi", "Priya", "John"}
group_B = {"Priya", "John", "Kiran", "Anita"}

Write a Python program to find:
Students registered in both groups.
Students registered only in Group A.
Students registered in either group.
Total number of unique students.

Topics: Sets, Union, Intersection, Difference.
"""

group_A = {"Amit", "Ravi", "Priya", "John"}
group_B = {"Priya", "John", "Kiran", "Anita"}

both_groups = group_A & group_B
only_group_A = group_A - group_B
either_group = group_A | group_B
total_unique_students = len(either_group)

print("Group A:", group_A)
print("Group B:", group_B)

print("\nStudents registered in both groups:", both_groups)
print("Students registered only in Group A:", only_group_A)
print("Students registered in either group:", either_group)
print("Total number of unique students:", total_unique_students)
