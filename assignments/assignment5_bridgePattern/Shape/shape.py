from abc import ABC, abstractmethod
import turtle as t
from .extension import parse_points

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def drawline(self, distance):
        pass

class Rectangle(Shape):
    BOUND = 100

    def __init__(self, coordinate, color):
        coordinates = parse_points(coordinate)
        coordinates.sort()
        coordinates = [(num1 * self.BOUND, num2 * self.BOUND) for (num1, num2) in coordinates]
        coordinate_1 = (coordinates[1][0],coordinates[0][1])
        coordinate_2 = (coordinates[0][0],coordinates[1][1])
        coordinates.insert(1, coordinate_1)
        coordinates.append(coordinate_2)
        coordinates.append(coordinates[0])
        self.coordinates = coordinates

        self.color = color

    def drawline(self, distance):
        t.fd(distance)

    def draw(self):
        # t.color(self.color)
        t.begin_fill() 

        for (x, y) in self.coordinates:
           t.goto(x, y)

        t.end_fill() 