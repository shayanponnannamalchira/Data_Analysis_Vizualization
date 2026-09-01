"""
U4 Q4. Combining Datasets - Student Records
A college stores student personal information and examination results in two
separate DataFrames: student_info and marks (both containing Student_ID).

a) Combine the two DataFrames using merge().
b) Display students who have records in both datasets.
c) Identify students whose examination marks are unavailable.
"""
import pandas as pd

student_info = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4],
    "Name": ["Ravi", "Anu", "Kiran", "Meena"],
})

marks = pd.DataFrame({
    "Student_ID": [1, 2, 4],
    "Marks": [85, 90, 78],
})

# a
merged = pd.merge(student_info, marks, on="Student_ID", how="left")
print("a) Merged DataFrame:")
print(merged)

# b
in_both = pd.merge(student_info, marks, on="Student_ID", how="inner")
print("\nb) Students with records in both datasets:")
print(in_both)

# c
missing_marks = merged[merged["Marks"].isnull()]
print("\nc) Students whose marks are unavailable:")
print(missing_marks)
