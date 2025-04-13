import math

class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __str__(self):
        return f"Point({self.x}, {self.y}, color={self.color})"

class PolarPoint(Point):
    def __init__(self, r, theta, color='black'):
        self.r = r
        self.theta = theta
        x = r * math.cos(math.radians(theta))
        y = r * math.sin(math.radians(theta))
        super().__init__(x, y, color)

    def __str__(self):
        return f"PolarPoint(r={self.r}, theta={self.theta}, x={self.x:.2f}, y={self.y:.2f})"

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def area(self):
        return abs((self.p2.x - self.p1.x) * (self.p2.y - self.p1.y))

    def __str__(self):
        return f"Rectangle from {self.p1} to {self.p2} | Area: {self.area():.2f}"

class ShapeManager:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def display_all(self):
        for shape in self.shapes:
            print(shape)

# Example usage
if __name__ == "__main__":
    p1 = Point(0, 0, 'red')
    p2 = Point(3, 4, 'blue')
    print(f"Distance: {p1.distance_to(p2):.2f}")

    pp = PolarPoint(5, 45)
    print(pp)

    rect = Rectangle(p1, p2)
    print(rect)

    sm = ShapeManager()
    sm.add_shape(p1)
    sm.add_shape(p2)
    sm.add_shape(pp)
    sm.add_shape(rect)
    sm.display_all()
