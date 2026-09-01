"""
U3&U4 Interview Q9. Pandas EDA Challenge
If df.describe() shows a very high maximum value compared with the 75th
percentile, what would you investigate next and why?
"""
print("""
Answer: A maximum value far above the 75th percentile is a red flag for potential
outliers or right-skew in that column. Next steps:
1. Compute the IQR (Q3 - Q1) and check how far the max lies beyond Q3 + 1.5*IQR.
2. Visualize the column with a boxplot or histogram to see the shape of the distribution.
3. Investigate the specific record(s) with the extreme value - check whether it's a
   genuine value, a data-entry error, or a different unit/scale by mistake.
4. Decide on treatment: keep, cap/winsorize, transform (e.g., log), or remove, depending
   on whether the value is genuine and how it affects the intended analysis/model.
""")
