# (Convert feet into meters) Write a program that reads a number in feet, converts it
# to meters, and displays the result. One foot is 0.305 meters.

# Prompt the user to enter value for feet
feet = float(input("Enter a value for feet: "))

# One foot is 0.305 meters
meters = 0.305

# Calculate meters
meters *= feet

# Display the results
print(f"{feet} feet is {meters} meters")
feet = eval(input("Enter a value for feet:"))
metre = feet * 0.305
print(feet, "feet is", metre, "metres")
