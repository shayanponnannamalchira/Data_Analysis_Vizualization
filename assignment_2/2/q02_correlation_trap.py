"""
U3&U4 Interview Q2. Correlation Trap
A dataset shows a correlation of 0.95 between two variables. Can you conclude
that one variable causes the other? Explain with an example.
"""
import numpy as np
import pandas as pd

np.random.seed(1)
month = np.arange(1, 13)
ice_cream_sales = month * 10 + np.random.normal(0, 2, 12)
drowning_incidents = month * 2 + np.random.normal(0, 1, 12)

df = pd.DataFrame({"month": month, "ice_cream_sales": ice_cream_sales,
                    "drowning_incidents": drowning_incidents})
print(df)
print(f"\nCorrelation: {df['ice_cream_sales'].corr(df['drowning_incidents']):.3f}")

print("""
Answer: No. Correlation measures association, not causation. In this classic example,
ice cream sales and drowning incidents are both driven by a third, "confounding" variable
- warmer weather/summer months - not by one causing the other. A high correlation of 0.95
could similarly arise from a lurking third variable, reverse causation, or coincidence, so
causal claims require controlled experiments or causal-inference techniques, not correlation
alone.
""")
