import math # imports math module

class GeometryShape:
    def __init__(self, x, y):
        self.translate(x, y)

    def translate(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):  # check if both arguments are numbers
            raise ValueError("translate expects a valid number input")          # throws error about invalid input
        self.x = x
        self.y = y

    # operator overload >=
    def __ge__(self, other):  # greater than or equal
        return self > other or self == other

    # operator overload <
    def __lt__(self, other):  # lesser than
        return not self > other and not self == other

    # operator overload <=
    def __le__(self, other):  # lesser than or equal
        return self < other or self == other

class Rectancle(GeometryShape):
    def __init__(self, x, y, height, width):
        super().__init__(x, y)                       # Calls the parents __init__. In this case that is GeometryShape
        if not isinstance(height, (int, float)) or not isinstance(width, (int, float)):
            raise ValueError("Rectangle expects valid number input")
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._height * self._width

    @property
    def circumference(self):
        return (self._height + self._width) * 2

    def is_square(self):
        return self._height == self._width

    def is_inside(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("is_inside expects valid number input")
        return self._height >= y and self._width >= x
        
    def __repr__(self): # Debug information
        return f"Rectancle({self.x}, {self.y}, {self._height}, {self._width})"

    def __str__(self):  # Pretty information
        return f"x = {self.x}, y = {self.y}, height = {self._height}, width = {self._width}"

    # operator overload ==
    def __eq__(self, other):
        if not isinstance(other, Rectancle):            # checks if other is also a rectangle
            return False
        return (                                        # compares stored variables of both rectangles
            self._width == other._width and
            self._height == other._height
        )

    # operator overload >
    def __gt__(self, other):                            # greater than
        if not isinstance(other, Rectancle):            # checks if other is also a rectangle
            return False
        return self.area > other.area