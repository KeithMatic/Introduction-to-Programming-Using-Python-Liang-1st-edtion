# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "icecream",
# ]
# ///

# (Sum the digits in an integer) Write a program that reads an integer between 0 and
# 1000 and adds all the digits in the integer. For example, if an integer is 932, the
# sum of all its digits is 14. (Hint: Use the % operator to extract digits, and use the //
# operator to remove the extracted digit. For instance, 932 % 10 = 2 and 932 //
# 10 = 93.)

from icecream import ic  # type: ignore

user_input_number = int(input("Enter a nubmer between 0 and 1000: "))

last_number = user_input_number % 10

second_last_number = (user_input_number // 10) % 10

third_last_number = (user_input_number // 10) // 10

sum = last_number + second_last_number + third_last_number

ic(f"The sum of the digits is {sum}")
