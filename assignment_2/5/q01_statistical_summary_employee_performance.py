"""
U3&U4 Stats Q1. Statistical Summary - Employee Performance
Performance scores of 8 employees:
E1:72 E2:85 E3:90 E4:72 E5:88 E6:95 E7:72 E8:86

a) Mean and median performance score.
b) Mode of the performance scores.
c) Variance and standard deviation.
"""
import pandas as pd

scores = pd.Series([72, 85, 90, 72, 88, 95, 72, 86],
                    index=["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8"])

print(f"a) Mean: {scores.mean():.2f}, Median: {scores.median():.2f}")
print(f"b) Mode: {scores.mode().tolist()}")
print(f"c) Variance: {scores.var():.2f}, Standard Deviation: {scores.std():.2f}")
