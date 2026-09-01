"""
Module 6, Case Study 6: Iris Dataset Multi-Variable Analysis
The Iris dataset contains: Sepal length, Sepal width, Petal length,
Petal width, Species.

a) Which Seaborn plot is most suitable for multi-variable analysis?
b) Explain how this plot shows relationships between variables.
c) Write a Seaborn program to generate this plot.
d) State two insights that can be obtained from this visualization.
"""
import seaborn as sns
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

print("""
a) A Pair Plot (sns.pairplot) is most suitable for multi-variable analysis of the Iris
   dataset.

b) A pair plot creates a grid of scatter plots for every pair of numerical variables
   (with histograms/KDEs on the diagonal), and when colored by a categorical variable like
   species, it reveals how each pair of features relates to one another and how well the
   species separate across all feature combinations simultaneously.
""")

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

pairplot = sns.pairplot(df, hue="species", palette="Set2")
pairplot.fig.suptitle("Iris Dataset - Pair Plot", y=1.02)
pairplot.savefig("m6_cs6_iris_pairplot.png")
plt.close("all")
print("Saved pair plot to m6_cs6_iris_pairplot.png")

print("""
d) Insights:
1. Petal length and petal width are strongly, almost linearly, correlated with each other.
2. Setosa is clearly separated from versicolor and virginica across nearly every feature
   pair, especially petal measurements, while versicolor and virginica show some overlap.
""")
