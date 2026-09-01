"""
U3&U4 Stats Q8. EDA Using Iris Dataset
A botanist wants to determine which Iris species has the largest average
petal length.

a) Group the data according to species.
b) Calculate the average petal_length for each species.
c) Identify the species with the highest average petal length.
d) State one conclusion from the analysis.
"""
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

# a & b
avg_petal_length = df.groupby("species", observed=True)["petal length (cm)"].mean()
print("a & b) Average petal length by species:")
print(avg_petal_length)

# c
top_species = avg_petal_length.idxmax()
print(f"\nc) Species with the highest average petal length: {top_species}")

# d
print(f"\nd) Conclusion: {top_species} flowers tend to have noticeably larger petals than the")
print("   other species, making petal length a useful feature for identifying this species.")
