"""
Q6. Covariance Analysis
A researcher wants to determine whether sepal length and petal length tend to
increase together.

Calculate the covariance between sepal length and petal length.
What does the sign of the covariance indicate?
"""
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

covariance = df["sepal length (cm)"].cov(df["petal length (cm)"])
print(f"Covariance between sepal length and petal length: {covariance:.4f}")

print("\nInterpretation: A positive covariance means the two variables tend to move in the")
print("same direction - as sepal length increases, petal length also tends to increase.")
print("(Unlike correlation, covariance is not standardized, so its magnitude is harder to")
print("interpret directly and depends on the units/scale of the variables.)")
