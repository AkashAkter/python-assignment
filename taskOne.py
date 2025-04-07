import math

class Color:
    """Class to represent color with RGB components"""
    def __init__(self, r=0, g=0, b=0):
        self.r = r  # Red component (0-255)
        self.g = g  # Green component (0-255)
        self.b = b  # Blue component (0-255)

class Point:
    """Class to represent a point in 2D space with x,y coordinates"""
    def __init__(self, x=0, y=0):
        self.__x = x  # Private x coordinate
        self.__y = y  # Private y coordinate
        self.color = Color()  # Color attribute initialized with default color
    
    # Getter methods
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    # Setter methods
    def set_x(self, x):
        self.__x = x
    
    def set_y(self, y):
        self.__y = y
    
    def get_distance(self, other_point):
        """Calculate Euclidean distance between two points"""
        dx = self.__x - other_point.get_x()
        dy = self.__y - other_point.get_y()
        return math.sqrt(dx**2 + dy**2)
    
    def __str__(self):
        return f"Point(x={self.__x}, y={self.__y}, color=({self.color.r},{self.color.g},{self.color.b}))"

class Rectangle:
    """Class to represent a rectangle using two points"""
    def __init__(self, top_left, bottom_right):
        if not (isinstance(top_left, Point) and isinstance(bottom_right, Point)):
            raise ValueError("Both arguments must be Point objects")
        self.top_left = top_left
        self.bottom_right = bottom_right
    
    def calculate_area(self):
        """Calculate area of the rectangle"""
        width = abs(self.bottom_right.get_x() - self.top_left.get_x())
        height = abs(self.top_left.get_y() - self.bottom_right.get_y())
        return width * height
    
    def __str__(self):
        return f"Rectangle(TopLeft: {self.top_left}, BottomRight: {self.bottom_right})"

class PolarPoint(Point):
    """Class to represent a point in polar coordinates (r,θ)"""
    def __init__(self, r=0, a=0):
        # Convert polar to Cartesian coordinates
        x = r * math.cos(a)
        y = r * math.sin(a)
        super().__init__(x, y)  # Initialize parent Point class
        self.__r = r  # Radius
        self.__a = a  # Angle in radians
    
    # Getters and setters for polar coordinates
    def get_r(self):
        return self.__r
    
    def get_a(self):
        return self.__a
    
    def set_r(self, r):
        self.__r = r
        # Update Cartesian coordinates when polar coordinates change
        self.set_x(r * math.cos(self.__a))
        self.set_y(r * math.sin(self.__a))
    
    def set_a(self, a):
        self.__a = a
        # Update Cartesian coordinates when polar coordinates change
        self.set_x(self.__r * math.cos(a))
        self.set_y(self.__r * math.sin(a))
    
    def __str__(self):
        return f"PolarPoint(r={self.__r}, a={self.__a}, x={self.get_x()}, y={self.get_y()})"