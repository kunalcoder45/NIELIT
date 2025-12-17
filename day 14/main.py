# Matplotlib

import matplotlib.pyplot as plt
import numpy as np

# vertical bar graph

# obj = ('Python', 'C++', 'Java', 'Ruby', 'Perl', 'Scala')
# clr_list=['red', 'blue', 'green', 'yellow', 'orange', 'purple']
# y_pos = np.arange(len(obj))
# performance = [10,8,6,4,2,1]
# plt.bar(y_pos, performance, align='center', alpha=0.7, color=clr_list)
# plt.xticks(y_pos, obj)
# plt.ylabel('Usage')
# plt.title('Programming language usage')
# plt.show()

# horizontal bar graph

# obj = ('Python', 'C++', 'Java', 'Ruby', 'Perl', 'Scala')
# y_pos = np.arange(len(obj))
# performance = [10,8,6,4,2,1]
# plt.barh(y_pos, performance, align='center', alpha=0.7)
# plt.yticks(y_pos, obj)
# plt.xlabel('Usage')
# plt.title('Programming language usage')
# plt.show()


# x = [1,2,3,4,5,6,7,8,9]
# y = [10,2,3,6,4,9,7,4,2]
# x2 = [1,2,3,4,5,6,7,8,9]
# y2 = [2,4,7,9,5,3,8,10,2]

# plt.bar(x, y, label='Bar 1', color='b')
# plt.bar(x2, y2, label='Bar 2', color='r')

# plt.legend()
# plt.title('Bar graph with multiple bars')
# plt.xlabel('Order')
# plt.ylabel('Count')
# plt.show()

# x= [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,65,60,49,50,100]
# num_bins = 10
# pawankala= 'black'
# plt.hist(x, num_bins, edgecolor=pawankala, color='r', alpha=0.7)
# plt.xlabel('Distribution')
# plt.ylabel('Frequency')
# plt.title('Histogram Chart')
# plt.show()


#  Create a bar graph showing the marks of 5 students: [65, 70, 80, 75, 90]. Label both axes

# students = ['Aniket', 'Indrajeet', 'Kunal', 'Rishav', 'Sameer']
# marks = [65, 70, 80, 75, 90]
# y_pos = np.arange(len(students))
# plt.bar(y_pos, marks, align='center', alpha=0.7, color='orange')
# plt.xticks(y_pos, students)
# plt.ylabel('Marks of Students')
# plt.xlabel('Students Names')
# plt.title('Marks of 6 Students')
# plt.show()

#  Draw a bar graph for sales of products A, B, C, and D with values [150, 200, 180, 220]. Add a title.

# products = ['A', 'B', 'C', 'D']
# sales = [150, 200, 180, 220]
# y_pos = np.arange(len(products))
# plt.bar(y_pos, sales, align='center', alpha=0.7, color='green')
# plt.xticks(y_pos, products)
# plt.ylabel('Sales')
# plt.xlabel('Products')
# plt.title('Sales of Products A, B, C, and D')
# plt.show()

# Plot a bar graph representing the population of 5 cities using different colors

# cities = ['Jamshedpur', 'Ranchi', 'Bhubaneswar', 'Kolkata', 'Mumbai']
# population = [1.5, 2.3, 3.1, 4.0, 2.8]
# colors = ['red', 'blue', 'green', 'orange', 'purple']
# y_pos = np.arange(len(cities))
# plt.bar(y_pos, population, align='center', alpha=0.7, color=colors)
# plt.xticks(y_pos, cities)
# plt.ylabel('Population (in millions)')
# plt.xlabel('Cities')
# plt.title('Population of 5 Cities')
# plt.show()

# Create a histogram for the data [12, 15, 20, 20, 25, 30, 35, 40, 45, 50] using 5 bins.
data = [12, 15, 20, 20, 25, 30, 35, 40, 45, 50]
num_bins = 5
plt.hist(data, num_bins, edgecolor='black', color='cyan', alpha=0.7)
plt.xlabel('Value Ranges')
plt.ylabel('Frequency')
plt.title('Histogram of Given Data')
plt.show()