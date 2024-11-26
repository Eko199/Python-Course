from math import pi

class Rectangle:
    def __init__(self, length, width, color):
        self._length = length
        self._width = width
        self._color = color

    @property
    def length(self):
        return self._length
    
    @property
    def width(self):
        return self._width
    
    @property
    def color(self):
        return self._color
    
    @property
    def area(self):
        return self.length * self.width
    
class Circle:
    def __init__(self, radius, color):
        self._radius = radius
        self._color = color

    @property
    def radius(self):
        return self._radius
    
    @property
    def color(self):
        return self._color
    
    @property
    def area(self):
        return pi * self.radius ** 2
    
class Shapes:
    def __init__(self):
        self._shapes = []
        self._rectangles = []
        self._circles = []

    def addRectangle(self, rect):
        self._shapes.push(rect)
        self._rectangles.push(rect)

    def addCircle(self, circle):
        self._shapes.push(circle)
        self._circles.push(circle)

    @property
    def rectsAreaSum(self):
        result = 0

        for rect in self._rectangles:
            result += rect.area

        return result

    @property
    def circlesAreaSum(self):
        result = 0

        for circle in self._circles:
            result += circle.area

        return result

    def __getitem__(self, index):
        return self._shapes[index]