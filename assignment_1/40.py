"""
Q40. Simple Data Analytics Dashboard
Create a Python program that accepts marks of students and provides the following analytics:
Total number of students
Average marks
Highest marks
Lowest marks
Number of students who passed
Number of students who failed
Percentage of students who passed
Students scoring above average
Grade distribution
The program should use at least one list, one function, one loop, and conditional statements.

Topics: Data Analytics + Lists + Functions + Loops + Conditions + Operators
"""

PASS_MARK = 40


def get_grade(marks):
    """Return a letter grade based on marks out of 100."""
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


def analyze_marks(marks_list):
    """Perform the complete analytics on a list of student marks."""
    total_students = len(marks_list)
    average_marks = sum(marks_list) / total_students
    highest_marks = max(marks_list)
    lowest_marks = min(marks_list)

    passed_count = 0
    failed_count = 0
    above_average = []
    grade_distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for marks in marks_list:
        if marks >= PASS_MARK:
            passed_count += 1
        else:
            failed_count += 1

        if marks > average_marks:
            above_average.append(marks)

        grade = get_grade(marks)
        grade_distribution[grade] += 1

    pass_percentage = (passed_count / total_students) * 100

    return {
        "total_students": total_students,
        "average_marks": average_marks,
        "highest_marks": highest_marks,
        "lowest_marks": lowest_marks,
        "passed_count": passed_count,
        "failed_count": failed_count,
        "pass_percentage": pass_percentage,
        "above_average": above_average,
        "grade_distribution": grade_distribution,
    }


def main():
    marks_list = []
    n = int(input("Enter the number of students: "))
    for i in range(n):
        marks = float(input(f"Enter marks for student {i + 1} (out of 100): "))
        marks_list.append(marks)

    results = analyze_marks(marks_list)

    print("\n===== Data Analytics Dashboard =====")
    print("Total number of students:", results["total_students"])
    print(f"Average marks: {results['average_marks']:.2f}")
    print("Highest marks:", results["highest_marks"])
    print("Lowest marks:", results["lowest_marks"])
    print("Number of students who passed:", results["passed_count"])
    print("Number of students who failed:", results["failed_count"])
    print(f"Percentage of students who passed: {results['pass_percentage']:.2f}%")
    print("Students scoring above average:", results["above_average"])
    print("Grade distribution:", results["grade_distribution"])


if __name__ == "__main__":
    main()
