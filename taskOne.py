import math

class Point:
    def _init_(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)*2 + (self.y - other.y)*2)

    def _str_(self):
        return f"Point({self.x}, {self.y}, color={self.color})"

class PolarPoint(Point):
    def _init_(self, r, theta, color='black'):
        self.r = r
        self.theta = theta
        x = r * math.cos(math.radians(theta))
        y = r * math.sin(math.radians(theta))
        super()._init_(x, y, color)

    def _str_(self):
        return f"PolarPoint(r={self.r}, theta={self.theta}, x={self.x:.2f}, y={self.y:.2f})"

class Rectangle:
    def _init_(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def area(self):
        return abs((self.p2.x - self.p1.x) * (self.p2.y - self.p1.y))

    def _str_(self):
        return f"Rectangle from {self.p1} to {self.p2} | Area: {self.area():.2f}"

class ShapeManager:
    def _init_(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def display_all(self):
        for shape in self.shapes:
            print(shape)