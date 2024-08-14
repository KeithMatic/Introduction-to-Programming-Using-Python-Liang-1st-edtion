# (Compute the volume of a cylinder) Write a program that reads in the radius and
# length of a cylinder and computes the area and volume using the following formulas:
# area = radius * radius * π
# volume = area * length


PI = 3.14159

radius, length = eval(input("Enter the radius and length of a cylinder: "))

# area = radius * radius * pi
area = float(radius * radius) * PI

# volume = area * length
volume = area * length

# print area and length
print(f"The area is {round(area)}")
print(f"The volume  is {round(volume)}")