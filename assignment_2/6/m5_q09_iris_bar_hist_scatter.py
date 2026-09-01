"""
Module 5, Q9. The Iris dataset contains information about different types of
flowers. Explain how Bar chart, Histogram, and Scatter plot can be used to
analyze this dataset.
"""
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

print("""
Bar chart: Used to show the count of flowers per species (a categorical summary) - e.g.,
how many setosa, versicolor, and virginica samples are in the dataset.

Histogram: Used to show the distribution of a single numeric feature, such as petal
length, revealing whether values cluster together, are skewed, or show multiple peaks
(which can hint at multiple species mixed together).

Scatter plot: Used to examine the relationship between two numeric features, such as
petal length vs. petal width, and (when colored by species) to see how well the species
separate based on those two measurements.
""")

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

df["species"].value_counts().plot(kind="bar", ax=axes[0], color="#4c72b0")
axes[0].set_title("Bar Chart: Species Count")

axes[1].hist(df["petal length (cm)"], bins=15, color="#dd8452", edgecolor="black")
axes[1].set_title("Histogram: Petal Length Distribution")

colors = {"setosa": "#4c72b0", "versicolor": "#dd8452", "virginica": "#55a868"}
for sp, group in df.groupby("species", observed=True):
    axes[2].scatter(group["petal length (cm)"], group["petal width (cm)"],
                     label=sp, color=colors[sp], alpha=0.7)
axes[2].set_title("Scatter Plot: Petal Length vs Width")
axes[2].set_xlabel("Petal Length (cm)")
axes[2].set_ylabel("Petal Width (cm)")
axes[2].legend()

plt.tight_layout()
plt.savefig("m5_q09_iris_charts.png")
print("Saved charts to m5_q09_iris_charts.png")
