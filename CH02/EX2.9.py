# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "icecream",
# ]
# ///

# (Science: wind-chill temperature) How cold is it outside? The temperature alone is
# not enough to provide the answer. Other factors including wind speed, relative
# humidity, and sunshine play important roles in determining coldness outside. In
# 2001, the National Weather Service (NWS) implemented the new wind-chill temperature
# to measure the coldness using temperature and wind speed. The formula
# is given as follows:
# where is the outside temperature measured in degrees Fahrenheit and v is the
# speed measured in miles per hour. is the wind-chill temperature. The formula
# cannot be used for wind speeds below 2 mph or for temperatures below or
# above 41°F.
# Write a program that prompts the user to enter a temperature between and
# 41°F and a wind speed greater than or equal to 2 and displays the wind-chill temperature.

from icecream import ic  # type: ignore

fahrenheit = eval(input("Enter a temperature in Fahrenheit between -58 and 41: "))
speed = eval(input("Enter the wind speed in miles per hour: "))

wind_chill = (
    35.74
    + (0.6215 * fahrenheit)
    - (35.75 * (speed) ** 0.16)
    + (0.4275 * (fahrenheit) * (speed) ** 0.16)
)

ic(f"The wind chill index is {wind_chill:.5f}")