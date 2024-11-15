# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "icecream",
# ]
# ///

# (Find the number of years and days) Write a program that prompts the user to
# enter the minutes (e.g., 1 billion), and displays the number of years and days for
# the minutes.

from icecream import ic  # type: ignore

minutes = int(input("Enter the number of minutes: "))

hours = minutes // 60

total_days = hours // 24

years = total_days // 365

days = total_days % 365

ic(f"{minutes} minutes is approximately {years} years and {days} days")
