# Kelly J Brown
# 10/05/24
# P2LAB1 - Circle Calculator
# This program calculates and displays the diameter, circumference, and area of a circle based on user input radius.

import math

# Get the radius from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate diameter, circumference, and area
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Display the results
print(f"\nCircle measurements:")
print(f"Diameter: {diameter:.1f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.3f}")
