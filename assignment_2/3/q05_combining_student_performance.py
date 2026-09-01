"""
U3 Q5 - Combining Datasets: Student Performance
A university maintains student information in two separate datasets:
Student Details and Student Marks.

1. Create the two DataFrames and display them.
2. Combine using an appropriate merge on Student_ID.
3. Identify students whose details are missing from either dataset.
4. Create Total_Marks.
5. Create Average_Marks.
6. Filter students whose average marks > 80.
7. Group by Department, calculate average marks.
8. Check the final dataset for duplicate records and missing values.
"""
import pandas as pd

student_details = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104],
    "Name": ["Ravi", "Anu", "Kiran", "Meena"],
    "Department": ["CSE", "ECE", "CSE", "ISE"],
})

student_marks = pd.DataFrame({
    "Student_ID": [101, 102, 103, 105],
    "Python": [85, 72, 90, 65],
    "Statistics": [78, 81, 86, 70],
    "ML": [88, 75, 92, 68],
})

print("Student Details:")
print(student_details)
print("\nStudent Marks:")
print(student_marks)

# 2. Merge (outer to reveal mismatches, as needed for step 3)
merged_outer = pd.merge(student_details, student_marks, on="Student_ID", how="outer")
print("\nOuter merge (all records):")
print(merged_outer)

# 3. Missing from either dataset
missing_details = merged_outer[merged_outer["Name"].isnull()]
missing_marks = merged_outer[merged_outer["Python"].isnull()]
print("\nStudents missing details:")
print(missing_details[["Student_ID"]])
print("\nStudents missing marks:")
print(missing_marks[["Student_ID"]])

# Use inner merge for the marks-based calculations going forward
merged = pd.merge(student_details, student_marks, on="Student_ID", how="inner")

# 4 & 5. Total and average marks
merged["Total_Marks"] = merged["Python"] + merged["Statistics"] + merged["ML"]
merged["Average_Marks"] = merged["Total_Marks"] / 3

# 6. Filter average > 80
top_students = merged[merged["Average_Marks"] > 80]
print("\nStudents with average marks > 80:")
print(top_students)

# 7. Group by department
print("\nAverage marks by department:")
print(merged.groupby("Department")["Average_Marks"].mean())

# 8. Duplicate / missing check
print(f"\nDuplicates: {merged.duplicated().sum()}")
print(f"Missing values: {merged.isnull().sum().sum()}")
