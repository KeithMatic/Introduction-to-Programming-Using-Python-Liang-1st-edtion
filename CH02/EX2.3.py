# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "icecream",
# ]
# ///


# (Convert feet into meters) Write a program that reads a number in feet, converts it
# to meters, and displays the result. One foot is 0.305 meters.

from icecream import ic  # type: ignore

FOOT = 0.305

feet = float(input("Enter a value for feet: "))

meters = feet * FOOT

ic(f"{feet} feet is {meters} meters")
