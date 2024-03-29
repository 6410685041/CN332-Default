import Shape
import turtle as t

class Rectangle(Shape):
    def drawline(self, distance):
        t.fd(distance)