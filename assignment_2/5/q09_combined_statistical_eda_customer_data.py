"""
U3&U4 Stats Q9. Combined Statistical EDA - Customer Data
Customer Age/Spending data for 8 customers (C1-C8).

a) Find the mean and median age.
b) Find the mode of age.
c) Calculate the standard deviation of age.
d) State whether the mean and median indicate any noticeable difference in
   the age distribution.
"""
import pandas as pd

df = pd.DataFrame({
    "Customer": ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"],
    "Age": [21, 25, 25, 28, 30, 30, 32, 45],
    "Spending": [2000, 3500, 4000, 4500, 5000, 5500, 6000, 7000],
})

# a
mean_age = df["Age"].mean()
median_age = df["Age"].median()
print(f"a) Mean age: {mean_age:.2f}, Median age: {median_age:.2f}")

# b
mode_age = df["Age"].mode().tolist()
print(f"b) Mode of age: {mode_age}")

# c
std_age = df["Age"].std()
print(f"c) Standard deviation of age: {std_age:.2f}")

# d
diff = mean_age - median_age
print(f"\nd) Mean - Median = {diff:.2f}. The mean is somewhat higher than the median, indicating")
print("   a slight right skew - likely caused by the 45-year-old customer (C8), an older outlier")
print("   pulling the mean upward relative to the bulk of younger customers.")
