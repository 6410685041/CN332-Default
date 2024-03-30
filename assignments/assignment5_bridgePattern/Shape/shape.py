from abc import ABC, abstractmethod
import turtle as t

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def drawline(self, distance):
        pass

class Rectangle(Shape):
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def drawline(self, distance):
        t.fd(distance)

    def draw(self):
        t.penup()
        t.goto(self.coordinates[0][0], self.coordinates[0][1])
        t.pendown()

        for (x, y) in self.coordinates:
           t.goto(x, y)

class Triangle(Shape):
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def drawline(self, distance):
        t.fd(distance)

    def draw(self):
        t.penup()
        t.goto(self.coordinates[0][0], self.coordinates[0][1])
        t.pendown()
 
        for (x, y) in self.coordinates:
           t.goto(x, y)

class Circle(Shape):
    def __init__(self,radius,coordinates):
        self.radius = radius
        self.coordinates = coordinates

    def drawline(self, distance):
        t.fd(distance)

    def draw(self):
        t.penup()
        t.goto(self.coordinates[0][0], self.coordinates[0][1]-self.radius)
        t.pendown()
 
        t.circle(self.radius)
