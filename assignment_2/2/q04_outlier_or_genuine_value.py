"""
U3&U4 Interview Q4. Outlier or Genuine Value?
An employee dataset contains one employee with a salary of Rs 10 lakh while most
salaries are between Rs 30,000 and Rs 80,000. Would you automatically remove
this value as an outlier? Why or why not?
"""
print("""
Answer: No, it should not be automatically removed. Statistically it is an outlier
(far outside the IQR-based bounds of the rest of the data), but that doesn't mean it's
an error - it could be a genuine value for a senior executive, founder, or specialist role.
Before removing it, investigate the context: check the employee's role/designation,
verify the value isn't a data-entry error (e.g., extra digit), and consider whether it
should be kept but treated separately (e.g., analyzed by role/band) rather than dropped
outright, since removing genuine high-value data can bias the analysis.
""")
