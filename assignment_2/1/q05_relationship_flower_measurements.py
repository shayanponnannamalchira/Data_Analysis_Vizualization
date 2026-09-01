"""
Q5. Relationship Between Flower Measurements
A botanist suspects that flowers with longer sepals may also have longer petals.

Calculate the correlation between sepal length and petal length.
Interpret the result and determine whether the researcher's assumption is supported.
"""
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

corr = df["sepal length (cm)"].corr(df["petal length (cm)"])
print(f"Correlation between sepal length and petal length: {corr:.3f}")

print("\nInterpretation: A correlation around 0.87 indicates a strong positive linear")
print("relationship - as sepal length increases, petal length also tends to increase.")
print("This supports the researcher's assumption.")
