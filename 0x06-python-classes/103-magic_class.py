#!/usr/bin/python3
# Define a class named MagicCircle

class MagicCircle:
    # The constructor (initializer) method
    def __init__(self, radius=0):
        # Initialize the radius attribute
        self.radius = radius

    # Method to calculate the area of the circle
    def calculate_area(self):
        pi = 3.14159  # A close approximation of pi
        area = pi * (self.radius ** 2)
        return area

    # Method to calculate the circumference of the circle
    def calculate_circumference(self):
        pi = 3.14159  # A close approximation of pi
        circumference = 2 * pi * self.radius
        return circumference

# Create an instance of MagicCircle with a radius of 5
circle = MagicCircle(5)

# Calculate and print the area and circumference
print("Area:", circle.calculate_area())
print("Circumference:", circle.calculate_circumference())

