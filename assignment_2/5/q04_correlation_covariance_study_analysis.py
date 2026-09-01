"""
U3&U4 Stats Q4. Correlation and Covariance - Study Analysis
Study_Hours vs Marks for 6 students:
S1:(2,45) S2:(3,50) S3:(4,58) S4:(5,65) S5:(6,70) S6:(7,78)

a) Calculate the correlation between Study_Hours and Marks.
b) Calculate their covariance.
c) Interpret whether the relationship is positive or negative.
"""
import pandas as pd

df = pd.DataFrame({
    "Study_Hours": [2, 3, 4, 5, 6, 7],
    "Marks": [45, 50, 58, 65, 70, 78],
})

# a
corr = df["Study_Hours"].corr(df["Marks"])
print(f"a) Correlation: {corr:.4f}")

# b
cov = df["Study_Hours"].cov(df["Marks"])
print(f"b) Covariance: {cov:.4f}")

# c
print(f"\nc) Since the correlation ({corr:.2f}) and covariance ({cov:.2f}) are both positive,")
print("   the relationship is positive - more study hours are associated with higher marks.")
