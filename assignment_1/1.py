"""
Q1. Student Performance Analysis — Descriptive Analytics
A college maintains marks of 10 students in a subject. 
Write a Python program to calculate the mean, median, maximum, minimum, and standard deviation of the marks. 
Display a short summary describing the overall performance of the class.

Topics: Data Analytics, Descriptive Analytics, Variables, Lists, Built-in functions.
"""
import pandas as pd
import numpy as np

marks = [56, 64, 76, 64, 65, 34, 97, 89, 78, 45]

mean=np.mean(marks)
median=np.median(marks)
max=np.max(marks)
min=np.min(marks)
std=np.std(marks)

print("Mean of marks: ", mean)
print("Median of marks: ", median)
print("Maximum of marks: ", max)
print("Minimum of marks: ", min)
print("Standard deviation of marks: ", std)

