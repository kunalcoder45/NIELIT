# CSV -- Comma Separated Values

import pandas as pd

dataset = pd.read_csv('day 11/Dataset.csv')

# print("Dataset \n", dataset)

# print("Show first 5 rows \n", dataset.head())  # prints first 5 rows of the dataset
# print("Show last 5 rows \n", dataset.tail())  # prints last 5 rows of the dataset
# print("Statistical summary \n", dataset.describe())  # prints statistical summary of the dataset
# print("Dataset info \n", dataset.info())  # prints information about the dataset

# print(dataset.shape)  # prints the shape of the dataset (rows, columns  
# print(dataset.columns)  # prints the column names of the dataset
# print(dataset.dtypes)  # prints the data types of each column
# print(dataset.index)  # prints the index of the dataset
# print(dataset["price"].unique())  # prints unique values in column2
# print(dataset["price"].value_counts())  # prints counts of unique values in column2
# print(dataset["price"].mean())  # prints mean of column2
# print(dataset["price"].median())  # prints median of column2


