"""
U3&U4 Stats Q5. Outlier Detection - Employee Salaries
Salaries (in Rs thousands): [30, 32, 35, 34, 31, 36, 33, 35, 34, 120]

a) Calculate Q1 and Q3.
b) Calculate the IQR and determine the lower and upper bounds.
c) Identify the outlier(s).
d) State why detecting outliers is important before performing statistical
   analysis.
"""
import pandas as pd

salaries = pd.Series([30, 32, 35, 34, 31, 36, 33, 35, 34, 120])

# a
Q1 = salaries.quantile(0.25)
Q3 = salaries.quantile(0.75)
print(f"a) Q1: {Q1}, Q3: {Q3}")

# b
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
print(f"b) IQR: {IQR}, Lower bound: {lower_bound}, Upper bound: {upper_bound}")

# c
outliers = salaries[(salaries < lower_bound) | (salaries > upper_bound)]
print(f"c) Outlier(s): {outliers.tolist()}")

# d
print("""
d) Outliers can heavily distort summary statistics like the mean and standard deviation,
lead to misleading conclusions, and negatively affect the performance of many statistical
models (which assume roughly normal, well-behaved data). Detecting them first allows an
analyst to decide whether to investigate, treat, or exclude them before further analysis.
""")
