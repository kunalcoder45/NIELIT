# CSV -- Comma Separated Values

import pandas as pd

dataset = pd.read_csv('day 11/Dataset.csv')

print("Dataset \n", dataset)

print("Show first 5 rows \n", dataset.head())  # prints first 5 rows of the dataset
print("Show last 5 rows \n", dataset.tail())  # prints last 5 rows of the dataset
print("Statistical summary \n", dataset.describe())  # prints statistical summary of the dataset
print("Dataset info \n", dataset.info())  # prints information about the dataset