"""
Q17. EDA Challenge - Iris
A plant scientist wants to build a classification model for Iris species but
first wants to understand the data.

Using Pandas:
- Display the first and last five records.
- Find the number of rows and columns.
- Check for missing values.
- Generate descriptive statistics.
- Calculate mean, median, and standard deviation.
- Generate a frequency distribution of species.
- Calculate the correlation matrix.
- Detect outliers.
- Identify the two variables that show the strongest relationship.
- State whether the dataset appears suitable for classification.
"""
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

print("First 5 records:")
print(df.head())
print("\nLast 5 records:")
print(df.tail())

print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nDescriptive statistics:")
print(df.describe())

numeric_cols = df.select_dtypes(include="number").columns
print("\nMean:\n", df[numeric_cols].mean())
print("\nMedian:\n", df[numeric_cols].median())
print("\nStandard deviation:\n", df[numeric_cols].std())

print("\nFrequency distribution of species:")
print(df["species"].value_counts())

corr_matrix = df[numeric_cols].corr()
print("\nCorrelation matrix:")
print(corr_matrix)

# Outlier detection via IQR for each numeric column
print("\nOutlier counts (IQR method):")
for col in numeric_cols:
    Q1, Q3 = df[col].quantile([0.25, 0.75])
    IQR = Q3 - Q1
    lower, upper = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
    n_outliers = ((df[col] < lower) | (df[col] > upper)).sum()
    print(f"  {col}: {n_outliers} outliers")

corr_unstacked = corr_matrix.abs().unstack().sort_values(ascending=False)
corr_unstacked = corr_unstacked[corr_unstacked < 1.0]
strongest_pair = corr_unstacked.index[0]
print(f"\nStrongest relationship: {strongest_pair} (r = {corr_matrix.loc[strongest_pair]:.3f})")

print("\nConclusion: The dataset has no missing values, clear separation in petal measurements")
print("between species, and strong correlations between petal length/width - it appears well")
print("suited for a classification model.")
