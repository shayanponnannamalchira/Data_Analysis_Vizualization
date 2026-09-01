"""
Q8. Research Question Using EDA
A botanist wants to determine: "Can flower measurements help distinguish
different Iris species?"

Use Pandas to calculate summary statistics for each species and examine the
relationships between sepal length, sepal width, petal length, and petal width.
Based on your EDA, identify which measurements appear most useful for
distinguishing species.
"""
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

print("Summary statistics per species:")
print(df.groupby("species").describe().T)

print("\nCorrelation matrix among numerical features:")
print(df.drop(columns="species").corr())

print("\nConclusion: Petal length and petal width show the clearest separation between")
print("species (their per-species means differ the most relative to their spread), making")
print("them the most useful measurements for distinguishing Iris species. Sepal width")
print("overlaps heavily across species and is the least useful on its own.")
