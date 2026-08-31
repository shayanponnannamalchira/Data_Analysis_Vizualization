"""
Q32. Employee Performance Analyzer
A company stores employee names and their monthly performance scores.
Write a Python program that:
Stores employee names in a list.
Stores scores in another list.
Uses a loop to calculate the average score.
Uses a conditional statement to classify employees as:
"Excellent" → score ≥ 90
"Good" → 70–89
"Needs Improvement" → below 70
Creates a dictionary containing employee names and performance categories.
Uses a function to calculate the average score.

Topics: Lists + Loops + Conditions + Functions + Dictionaries.
"""

employee_names = ["Amit", "Ravi", "Priya", "John", "Kiran"]
performance_scores = [92, 68, 85, 55, 95]


def calculate_average(scores):
    """Calculate and return the average of a list of scores."""
    total = 0
    for score in scores:
        total += score
    return total / len(scores)


def classify_performance(score):
    """Classify an employee's performance based on their score."""
    if score >= 90:
        return "Excellent"
    elif score >= 70:
        return "Good"
    else:
        return "Needs Improvement"


average_score = calculate_average(performance_scores)

performance_dict = {}
for name, score in zip(employee_names, performance_scores):
    performance_dict[name] = classify_performance(score)

print("Employee Names:", employee_names)
print("Performance Scores:", performance_scores)
print(f"\nAverage Score: {average_score:.2f}")

print("\nEmployee Performance Categories:")
for name, category in performance_dict.items():
    print(f"{name}: {category}")
