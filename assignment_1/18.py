"""
Q18. Attendance Monitoring System
A teacher enters attendance percentages for students one by one.
Use a loop to identify students whose attendance is below 75%. Continue until the teacher chooses
to stop entering data.

Topics: while loop, conditions, input, variables.
"""

low_attendance_students = []
student_count = 0

print("=== Attendance Monitoring System ===")

while True:
    student_name = input("Enter student name (or type 'stop' to finish): ")

    # Stop the loop when the teacher types 'stop'
    if student_name.lower() == "stop":
        break

    attendance = float(input(f"Enter attendance percentage for {student_name}: "))
    student_count += 1

    # Check if attendance is below 75%
    if attendance < 75:
        low_attendance_students.append((student_name, attendance))

print(f"\nTotal students entered: {student_count}")
print("Students with attendance below 75%:")

if low_attendance_students:
    for name, attendance in low_attendance_students:
        print(f"  {name}: {attendance}%")
else:
    print("  None")
