"""
Q12. Age Variation by Passenger Class
A researcher wants to compare the ages of passengers belonging to different classes.

Calculate the mean, median, variance, and standard deviation of age for each
passenger class. Which class shows the greatest variation in passenger age?
"""
import seaborn as sns
import pandas as pd

df = sns.load_dataset("titanic")

stats = df.groupby("class")["age"].agg(["mean", "median", "var", "std"])
print("Age statistics by passenger class:")
print(stats)

most_variable_class = stats["std"].idxmax()
print(f"\nClass with the greatest variation in age: {most_variable_class}")
