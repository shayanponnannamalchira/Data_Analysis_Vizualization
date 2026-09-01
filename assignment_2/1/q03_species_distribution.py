"""
Q3. Species Distribution
A botanist wants to know how many flowers belong to each Iris species.

Create a frequency distribution showing the number of observations for each species.
Represent the result using a suitable visualization.
"""
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

freq = df["species"].value_counts()
print("Frequency distribution of species:")
print(freq)

freq.plot(kind="bar", color=["#4c72b0", "#dd8452", "#55a868"])
plt.title("Frequency Distribution of Iris Species")
plt.xlabel("Species")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("q03_species_distribution.png")
print("Saved bar chart to q03_species_distribution.png")
