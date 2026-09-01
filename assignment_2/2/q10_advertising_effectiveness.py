"""
U3&U4 Interview Q10. Question
You calculate the following statistics for a sales dataset:
- Mean: Rs 52,000
- Median: Rs 35,000
- Standard Deviation: Rs 48,000
- Correlation between advertising expenditure and sales: 0.15

The marketing manager says, "Our advertising strategy is highly effective."
As a data analyst, would you agree with this conclusion? What additional
EDA would you perform before making a decision?
"""
print(f"Mean: Rs 52,000 | Median: Rs 35,000 | Std Dev: Rs 48,000 | Corr(ad, sales): 0.15")

print("""
Answer: No, I would not agree. A correlation of only 0.15 between advertising expenditure
and sales is weak, suggesting advertising spend explains very little of the variation in
sales - this contradicts the claim that the strategy is "highly effective." Also, the
large gap between mean (52,000) and median (35,000), plus a very high standard deviation
(48,000) relative to the median, indicates the sales data is right-skewed with high
variability, likely driven by a few large sales - the "average effectiveness" picture is
distorted by these outliers.

Additional EDA before deciding:
1. Plot a scatter plot of advertising spend vs. sales to visually inspect the relationship
   and check for non-linear patterns or outlier-driven correlation.
2. Segment analysis - check correlation within customer segments, regions, or time periods
   separately, since aggregated correlation can mask sub-group effects.
3. Check for outliers in both sales and advertising expenditure using the IQR method.
4. Consider time-lag effects (advertising today may affect sales next month) and control
   for other factors (seasonality, promotions, pricing) before attributing sales to ads.
""")
