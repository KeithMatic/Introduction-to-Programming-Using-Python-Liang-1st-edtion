# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "icecream",
#     "ruff",
# ]
# ///

# (Convert pounds into kilograms) Write a program that converts pounds into
# kilograms. The program prompts the user to enter a value in pounds, converts it to
# kilograms, and displays the result. One pound is 0.454 kilograms. Here is a
# sample run:

from icecream import ic

KILOGRAM = 0.454

pounds = float(input("Enter a value in pounds: "))

kilograms = pounds * KILOGRAM

ic(f"{pounds} pounds is {kilograms} kilograms")
