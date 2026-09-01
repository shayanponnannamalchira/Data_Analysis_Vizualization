"""
U3&U4 Interview Q7. Statistical Summary Trap
Two datasets have the same mean and median but very different standard
deviations. What does this tell you about the two datasets?
"""
import numpy as np
import pandas as pd

np.random.seed(2)
d1 = np.random.normal(50, 2, 1000)
d2 = np.random.normal(50, 15, 1000)

print(f"Dataset 1 - mean: {d1.mean():.2f}, median: {np.median(d1):.2f}, std: {d1.std():.2f}")
print(f"Dataset 2 - mean: {d2.mean():.2f}, median: {np.median(d2):.2f}, std: {d2.std():.2f}")

print("""
Answer: Equal mean/median but different standard deviations means both datasets have the
same central tendency, but Dataset 2 is far more spread out / variable than Dataset 1.
Central tendency alone doesn't describe a dataset fully - two datasets can look identical
"on average" yet have very different risk, consistency, or reliability, which is why
spread measures (variance/std) must always be reported alongside mean/median.
""")
