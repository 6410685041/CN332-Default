from abc import ABC, abstractmethod
import turtle as t
from .extension import parse_points, calculate_angle

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
        t.color(self.color)
        t.begin_fill()
        t.penup()
        t.goto(self.coordinates[0][0], self.coordinates[0][1])
        t.pendown()

        for (x, y) in self.coordinates:
           t.goto(x, y)

        t.end_fill()

class Triangle(Shape):
    BOUND = 100

    def __init__(self, coordinate, color):
        coordinates = parse_points(coordinate)
        coordinates = [(num1 * self.BOUND, num2 * self.BOUND) for (num1, num2) in coordinates]
        coordinates.append(coordinates[0])

        angle = []
        angle.append(calculate_angle(coordinates[0],coordinates[1],coordinates[2]))
        angle.append(calculate_angle(coordinates[1],coordinates[2],coordinates[0]))
        angle.append(calculate_angle(coordinates[2],coordinates[0],coordinates[1]))

        self.coordinates = coordinates
        self.angle = angle
        self.color = color

    def drawline(self, distance):
        t.fd(distance)

    def draw(self):
        t.color(self.color)
        t.begin_fill() 

        t.penup()
        t.goto(self.coordinates[0][0], self.coordinates[0][1])
        t.pendown()
 
        for (x, y) in self.coordinates:
           t.goto(x, y)

        t.end_fill()

class Circle(Shape):
    BOUND=100

    def __init__(self,radius,coordinate,color):
        coordinates = parse_points(coordinate)
        coordinates = [(num1 * self.BOUND, num2 * self.BOUND) for (num1, num2) in coordinates]

        self.radius = float(radius)*self.BOUND
        self.coordinates = coordinates
        self.color = color

    def drawline(self, distance):
        t.fd(distance)

    def draw(self):
        t.color(self.color)
        t.begin_fill() 

        t.penup()
        t.goto(self.coordinates[0][0], self.coordinates[0][1]-self.radius)
        t.pendown()
 
        t.circle(self.radius)

        t.end_fill()
        t.done()
