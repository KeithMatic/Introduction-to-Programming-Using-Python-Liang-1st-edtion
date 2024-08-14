# (Convert Celsius to Fahrenheit)
 
# Write a program that reads a Celsius degree from the console and converts it to Fahrenheit and displays the result. The formula for the conversion is as follows:

# fahrenheit = (9 / 5) * celsius + 32

celsius = int(input("Enter a degree in Celsius: "))

fahrenheit = (9 / 5) * celsius + 32

print(f"{celsius} Celsius is {fahrenheit} Fahrenheit")