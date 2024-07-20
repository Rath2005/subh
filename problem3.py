#Program to create a circle with certain details

import math

class Circle:

    def _init_(self, x, y, radius):

        self.x = x

        self.y = y

        self.radius = radius

    def get_area(self):

        return math.pi * self.radius ** 2

    def get_perimeter(self):

        return 2 * math.pi * self.radius

    def get_circumference(self):

        return self.get_perimeter()

# Example usage:

circle = Circle(0, 0, 5)

print(f"Area: {circle.get_area()}")

print(f"Perimeter: {circle.get_perimeter()}")

print(f"Circumference: {circle.get_circumference()}")