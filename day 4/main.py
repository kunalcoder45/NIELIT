# functions

# two types of functions
# 1. built-in functions
# 2. user-defined functions

# def name():
#     return "Kunal"

# name_var = name()
# print(name_var)


# def addNo(a, b):
#     return a + b
# result = addNo(5, 10)
# print(result)

# def add():
#     a=5
#     b=10
#     c = a + b
#     return c
# print(add())

# def fun():
#     for i in range(5):
#         print("Hello World")
# fun()

# Q1

# def greet():
#     print("Hello, welcome to Python!")
# greet()

# # Q2

# def addNo(a, b):
#     return a + b
# result = addNo(5, 10)
# print(result)

# # Q3
# def sqare(num):
#     return num * num

# inputNo = int(input("Enter a number: "))
# print(sqare(inputNo))

# Q4

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# inputNo = int(input("Enter a number: "))
# print(is_even(inputNo))

# Q5
# def multiply(a, b, c):
#     return a * b * c
# result = multiply(2, 3, 4)
# print(result)

# Q6

# def largestNo(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print("The largest number is:", largestNo(num1, num2))


# Q7
# def greet_user(name):
#     return f"Hello, {name}!"
# user_name = input("Enter your name: ")
# print(greet_user(user_name))

# Q8
# def calculate_area(radius):
#     pi = 3.14159
#     return pi * radius * radius
# r = float(input("Enter the radius of the circle: "))
# area = calculate_area(r)
# print(f"The area of the circle with radius {r} is: {area}")

# Q9
# def check_vowel(letter):
#     vowels = 'aeiouAEIOU'
#     if letter in vowels:
#         return True
#     else:
#         return False
# input_letter = input("Enter a letter: ")
# print(check_vowel(input_letter))

# Q10
# def sum_list(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total

# num_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
# print("The sum of the list is:", sum_list(num_list))

# Q11

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# num = int(input("Enter a number to find its factorial: "))
# print(f"The factorial of {num} is: {factorial(num)}")

# Q12
# def reverse_string(s):
#     return s[::-1]
# input_str = input("Enter a string: ")
# print("The reversed string is:", reverse_string(input_str))

# Q13
# def is_palindrome(s):
#     s = s.lower().replace(" ", "")
#     return s == s[::-1]
# input_str = input("Enter a string: ")
# print("Is the string a palindrome?", is_palindrome(input_str))

# Q14
# def count_even(numbers):
#     count = 0
#     for num in numbers:
#         if num % 2 == 0:
#             count += 1
#     return count
# num_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
# print("The count of even numbers in the list is:", count_even(num_list))

# Q15
# def convert_temp(celsius):
#     ferenhite = (celsius * 9/5) + 32
#     print(ferenhite)

# convert_temp(24)