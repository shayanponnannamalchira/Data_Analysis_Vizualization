"""
Q27. Duplicate Data Detection
A company receives customer IDs from multiple branches:
[101, 102, 103, 101, 104, 102, 105, 103]
Write a Python program to identify duplicate customer IDs and generate a list of unique customer IDs.

Topics: Lists, Sets, Loops.
"""

customer_ids = [101, 102, 103, 101, 104, 102, 105, 103]

seen = set()
duplicates = set()

for cid in customer_ids:
    if cid in seen:
        duplicates.add(cid)
    else:
        seen.add(cid)

unique_ids = list(set(customer_ids))
unique_ids.sort()

print("Original customer IDs:", customer_ids)
print("Duplicate customer IDs:", sorted(duplicates))
print("Unique customer IDs:", unique_ids)
