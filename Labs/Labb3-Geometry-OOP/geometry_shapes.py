import math # imports math module

class GeometryShape:                                                            # Parent class, other classes will inhereit from this
    def __init__(self, x, y):
        self.translate(x, y)

    def translate(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):  # check if both arguments are numbers
            raise ValueError("translate expects a valid number input")          # throws error about invalid input
        self.x = x
        self.y = y

    # operator overload ==
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.area == other.area

    # operator overload >
    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.area > other.area

    # operator overload >=
    def __ge__(self, other):
        return self > other or self == other

    # operator overload <
    def __lt__(self, other):
        return self < other and self == other

    # operator overload <=
    def __le__(self, other):
        return self < other or self == other

class GeomtryShape3D(GeometryShape):        # 3d geometry requires another dimension, inherits from the other Parent class
    def __init__(self, x, y, z):
        self.translate(x, y, z)

    def translate(self, x, y, z):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)) or not isinstance(z, (int, float)):  # check if both arguments are numbers
            raise ValueError("translate expects a valid number input")          # throws error about invalid input
        self.x = x
        self.y = y
        self.z = z

class Rectangle(GeometryShape):
    def __init__(self, x, y, side1, side2):
        super().__init__(x, y)                       # Calls the parents __init__. In this case that is GeometryShape
        if not isinstance(side1, (int, float)) or not isinstance(side2, (int, float)):
            raise ValueError("Rectangle expects valid number input")
        self._height = side1
        self._width = side2

    @property
    def area(self):
        return self._height * self._width   # height * width = area

    @property
    def circumference(self):
        return (self._height + self._width) * 2 # (height + width) * 2 = circumference

    def is_square(self):
        return self._height == self._width  # both sides same lenghts -> square

    def is_inside(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("is_inside expects valid number input")
        dif_x = self.x - x                  # subtracts our postions from the input in order to get the relative position
        dif_y = self.y - y
        return self._height >= abs(dif_y) and self._width >= abs(dif_x) # checks if distance to middle is bigger than width and height
        
    def __repr__(self): # Debug information
        return f"Rectangle({self.x}, {self.y}, {self._height}, {self._width})"

    def __str__(self):  # Pretty information
        return f"x = {self.x}, y = {self.y}, height = {self._height}, width = {self._width}"

class Circle(GeometryShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)                       # Calls the parents __init__. In this case that is GeometryShape
        if not isinstance(radius, (int, float)):
            raise ValueError("Circle expects valid number input")
        self._radius = radius

    @property
    def area(self):
        return (self._radius ** 2) * math.pi 

    @property
    def circumference(self):
        return self._radius * 2 * math.pi

    def is_unit_circle(self):
        return self._radius == 1

    def is_inside(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("is_inside expects valid number input")
        dif_x = self.x - x                  # subtracts our postions from the input in order to get the relative position
        dif_y = self.y - y
        return self._radius >= abs(dif_x + dif_y)       # absoulte value, calculating distance which cant be negative
        # x = 1 , y = 1 , x + y <= radius

    def __repr__(self): # Debug information
        return f"Circle({self.x}, {self.y}, {self._radius})"

    def __str__(self):  # Pretty information
        return f"x = {self.x}, y = {self.y}, radius = {self._radius}"

class Sphere(GeomtryShape3D):
    def __init__(self, x, y, z, radius):                # Cube, 
        super().__init__(x, y, z)                       # Calls the parents __init__. In this case that is GeomtryShape3D
        if not isinstance(radius, (int, float)):
            raise ValueError("Sphere expects valid number input")
        self._radius = radius

    @property
    def area(self):
        return (self._radius ** 2) * math.pi * 4

    @property
    def circumference(self):
        return self._radius * 2 * math.pi

    def is_unit_sphere(self):
        return self._radius == 1

    def is_inside(self, x, y, z):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)) or not isinstance(z, (int, float)):
            raise ValueError("is_inside expects valid number input")
        dif_x = self.x - x                  # subtracts our postions from the input in order to get the relative position
        dif_y = self.y - y
        dif_z = self.z - z
        return self._radius >= abs(dif_x + dif_y + dif_z)       # absoulte value, calculating distance which cant be negative

    def __repr__(self): # Debug information
        return f"Sphere({self.x}, {self.y}, {self.z}, {self._radius})"

    def __str__(self):  # Pretty information
        return f"x = {self.x}, y = {self.y}, z = {self.z}, radius = {self._radius}"

class Cube(GeomtryShape3D):
    def __init__(self, x, y, z, size):
        super().__init__(x, y, z)                       # Calls the parents __init__. In this case that is GeomtryShape3D
        if not isinstance(size, (int, float)):
            raise ValueError("Cube expects valid number input")
        self._size = size

    @property
    def area(self):
        return (self._size * 2) * 6

    @property
    def circumference(self):
        return self._size * 6

    def is_inside(self, x: float, y: float, z:float) -> bool:   # type hint
        """
                # docstring --------------
        """
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)) or not isinstance(z, (int, float)):
            raise ValueError("is_inside expects valid number input")
        dif_x = self.x - x                  # subtracts our postions from the input in order to get the relative position
        dif_y = self.y - y
        dif_z = self.z - z
        return self._size >= abs(dif_x) and self._size >= abs(dif_y) and self._size >= abs(dif_z)
        
    def __repr__(self): # Debug information
        return f"Cube({self.x}, {self.y}, {self.z}, {self._size})"

    def __str__(self):  # Pretty information
        return f"x = {self.x}, y = {self.y}, z = {self.z}, size = {self._size}"




# Komplettering

# * UMLen är felaktig och behöver skrivas om. Ex på UML du kan kika på https://github.com/kokchun/Python-course-AI22/blob/main/Lecture_notes/Lec13.1-UML_exempel.png
# * lägg till docstrings
# X * notera att not self > other är samma som self < other
# * lägg till type hints
# * hade velat se fler manuella tester 