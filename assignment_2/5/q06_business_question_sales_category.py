"""
U3&U4 Stats Q6. Business Question Using Pandas EDA - Sales Dataset
"Which product category generates the highest average sales?"

a) Group the data by Category.
b) Calculate the average sales for each category.
c) Identify the category with the highest average sales.
d) Write one business conclusion based on the result.
"""
import pandas as pd

df = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Chair", "Table", "Mobile", "Sofa"],
    "Category": ["Electronics", "Electronics", "Furniture", "Furniture", "Electronics", "Furniture"],
    "Sales": [60000, 1500, 8000, 12000, 25000, 30000],
})

# a & b
avg_sales = df.groupby("Category")["Sales"].mean()
print("a & b) Average sales by category:")
print(avg_sales)

# c
top_category = avg_sales.idxmax()
print(f"\nc) Category with highest average sales: {top_category}")

# d
print(f"\nd) Business conclusion: {top_category} generates the highest average sales, so the")
print("   company should consider prioritizing marketing spend and inventory investment in this")
print("   category to maximize revenue.")
