"""
U3&U4 Interview Q5. Correlation with Outliers
Suppose two variables have a correlation of 0.8. After removing three outliers,
the correlation becomes 0.2. What does this tell you about the original relationship?
"""
print("""
Answer: This tells us the original correlation of 0.8 was largely driven by those three
outlier points, not by a genuine relationship across the bulk of the data. Correlation is
sensitive to extreme values, so a few influential points can create the appearance of a
strong linear relationship. The drop to 0.2 after removing them reveals that the "real"
relationship among the typical/majority of data points is actually weak. This is a good
reminder to always visualize data (e.g., scatter plot) rather than relying on the
correlation coefficient alone.
""")
