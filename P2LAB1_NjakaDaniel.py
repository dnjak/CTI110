# Daniel Njaka
# 2/18/25
# P2LAB1
# Using f-strings to display circle calculations

# import math library

import math

# get radius from user
radius = float(input("What is the radius of the circle? "))

# calculations
diameter = 2 * radius

circumference = 2 * math.pi * radius

area = math.pi * radius ** 2

# display all calculations to user
print(f"The diameter of the circle is {diameter:.1f}")

print(f"The circumference of the circle is {circumference:.2f}")

print(f"The area of the circle is {area:.3f}")