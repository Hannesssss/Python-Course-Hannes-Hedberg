from geometry_shapes import Rectancle

rect = Rectancle(1, 1, 2, 2)

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
assert rect.is_inside(1, 3) == True

rect1 = Rectancle(1, 1, 1, 1)
rect2 = Rectancle(0, 0, 2, 2)

print(f"rect1 = {repr(rect1)}")
print(f"rect2 = {repr(rect2)}")

print(rect1 == rect2)  # self == other
print(rect1 > rect2)   # self > other
print(rect1 >= rect2)  # self >= other
print(rect1 < rect2)   # self < other
print(rect1 <= rect2)  # self <= other
