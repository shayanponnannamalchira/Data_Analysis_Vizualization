"""
U4 Q5. Feature Engineering - Titanic Dataset
A researcher wants to determine whether the size of a passenger's family
affected their survival.

a) Create FamilySize using sibsp + parch + 1.
b) Create FamilyType where FamilySize == 1 is "Alone", others are "Family".
c) Display the first five records with these newly created features.
"""
import seaborn as sns

df = sns.load_dataset("titanic")

# a
df["FamilySize"] = df["sibsp"] + df["parch"] + 1

# b
df["FamilyType"] = df["FamilySize"].apply(lambda x: "Alone" if x == 1 else "Family")

# c
print("First five records with FamilySize and FamilyType:")
print(df[["sibsp", "parch", "FamilySize", "FamilyType", "survived"]].head())
