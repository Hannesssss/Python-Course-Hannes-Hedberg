import math # imports math module

class GeometryShape:                                                            # Parent class, other classes will inhereit from this
    def __init__(self, x: int, y: int) -> int:
        """
        initalize x and y
        """
        self.translate(x, y)

    def translate(self, x: int, y: int) -> int:
        """
        Raises an Error if value isnt an int
        """
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):  # check if both arguments are numbers
            raise ValueError("translate expects a valid number input")          # throws error about invalid input
        self.x = x
        self.y = y

    # operator overload ==
    def __eq__(self, other: int) -> int:   
        """
        Checks if area is = other
        """ 
        if not isinstance(other, self.__class__):
            return False
        return self.area == other.area

    # operator overload >
    def __gt__(self, other: int) -> int:
        """
        self area larger than other area
        """ 
        if not isinstance(other, self.__class__):
            return False
        return self.area > other.area

    # operator overload >=
    def __ge__(self, other: int) -> int:
        """
        self area larger than other area, or same area
        """ 
        return self > other or self == other

    # operator overload <
    def __lt__(self, other: int) -> int:
        """
        Checks if area is = other and if its equal to area
        """ 
        return self < other and self == other

    # operator overload <=
    def __le__(self, other: int) -> int:
        """
        Checks if self is smaller than other or equal to other
        """ 
        return self < other or self == other

class GeomtryShape3D(GeometryShape):        # 3d geometry requires another dimension, inherits from the other Parent class
    def __init__(self, x: int, y: int, z: int) -> int:
        """
        Creates 3D class, used for cube and sphere, inherits from 2d but adding z as the 3rd dimension
        """ 
        self.translate(x, y, z)

    def translate(self, x: int, y: int, z: int) -> int:
        """
        Checks if xyz are int, returns error if not
        """
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)) or not isinstance(z, (int, float)):  # check if both arguments are numbers
            raise ValueError("translate expects a valid number input")          # throws error about invalid input
        self.x = x
        self.y = y
        self.z = z

class Rectangle(GeometryShape):
    """
    Creates Rectnagle class
    """
    def __init__(self, x: int, y: int, side1: int, side2: int) -> int:
        super().__init__(x, y)                       # Calls the parents __init__. In this case that is GeometryShape
        if not isinstance(side1, (int, float)) or not isinstance(side2, (int, float)):
            raise ValueError("Rectangle expects valid number input")
        self._height = side1
        self._width = side2

    @property
    def area(self):
        """
        Property of area is selfs height multiplied by its width
        """
        return self._height * self._width   # height * width = area

    @property
    def circumference(self):
        """
        Property of circumference is selfs height multiplied by its width, squared
        """
        return (self._height + self._width) * 2 # (height + width) * 2 = circumference

    def is_square(self):
        """
        Checks if self height is equal to width, if true then its a square
        """
        return self._height == self._width  # both sides same lenghts -> square

    def is_inside(self, x: float, y: float) -> bool:
        """
        checks if its within the square, returns value error if presented with invalid input
        """
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
    def __init__(self, x: int, y: int, radius: int) -> int:
        """
        Cirlce calls the parent class GeometryShape, then checks for valid value input
        """
        super().__init__(x, y)                       # Calls the parents __init__. In this case that is GeometryShape
        if not isinstance(radius, (int, float)):
            raise ValueError("Circle expects valid number input")
        self._radius = radius

    @property
    def area(self):
        """
        Calculates circle selfs area, by doing its radius squared, multiplied with pi
        """
        return (self._radius ** 2) * math.pi 

    @property
    def circumference(self):
        """
        Calculates circle selfs circumference, by doing its radius, multiplied with two, then multiplied with pi
        """
        return self._radius * 2 * math.pi

    def is_unit_circle(self):
        """
        The circle has to have a value to be a circle
        """
        return self._radius == 1

    def is_inside(self, x: float, y: float) -> bool:
        """
        Determinds if self is within the circle or not
        """
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
    """
    Creating Sphere class, which inherts from GemotryShape3D, which inherited from GemotryShapes earlier.
     Checks for valid number input otherwise rasies error
    """
    def __init__(self, x: int, y: int, z: int, radius: int) -> int:               
        super().__init__(x, y, z)                       # Calls the parents __init__. In this case that is GeomtryShape3D
        if not isinstance(radius, (int, float)):
            raise ValueError("Sphere expects valid number input")
        self._radius = radius

    @property
    def area(self):
        """
        calculate the area of the Sphere, radius squared with 2, multiplied with pi, mulitplied with 4.
        """
        return (self._radius ** 2) * math.pi * 4

    @property
    def circumference(self):
        """
        Calculate the circumference of the circle, radius multiplied with 2, multiplied with pi
        """
        return self._radius * 2 * math.pi

    def is_unit_sphere(self):
        """
        Checks if the sphere has a valid value, needs a value to exist
        """
        return self._radius == 1

    def is_inside(self, x: float, y: float, z: float) -> bool:
        """
        Checks if self is inside the sphere or not
        """
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
    """
    Creating the Cube Class which inherits from GemotryShape3D
    """
    def __init__(self, x: int, y: int, z: int, size: int) -> int:
        super().__init__(x, y, z)                       # Calls the parents __init__. In this case that is GeomtryShape3D
        if not isinstance(size, (int, float)):
            raise ValueError("Cube expects valid number input")
        self._size = size

    @property
    def area(self):
        """
        Calculate area of the Cube, self multiplied with 2, multiplied with 6 for each side
        """
        return (self._size * 2) * 6

    @property
    def circumference(self):
        """
        Calculate circumference, multiplies self with 6, for each side.
        """
        return self._size * 6

    def is_inside(self, x: float, y: float, z:float) -> bool:   # type hint
        """
        Checks if self is inside cube
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
