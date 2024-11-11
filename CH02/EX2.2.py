# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "icecream",
# ]
# ///
# (Compute the volume of a cylinder) Write a program that reads in the radius and
# length of a cylinder and computes the area and volume using the following formulas:
# area = radius * radius * π
# volume = area * length

import math

from icecream import ic  # type: ignore

radius, length = eval(input("Enter the radius and length of a cylinder: "))

area = radius * radius * math.pi
volume = area * length

ic(f"The area is {area}")
ic(f"The volume is {volume}")
