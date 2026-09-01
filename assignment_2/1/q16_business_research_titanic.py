"""
Q16. Business/Research Question - Titanic
A data analyst has been asked:
"Which passenger characteristics appear to be associated with survival?"

Perform the following:
1. Generate descriptive statistics.
2. Analyze survival by gender.
3. Analyze survival by passenger class.
4. Examine age distribution.
5. Calculate correlations among numerical variables.
6. Detect outliers in fare.
7. Summarize at least five important findings.
"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

# 1. Descriptive statistics
print("1. Descriptive statistics:")
print(df.describe(include="all"))

# 2. Survival by gender
print("\n2. Survival rate by gender:")
print(df.groupby("sex")["survived"].mean().round(3))

# 3. Survival by class
print("\n3. Survival rate by class:")
print(df.groupby("class")["survived"].mean().round(3))

# 4. Age distribution
print("\n4. Age distribution summary:")
print(df["age"].describe())
df["age"].plot(kind="hist", bins=30, title="Age Distribution")
plt.xlabel("Age")
plt.tight_layout()
plt.savefig("q16_age_distribution.png")
plt.close()

# 5. Correlations
numeric_df = df.select_dtypes(include="number")
print("\n5. Correlation matrix:")
print(numeric_df.corr().round(2))

# 6. Fare outliers
Q1, Q3 = df["fare"].quantile([0.25, 0.75])
IQR = Q3 - Q1
lower, upper = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
fare_outliers = df[(df["fare"] < lower) | (df["fare"] > upper)]
print(f"\n6. Number of fare outliers: {len(fare_outliers)}")

# 7. Findings
print("""
7. Findings:
1. Sex is the strongest single predictor of survival - females survived at a much higher rate.
2. Passenger class strongly influences survival, with first class the highest, third the lowest.
3. Age is right-skewed with several missing values; most passengers were young adults.
4. Fare correlates positively with survival, largely because fare correlates with class.
5. Fare has a substantial number of high-value outliers, mostly first-class passengers.
""")
