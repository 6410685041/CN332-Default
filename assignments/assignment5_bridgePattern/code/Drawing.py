from abc import ABC, abstractmethod
import turtle as t
from Shape import Triangle, Rectangle, Circle

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
    def __init__(self, shapes, colors):
        self.shapes = shapes
        self.colors = colors

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

    def draw(self, path):
        for index, shape, coordinate in self.shapes.items().enumerate():
            match shape:
                case 'Triangle':
                    Triangle(coordinate, self.colors[index]).draw()
                case 'Rectangle':
                    Rectangle(coordinate, self.colors[index]).draw()
                case "Circle":
                    Circle(coordinate, self.colors[index]).draw()
                case _:
                    print("Shape not found")
        turtle.done()
        # Setup the screen
        turtle.setup(width=600, height=500)
        screen = turtle.Screen()

        # Draw something
        create_drawing()

        # Save the drawing to a PostScript file
        canvas = screen.getcanvas()
        canvas.postscript(file="drawing.ps", colormode='color')

        # Convert the PostScript file to PNG
        img = Image.open("drawing.ps")
        img.save("drawing.png", "png")

        # Convert the PostScript file to JPG
        img.save("drawing.jpg", "jpeg")


# class V2Drawing(Drawing):
#     def drawLine(self, x1, y1, x2, y2):
#         # Assume DP2's drawLine method requires reordering of parameters
#         print(f"V2 drawing line from ({x1},{y1}) to ({x2},{y2})")

#     def drawCircle(self, x, y, r):
#         print(f"V2 drawing circle at ({x},{y}) with radius {r}")

