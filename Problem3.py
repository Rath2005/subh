#Program to take an input for the 3 sides of a triangle from the user and check

import math

def is_valid_triangle(a, b, c):

    return a + b > c and a + c > b and b + c > a

def classify_triangle(a, b, c):

    if a == b == c:

        return "Equilateral"
    
    elif a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:

        return "Right-angled"
    
    elif a == b or b == c or a == c:

        return "Isosceles"
    
    else:

        return "Scalene"

def circumcenter_radius(a, b, c):

    if not is_valid_triangle(a, b, c):

        return -1
    
    triangle_type = classify_triangle(a, b, c)

    if triangle_type == "Right-angled":

        # For a right-angled triangle, the radius of the circumcenter is half the hypotenuse.

        hypotenuse = max(a, b, c)

        return hypotenuse / 2
    
    return -1

def main():

    a = float(input("Enter the first side of the triangle: "))

    b = float(input("Enter the second side of the triangle: "))

    c = float(input("Enter the third side of the triangle: "))

    if not is_valid_triangle(a, b, c):

        print("The given sides do not form a valid triangle.")

        return

    triangle_type = classify_triangle(a, b, c)

    print(f"The triangle is {triangle_type}.")

    radius = circumcenter_radius(a, b, c)

    if radius != -1:

        print(f"The radius of the circumcenter is: {radius}")

    else:

        print(radius)

if __name__ == "_main_":
    
    main()
