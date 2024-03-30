from abc import ABC, abstractmethod
import turtle as t

# Abstract Drawing class
class Drawing(ABC):
    @abstractmethod
    def drawLine(self, coordinates):
        pass

    @abstractmethod
    def drawCircle(self, radius, coordinates):
        pass

# Concrete Drawing implementations
class V1Drawing(Drawing):
    def drawLine(self, coordinates):
        t.penup()
        t.goto(self.coordinates[0][0], self.coordinates[0][1])
        t.pendown()
 
        for (x, y) in self.coordinates:
           t.goto(x, y)


    def drawCircle(self, radius, coordinates):
        t.penup()
        t.goto(self.coordinates[0][0], self.coordinates[0][1]-self.radius)
        t.pendown()
        t.circle(self.radius)

# class V2Drawing(Drawing):
#     def drawLine(self, x1, y1, x2, y2):
#         # Assume DP2's drawLine method requires reordering of parameters
#         print(f"V2 drawing line from ({x1},{y1}) to ({x2},{y2})")

#     def drawCircle(self, x, y, r):
#         print(f"V2 drawing circle at ({x},{y}) with radius {r}")

