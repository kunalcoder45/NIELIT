# # condition statements in Python

# # age = int(input("Enter your age: "))
# # if age < 18:
# #     print("Sorry, you are not eligible to vote.")
# # else:
# #     print("Yes you can vote!")

# # number = int(input("Enter a number: "))
# # if number % 2 == 0:
# #     print(f"{number} is an even number.")
# # else:
# #     print(f"{number} is an odd number.")


# # questions

# # Q1
# num = int(input("Enter a number: "))
# if num > 0:
#     print(f"{num} is a positive number.")
# elif num < 0:
#     print(f"{num} is a negative number.")
# else:
#     print("The number is zero.")

# # Q2
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print(f"{number} is an even number.")
# else:
#     print(f"{number} is an odd number.")

# # Q3

# age = int(input("Enter your age: "))
# if age < 18:
#     print("Sorry, you are not eligible to vote.")
# else:
#     print("Yes you can vote!")

# # Q4
# number = int(input("Enter a number: "))
# if number % 5 == 0:
#     print(f"{number} is divisible by 5.")
# else:
#     print(f"{number} is not divisible by 5.")

# # Q5

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1 > num2:
#     print(f"{num1} is greater than {num2}.")
# elif num2 > num1:
#     print(f"{num2} is greater than {num1}.")
# else:
#     print("Both numbers are equal.")

# # Q6
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# if num1 >= num2 and num1 >= num3:
#     print(f"{num1} is the largest number.")
# elif num2 >= num1 and num2 >= num3:
#     print(f"{num2} is the largest number.")
# else:
#     print(f"{num3} is the largest number.")

# Q7
# vowels = ['a', 'e', 'i', 'o', 'u']
# char = input("Enter a character: ").lower()
# if char in vowels:
#     print(f"{char} is a vowel.")
# else:
#     print(f"{char} is not a vowel its a consonant.")

# Q8
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

# Q9

# unit = int(input("Enter the number of electricity units consumed: "))
# if unit <= 100:
#     bill = unit * 5
# elif unit > 100 and unit < 200:
#     bill = unit * 7
# elif unit >= 200:
#     bill = unit * 10
# print(f"Your electricity bill is: {bill} units.")

# Q10 prime number check
# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print(f"{num} is not a prime number.")
#             break
#     else:
#         print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")