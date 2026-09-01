"""
U4 Q6. Encoding Categorical Variables - Iris Dataset
A machine-learning model requires numerical input instead of text labels.

a) Identify the categorical species column.
b) Convert the species categories into numerical values using an appropriate
   encoding technique.
c) Display the original and encoded values together for verification.
"""
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

# a
print(f"a) Categorical column: 'species' (dtype: {df['species'].dtype})")

# b - Label encoding (ordinal not implied, but suitable for tree-based models)
df["species_encoded"] = df["species"].cat.codes

# c
print("\nc) Original vs encoded species:")
print(df[["species", "species_encoded"]].drop_duplicates().reset_index(drop=True))
