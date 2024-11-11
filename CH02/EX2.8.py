# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "icecream",
# ]
# ///


# (Science: calculate energy) Write a program that calculates the energy needed to
# heat water from an initial temperature to a final temperature. Your program should
# prompt the user to enter the amount of water in kilograms and the initial and final
# temperatures of the water. The formula to compute the energy is
# Q = M * (finalTemperature – initialTemperature) * 4184
# where M is the weight of water in kilograms, temperatures are in degrees Celsius,
# and energy Q is measured in joules.

from icecream import ic  # type: ignore

water_in_kilograms = float(input("Enter the amount of water in kilograms: "))
initial_temperature = float(input("Enter initial temperatures: "))
final_temperature = float(input("Enter final temperatures: "))

energy = water_in_kilograms * (final_temperature - initial_temperature) * 4184

ic(f"The energy needed is {energy}")
