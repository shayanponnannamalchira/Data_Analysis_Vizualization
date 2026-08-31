"""
Q22. Hospital Patient Data
A hospital stores the ages of patients visiting the outpatient department:
[25, 42, 18, 67, 35, 52, 29, 71]
Write a Python program to:
Find the youngest patient.
Find the oldest patient.
Calculate average age.
Count patients above 60 years.

Topics: Lists, Loops, Conditions, Built-in functions.
"""

ages = [25, 42, 18, 67, 35, 52, 29, 71]

youngest = min(ages)
oldest = max(ages)
average_age = sum(ages) / len(ages)

count_above_60 = 0
for age in ages:
    if age > 60:
        count_above_60 += 1

print("Patient ages:", ages)
print("Youngest patient age:", youngest)
print("Oldest patient age:", oldest)
print(f"Average age: {average_age:.2f}")
print("Number of patients above 60 years:", count_above_60)
