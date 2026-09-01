"""
Module 5, Q10. A teacher wants to analyze students' performance over five
exams and also compare marks among different subjects. Which charts will you
use for each case? Justify your answer with reasons.
"""
import matplotlib.pyplot as plt

print("""
Case 1 - Performance over five exams (trend over time/sequence):
Use a Line Chart. Justification: exams are ordered sequentially, and a line chart
clearly shows whether a student's performance is improving, declining, or fluctuating
across the exams.

Case 2 - Comparing marks among different subjects (categorical comparison):
Use a Bar Chart. Justification: subjects are discrete categories with no inherent order,
so a bar chart makes it easy to visually compare the marks scored in each subject side
by side.
""")

exams = ["Exam 1", "Exam 2", "Exam 3", "Exam 4", "Exam 5"]
marks_over_time = [60, 65, 70, 68, 75]

subjects = ["Math", "Science", "English", "History"]
subject_marks = [78, 82, 74, 69]

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].plot(exams, marks_over_time, marker="o", color="#4c72b0")
axes[0].set_title("Performance Over 5 Exams (Line Chart)")
axes[0].set_ylabel("Marks")

axes[1].bar(subjects, subject_marks, color="#dd8452")
axes[1].set_title("Marks by Subject (Bar Chart)")
axes[1].set_ylabel("Marks")

plt.tight_layout()
plt.savefig("m5_q10_student_performance.png")
print("Saved charts to m5_q10_student_performance.png")
