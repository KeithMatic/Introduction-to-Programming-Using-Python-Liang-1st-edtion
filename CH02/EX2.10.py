# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "icecream",
# ]
# ///


# (Physics: find runway length) Given an airplane’s acceleration a and take-off
# speed v, you can compute the minimum runway length needed for an airplane to
# take off using the following formula:
# Write a program that prompts the user to enter v in meters/second (m/s) and the
# acceleration a in meters/second squared and displays the minimum runway
# length.

from icecream import ic  # type: ignore

speed_meters_seconds, accelaration_meters_seconds = eval(
    input("Enter speed acceleration: ")
)

runway_length = (speed_meters_seconds) ** 2 / (2 * accelaration_meters_seconds)

ic(f"The minimum runway length for this airplane is {runway_length:.3f} meters")
