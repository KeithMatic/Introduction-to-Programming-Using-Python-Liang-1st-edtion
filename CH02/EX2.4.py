# (Convert pounds into kilograms) Write a program that converts pounds into
# kilograms. The program prompts the user to enter a value in pounds, converts it to
# kilograms, and displays the result. One pound is 0.454 kilograms. Here is a
# sample run:


# Prompt the user to enter a value in pounds
pounds = float(input("Enter a value in pounds: "))

# One pound is 0.454 kilograms
kilograms = 0.454

# Convert the pounds to kilograms
kilograms *= pounds

# Display results
print(f"{pounds} is {kilograms} kilograms")