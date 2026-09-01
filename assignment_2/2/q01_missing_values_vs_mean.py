"""
U3&U4 Interview Q1. Missing Values vs Mean
A dataset contains a numerical column where 30% of the values are missing and
the remaining values contain extreme outliers. Would you use fillna(mean)?
Why or why not? What alternative would you consider?
"""
import numpy as np
import pandas as pd

np.random.seed(0)
data = np.concatenate([np.random.normal(50, 5, 65), [500, 520, 510]])  # outliers included
s = pd.Series(data)
mask = np.random.choice([True, False], size=len(s), p=[0.3, 0.7])
s_missing = s.mask(mask)

print(f"Mean (with outliers): {s_missing.mean():.2f}")
print(f"Median (with outliers): {s_missing.median():.2f}")

filled_mean = s_missing.fillna(s_missing.mean())
filled_median = s_missing.fillna(s_missing.median())

print(f"\nAfter fillna(mean), new overall mean: {filled_mean.mean():.2f}")
print(f"After fillna(median), new overall mean: {filled_median.mean():.2f}")

print("""
Answer: No, fillna(mean) is not ideal here. With extreme outliers, the mean itself is
pulled away from the "typical" value, so filling missing values with it propagates that
distortion into 30% of the dataset. A better alternative is to fill with the median
(robust to outliers), or to first treat/cap the outliers and then impute, or use a
model-based imputation (e.g., KNNImputer) that considers other correlated columns.
""")
