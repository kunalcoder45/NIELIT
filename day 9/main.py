import pandas as pd

# s=pd.Series([1, 3, 5, 7, 9], index=['a', 'b', 'c', 'd', 'e'])
# print(s)
# print(s['c'])

# Dataframes are two-dimensional labeled data structures with columns of potentially different types.

# d=pd.DataFrame()
# print(d)

# data2 = {1,2,3,4,5}
# d2=pd.DataFrame(data2)
# print(d2)

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [24, 27, 22, 32],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
# }

# df = pd.DataFrame(data)
# print(df)

# data=[{'a':1,'b':2},{'a':5,'b':10,'c':20}]

# df = pd.DataFrame(data)
# print(df)

# data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#         'two': pd.Series([1, 2, 3, 4], index=['e', 'f', 'g', 'h'])        
# }

# df = pd.DataFrame(data)
# print(df)

# data = {'Student': ['Aniket', 'Kunal', 'Indrajeet', 'Sameer', 'Aditiya'],
#         'Math': [90, 80, 70, 85, 95],
#         'Science': [85, 95, 80, 90, 88],
#         'English': [88, 76, 92, 81, 79],
#         'SST'   : [75, 85, 80, 70, 90],
#         'Hindi' : [80, 70, 75, 85, 88],
# }

data = {'Student': pd.Series(['Kunal', 'Aniket', 'Indrajeet', 'Sameer', 'Aditiya'], index=['1', '2', '3', '4', '5']),
        'Math': pd.Series([90, 80, 70, 85, 95], index=['1', '2', '3', '4', '5']),
        'Science': pd.Series([85, 95, 80, 90, 88], index=['1', '2', '3', '4', '5']),
        'English': pd.Series([88, 76, 92, 81, 79], index=['1', '2', '3', '4', '5']),
        'SST'   : pd.Series([75, 85, 80, 70, 90], index=['1', '2', '3', '4', '5']),
        'Hindi' : pd.Series([80, 70, 75, 85, 88], index=['1', '2', '3', '4', '5']),
}
df = pd.DataFrame(data)
print(df)