"""
U3&U4 Stats Q2. Frequency Distribution - Customer Ratings
Ratings = [5, 4, 5, 3, 4, 5, 2, 4, 3, 5, 4, 3]

a) Create a frequency distribution showing the number of customers giving
   each rating.
b) Identify the most frequently given rating.
c) Briefly state what the frequency distribution indicates about customer
   satisfaction.
"""
import pandas as pd

ratings = pd.Series([5, 4, 5, 3, 4, 5, 2, 4, 3, 5, 4, 3])

# a
freq = ratings.value_counts().sort_index()
print("a) Frequency distribution:")
print(freq)

# b
most_common = ratings.mode()[0]
print(f"\nb) Most frequently given rating: {most_common}")

# c
print("""
c) Interpretation: Ratings of 4 and 5 are the most common, together making up over half of
all responses, while very low ratings (2) are rare. This suggests overall customer
satisfaction is fairly high, though there is still a spread of opinions worth investigating.
""")
