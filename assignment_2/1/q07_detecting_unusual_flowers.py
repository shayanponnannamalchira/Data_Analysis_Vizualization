"""
Q7. Detecting Unusual Flowers
A quality-control researcher wants to identify flowers whose petal length is
unusually high or low.

Use the IQR method to identify possible outliers in the petal length variable.
How many potential outliers are present?
"""
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

Q1 = df["petal length (cm)"].quantile(0.25)
Q3 = df["petal length (cm)"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["petal length (cm)"] < lower_bound) | (df["petal length (cm)"] > upper_bound)]

print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
print(f"Lower bound: {lower_bound}, Upper bound: {upper_bound}")
print(f"Number of potential outliers in petal length: {len(outliers)}")
print(outliers[["petal length (cm)"]])
