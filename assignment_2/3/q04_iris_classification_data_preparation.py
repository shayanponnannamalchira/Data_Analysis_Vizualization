"""
U3 Q4 - Iris Dataset: Flower Classification Data Preparation
A botanist wants to analyze the Iris dataset before developing a
machine-learning model to classify flowers.

1. Load the dataset, check for missing values.
2. Check for and remove duplicate observations.
3. Rename feature columns as Sepal_Length, Sepal_Width, Petal_Length,
   Petal_Width.
4. Filter flowers having Petal_Length > 5.0, sort by Petal_Width.
5. Group by species, calculate average of each numerical feature.
6. Create Petal_Area = Petal_Length * Petal_Width.
7. Encode the categorical Species column numerically.
8. Perform a basic data-quality check.
"""
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["Species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

# 1. Missing values
print("Missing values:")
print(df.isnull().sum())

# 2. Duplicates
print(f"\nDuplicate observations: {df.duplicated().sum()}")
df = df.drop_duplicates()

# 3. Rename columns
df = df.rename(columns={
    "sepal length (cm)": "Sepal_Length",
    "sepal width (cm)": "Sepal_Width",
    "petal length (cm)": "Petal_Length",
    "petal width (cm)": "Petal_Width",
})

# 4. Filter and sort
filtered = df[df["Petal_Length"] > 5.0].sort_values("Petal_Width")
print("\nFlowers with Petal_Length > 5.0, sorted by Petal_Width:")
print(filtered.head())

# 5. Group by species
print("\nAverage of each numerical feature by species:")
print(df.groupby("Species", observed=True).mean(numeric_only=True))

# 6. Petal_Area
df["Petal_Area"] = df["Petal_Length"] * df["Petal_Width"]

# 7. Encode species
df["Species_encoded"] = df["Species"].cat.codes

# 8. Data-quality check
print(f"\nAny negative/invalid numeric values? {(df.select_dtypes('number') < 0).any().any()}")
print(f"Remaining missing values: {df.isnull().sum().sum()}")
print(f"Remaining duplicates: {df.duplicated().sum()}")
