# (Financial application: calculate tips) Write a program that reads the subtotal and
# the gratuity rate and computes the gratuity and total. For example, if the user
# enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5
# as the gratuity and 11.5 as the total.

# Read subtotal
subtotal, gratuity = eval(input("Enter the subtotal and a gratuity rate: "))

# Compute the gratuity
gratuity = subtotal * (gratuity / 100)

# Compute subtotal
subtotal += gratuity

# Display results
print(f"The gratuity is {gratuity:.2f} and the total is {subtotal:.2f}")