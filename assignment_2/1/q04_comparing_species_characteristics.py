"""
Q4. Comparing Species Characteristics
A researcher wants to compare the average petal length among the three Iris species.

Use Pandas to calculate the average petal length for each species.
Which species has the highest average petal length?
"""
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

avg_petal_length = df.groupby("species")["petal length (cm)"].mean()
print("Average petal length per species:")
print(avg_petal_length)

highest = avg_petal_length.idxmax()
print(f"\nSpecies with the highest average petal length: {highest}")
