from abc import ABC, abstractmethod
import turtle as t
import assignments.assignment5_bridgePattern.Drawing as d

class Shape(ABC):
    def __init__(self, drawing):
        self.myDrawing = drawing

    @abstractmethod
    def draw(self):
        pass

class Rectangle(Shape):
    def __init__(self, drawing, coordinates):
        super().__init__(drawing)
        self.coordinates = coordinates

    def draw(self): 
        self.myDrawing.drawLine(self.coordinates)

class Triangle(Shape):
    def __init__(self, drawing, coordinates):
        self.coordinates = coordinates

    def draw(self):
        self.myDrawing.drawLine(self.coordinates)
     
class Circle(Shape):
    def __init__(self,drawing,radius,coordinates):
        super().__init__(drawing)
        self.radius = radius
        self.coordinates = coordinates

    def draw(self):
        self.myDrawing.drawCircle(self.radius, self.coordinates)
