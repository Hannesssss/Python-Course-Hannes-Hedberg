class Rectangle:
    def __init__(self, center_x, center_y, width, height):
        self.x = center_x
        self.y = center_y
        self.width = width
        self.height = height

    def foo(self):
        pass

    @property
    def area(self):
        return self.width * self.height

    @property
    def circumference(self):
        return (self.width + self.height) * 2

    def __str__(self):
        return f"A {self.width}x{self.height} rectangle"

    def __repr__(self):
        return f"""
        Rectangle
            Center: ({self.x}, {self.y})
            Dimensions: {self.width}x{self.height}
        """

    def __eq__(self, other_rectangle):
        return (
            other_rectangle.x == self.x
            and other_rectangle.y == self.y
            and other_rectangle.width == self.width
            and other_rectangle.height == self.height
        )

    def __lt__(self, other_rectangle):
        return self.area < other_rectangle.area

    def __gt__(self, other_rectangle):
        return self.area > other_rectangle.area

    def __le__(self, other_rectangle):
        return self == other_rectangle or self < other_rectangle

    def __ge__(self, other_rectangle):
        return self == other_rectangle or self > other_rectangle


assert Rectangle(0, 0, 2, 3) == Rectangle(0, 0, 2, 3)

assert Rectangle(10, 20, 1, 2) < Rectangle(40, 100, 3, 2)
assert Rectangle(0, 0, 3, 2) > Rectangle(100, 50, 2, 1)

assert Rectangle(40, 20, 2, 1) <= Rectangle(0, 0, 3, 2)
assert Rectangle(0, 0, 3, 2) >= Rectangle(40, 30, 2, 1)

a_rectangle = Rectangle(0, 0, 5, 8)
print(a_rectangle)
print(repr(a_rectangle))