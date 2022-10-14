from geometry_shapes import Rectangle
from geometry_shapes import Circle
from geometry_shapes import Sphere
from geometry_shapes import Cube

rect = Rectangle(1, 1, 2, 2)

print("x, y", rect.x, rect.y)
assert rect.x == 1
assert rect.y == 1

print("area", rect.area)
assert rect.area == 4

print("circumference", rect.circumference)
assert rect.circumference == 8

print("is_square", rect.is_square())
assert rect.is_square() == True

print("is_inside(1, 1)", rect.is_inside(1, 1))
assert rect.is_inside(1, 1) == True

print("is_inside(0.5, 0.5)", rect.is_inside(0.5, 0.5))
assert rect.is_inside(0.5, 0.5) == True

print("is_inside(1, 3)", rect.is_inside(1, 3))
assert rect.is_inside(1, 3) == False

print("is_inside(-0.5, -0.5)", rect.is_inside(-0.5, -0.5))
assert rect.is_inside(-0.5, -0.5) == False

rect1 = Rectangle(1, 1, 1, 1)
rect2 = Rectangle(0, 0, 2, 2)

print(f"rect1 = {repr(rect1)}")
print(f"rect2 = {repr(rect2)}")

print(rect1 == rect2)  # self == other
print(rect1 > rect2)   # self > other
print(rect1 >= rect2)  # self >= other
print(rect1 < rect2)   # self < other
print(rect1 <= rect2)  # self <= other

circle1 = Circle(1, 1, 1)
circle2 = Circle(2, 2, 2)

print(f"circle1 = {repr(circle1)}")
print(f"circle2 = {repr(circle2)}")

print(circle1 == circle2)  # self == other
print(circle1 > circle2)   # self > other
print(circle1 >= circle2)  # self >= other
print(circle1 < circle2)   # self < other
print(circle1 <= circle2)  # self <= other

sphere1 = Sphere(1, 1, 1)
sphere2 = Sphere(2, 2, 2)

print(f"sphere1 = {repr(sphere1)}")
print(f"sphere2 = {repr(sphere2)}")

print(sphere1 == sphere2)  # self == other
print(sphere1 > sphere2)   # self > other
print(sphere1 >= sphere2)  # self >= other
print(sphere1 < sphere2)   # self < other
print(sphere1 <= sphere2)  # self <= other
