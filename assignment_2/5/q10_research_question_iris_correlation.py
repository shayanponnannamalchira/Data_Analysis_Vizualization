"""
U3&U4 Stats Q10. Research Question - Iris Dataset
"Is sepal length related to petal length in Iris flowers?"

a) Calculate the correlation between sepal_length and petal_length.
b) Calculate their covariance.
c) Based on the correlation value, state whether the relationship is weak,
   moderate, or strong.
d) State whether the relationship is positive or negative.
"""
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# a
corr = df["sepal length (cm)"].corr(df["petal length (cm)"])
print(f"a) Correlation: {corr:.4f}")

# b
cov = df["sepal length (cm)"].cov(df["petal length (cm)"])
print(f"b) Covariance: {cov:.4f}")

# c
if abs(corr) >= 0.7:
    strength = "strong"
elif abs(corr) >= 0.4:
    strength = "moderate"
else:
    strength = "weak"
print(f"c) Relationship strength: {strength} (|r| = {abs(corr):.2f})")

# d
direction = "positive" if corr > 0 else "negative"
print(f"d) Relationship direction: {direction}")
