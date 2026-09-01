"""
Q18. Open-Ended EDA Question
Scenario: You are a data analyst working for a research organization. You are
given the Iris dataset and are asked to "Find something interesting in the data."

Frame three research questions that can be answered using the dataset. Use
Pandas to perform EDA and provide evidence-based answers to your questions.
"""
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

print("Research Question 1: Does petal size differ meaningfully across species?")
print(df.groupby("species")[["petal length (cm)", "petal width (cm)"]].mean())
print("Answer: Yes - setosa has much smaller petals than versicolor and virginica, and")
print("virginica has the largest, showing clear species-level separation.\n")

print("Research Question 2: Is sepal width a useful feature for distinguishing species?")
print(df.groupby("species")["sepal width (cm)"].agg(["mean", "std"]))
print("Answer: Sepal width means are close across species relative to their spread, so it")
print("is a weak standalone distinguishing feature compared to petal measurements.\n")

print("Research Question 3: Which pair of features is most strongly correlated overall?")
corr = df.select_dtypes(include="number").corr()
print(corr)
print("Answer: Petal length and petal width show the strongest correlation (>0.9),")
print("suggesting they carry largely overlapping information about flower size.")
