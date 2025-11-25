import pandas as pd

# 1)
# d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#      'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# }

# df = pd.DataFrame(d)
# print("First\n",df)
# print("Second\n",df['one'])
# print("Third\n",df['two'])

# 2)
# data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#         'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
#         'three': pd.Series([10, 20, 30], index=['a', 'b', 'c'])
# }

# df = pd.DataFrame(data)
# print(df)
# del df['one'] # deleting column 'one' using del keyword and delete function 
# print(df)
# df.pop('two') # deleting column 'two' using pop function and keyword
# print(df)

# 3)
# data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#         'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# }

# df = pd.DataFrame(data)
# new = df['three'] = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
# print(df)

# add = df['four'] = new + df['two'] + df['one']
# print(df)

# 4)
# data = pd.DataFrame({'Age': [25, 30, 35, 40],
#                      'color': ['Red', 'Blue', 'Green', 'Black'],
#                      'Height': [5.5, 6.0, 5.8, 5.9],
#                      'food': ['Pizza', 'Burger', 'Salad', 'Pasta'],
#                      'score': [85, 90, 95, 80],
#                      'state': ['NY', 'CA', 'TX', 'FL']
#                     },
#                     index=['a', 'b', 'c', 'd'])

# print("Original DataFrame:\n", data)
# print(data.loc['b'])

