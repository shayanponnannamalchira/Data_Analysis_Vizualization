"""
U3&U4 Stats Q3. Cross-Tabulation - Titanic Dataset
A researcher wants to investigate whether passenger gender and passenger
class were related to survival on the Titanic.

a) Create a cross-tabulation of Sex against Pclass.
b) Create a cross-tabulation of Sex against Survived.
c) State one observation from the resulting table.
"""
import seaborn as sns
import pandas as pd

df = sns.load_dataset("titanic")

# a
print("a) Sex vs Pclass:")
print(pd.crosstab(df["sex"], df["pclass"]))

# b
print("\nb) Sex vs Survived:")
print(pd.crosstab(df["sex"], df["survived"]))

# c
print("""
c) Observation: Female passengers had a much higher count of survivors relative to their
total count than male passengers did, indicating gender was strongly associated with
survival likelihood.
""")
