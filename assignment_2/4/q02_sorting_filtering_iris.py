"""
U4 Q2. Sorting and Filtering - Iris Dataset
A botanist wants to identify flowers with larger petals from the Iris dataset.

a) Display flowers whose petal length is greater than 5 cm.
b) Sort the filtered records in descending order of petal width.
c) Display only the sepal length, petal length, and species columns.
"""
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

# a
large_petals = df[df["petal length (cm)"] > 5]
print("a) Flowers with petal length > 5 cm:")
print(large_petals.head())

# b
sorted_df = large_petals.sort_values("petal width (cm)", ascending=False)
print("\nb) Sorted by petal width (descending):")
print(sorted_df.head())

# c
result = sorted_df[["sepal length (cm)", "petal length (cm)", "species"]]
print("\nc) Selected columns only:")
print(result.head())
