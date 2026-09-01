"""
Q2. Variation in Flower Size
A researcher observes that flowers belonging to the same species may have different
measurements.

Calculate the variance and standard deviation of sepal length for the Iris dataset.
Which measure gives a better understanding of the spread of the data? Explain.
"""
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

variance = df["sepal length (cm)"].var()
std_dev = df["sepal length (cm)"].std()

print(f"Variance of sepal length: {variance:.4f} (cm^2)")
print(f"Standard deviation of sepal length: {std_dev:.4f} (cm)")

print("\nInterpretation: Standard deviation gives a better intuitive understanding of spread")
print("because it is expressed in the same unit (cm) as the original measurement, whereas")
print("variance is in squared units (cm^2) and is harder to relate back to the data directly.")
