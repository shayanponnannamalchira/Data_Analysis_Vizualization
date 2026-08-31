"""
Q37. Student Result Management System
Develop a menu-driven Python program for a college that maintains student results.
The program should provide options to:
Add student details.
Display all students.
Calculate average marks.
Find the highest scorer.
Search for a student.
Display students who passed.
Display students who failed.
Exit the program.
Use appropriate Python data structures and functions.

Topics: Lists + Dictionaries + Functions + Loops + Conditions + Operators.
"""

PASS_MARK = 40

students = [] 


def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter student marks: "))
    students.append({"name": name, "marks": marks})
    print(f"Student '{name}' added successfully.")


def display_all_students():
    if not students:
        print("No student records found.")
        return
    print("\nAll Students:")
    for student in students:
        print(f"Name: {student['name']}, Marks: {student['marks']}")


def calculate_average_marks():
    if not students:
        print("No student records found.")
        return
    total = 0
    for student in students:
        total += student["marks"]
    average = total / len(students)
    print(f"Average marks of all students: {average:.2f}")


def find_highest_scorer():
    if not students:
        print("No student records found.")
        return
    topper = students[0]
    for student in students:
        if student["marks"] > topper["marks"]:
            topper = student
    print(f"Highest scorer: {topper['name']} with {topper['marks']} marks")


def search_student():
    name = input("Enter student name to search: ")
    for student in students:
        if student["name"].lower() == name.lower():
            print(f"Found: Name: {student['name']}, Marks: {student['marks']}")
            return
    print(f"Student '{name}' not found.")


def display_passed_students():
    print(f"\nStudents who passed (marks >= {PASS_MARK}):")
    found = False
    for student in students:
        if student["marks"] >= PASS_MARK:
            print(f"Name: {student['name']}, Marks: {student['marks']}")
            found = True
    if not found:
        print("No students passed.")


def display_failed_students():
    print(f"\nStudents who failed (marks < {PASS_MARK}):")
    found = False
    for student in students:
        if student["marks"] < PASS_MARK:
            print(f"Name: {student['name']}, Marks: {student['marks']}")
            found = True
    if not found:
        print("No students failed.")


def display_menu():
    print("\n===== Student Result Management System =====")
    print("1. Add student details")
    print("2. Display all students")
    print("3. Calculate average marks")
    print("4. Find the highest scorer")
    print("5. Search for a student")
    print("6. Display students who passed")
    print("7. Display students who failed")
    print("8. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_all_students()
        elif choice == "3":
            calculate_average_marks()
        elif choice == "4":
            find_highest_scorer()
        elif choice == "5":
            search_student()
        elif choice == "6":
            display_passed_students()
        elif choice == "7":
            display_failed_students()
        elif choice == "8":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
