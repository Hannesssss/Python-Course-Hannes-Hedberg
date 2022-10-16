# Labb 3 OOP Gemoetry

import math # imports math module
import matplotlib as plt
import numpy as np

class Rectangle:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def __repr__(self):
        rv = "\nRectangle with side lenghts " + str(self.s1) + ", " + str(self.s2)
        rv += "\nArea: " + str(self.calc_area())
        rv += "\nCircumference: " + str(self.calc_circumference())
        rv += "\nCenter of mass: x = " + str(self.calc_center_x()) + ", y = " + str(self.calc_center_y())
        return rv
    
    def calc_area(self):
        return self.s1 * self.s2
    
    def calc_circumference(self):
        return self.s1 + self.s1 + self.s2 + self.s2

    def calc_center_x(self):
        return (self.s1 + self.s1) / 2
    
    def calc_center_y(self):
        return (self.s2 + self.s2) / 2

    def user_input_x(self):
        return (input())

    def user_input_y(self):
        return(input())

    def determine_within_object(self):
        pass

    def __eq__(self, rectangle_object):
        pass

    # s1 < s2 or s1 > s2

# s1 = Rectangle(1)
# s2 = Rectangle(2)
# s3 = s1 == s2 
# print(s3)
    

class Circle:
    def __init__(self, r):
        self.radius = r
    
    def __repr__(self):
        rv = "\nCircle with radius " + str(self.radius)
        rv += "\nArea: " + str(self.calc_area())
        rv += "\nCircumference: " + str(self.calc_circumference())
        rv += "\nCenter: x = " + str(self.calc_center_x()) + ", y = " + str(self.calc_center_y())
        return rv
    
    def calc_area(self):
        return math.pi * (self.radius ** 2)

    def calc_circumference(self):
        return 2 * math.pi * (self.radius)

    def calc_center_x(self):
        return (self.radius)

    def calc_center_y(self):
        return (self.radius)

class Cube:
    def __init__(self, s1, s2, s3): # s1 = width, s2 = height, s3 = depth
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def __repr__(self):
        rv = "\nCube with side lenghts " + str(self.s1) + ", " + str(self.s2) + ", " + str(self.s2)
        rv += "\nVolume: " + str(self.calc_volume())
        rv += "\nRestriction Area: " + str(self.calc_restrictionArea())
        rv += "\nCircumference: " + str(self.calc_circumference())
        return rv

    def calc_volume(self):
        return self.s1 * self.s2 * self.s3

    def calc_restrictionArea(self):
        return 6 * self.s1 ** 2

    def calc_circumference(self):
        return 4 * self.s1

class Sphere:
    def __init__(self, r):
        self.radius = r

    def __repr__(self):
        rv = "\nSphere with radius " + str(self.radius)
        rv += "\nArea: " + str(self.calc_area())
        return rv

    def calc_area(self):
        return 4 * math.pi * (self.radius**2)

rectangle = Rectangle(5, 10)
print(rectangle)

circle = Circle(5)
print(circle)

cube = Cube(5, 5, 5)
print(cube)

sphere = Sphere(5)
print(sphere)

#circle_check = isinstance(Circle, object)
# print(f"The circle circle_check")

# f(r) = (r + r) / 2 