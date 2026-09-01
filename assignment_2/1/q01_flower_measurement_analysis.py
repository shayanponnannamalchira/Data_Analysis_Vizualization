"""
Q1. Flower Measurement Analysis
A botanical researcher wants to understand the typical characteristics of flowers
in the Iris dataset.

Calculate the mean, median, and mode of sepal length and petal length.
What do these statistics tell the researcher about the typical flower measurements?
"""
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = iris.target

for col in ["sepal length (cm)", "petal length (cm)"]:
    mean_val = df[col].mean()
    median_val = df[col].median()
    mode_val = df[col].mode()[0]
    print(f"--- {col} ---")
    print(f"Mean   : {mean_val:.3f}")
    print(f"Median : {median_val:.3f}")
    print(f"Mode   : {mode_val:.3f}\n")

print("Interpretation: The mean and median for sepal length are close, suggesting a fairly")
print("symmetric distribution. Petal length has a bigger mean-median gap because the dataset")
print("mixes three species with quite different petal sizes, making the distribution multimodal")
print("rather than a single 'typical' value.")
