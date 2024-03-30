from abc import ABC, abstractmethod
import turtle as t
from Shape import Triangle, Rectangle, Circle
from PIL import Image

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
    def __init__(self, details):
        self.details = details

    def drawLine(self, coordinates):
        t.penup()
        t.goto(coordinates[0][0], coordinates[0][1])
        t.pendown()
 
        for (x, y) in coordinates:
           t.goto(x, y)


    def drawCircle(self, radius, coordinates):
        radius = float(radius)
        t.penup()
        t.goto(coordinates[0][0], coordinates[0][1]-radius)
        t.pendown()
        t.circle(radius)

    def draw(self, path=None):
        t.setup(width=600, height=500)
        screen = t.Screen()
        for _, section_value in self.details.items():
            t.color(section_value["color"])
            match section_value["shape"]:
                case 'triangle':
                    # Assuming Triangle is a properly defined class or function
                    Triangle(self, coordinates=section_value["coordinate"]).draw()
                case 'rectangle':
                    # Assuming Rectangle is a properly defined class or function
                    Rectangle(self, coordinates=section_value["coordinate"]).draw()
                case "circle":
                    # Assuming Circle is a properly defined class or function
                    Circle(self, radius=section_value["radius"], coordinates=section_value["coordinate"]).draw()
                case _:
                    print("Shape not found")
            t.end_fill()

        if path:
            file_name = '.'.join(path.split('.')[:-1])
            file_extension = path.split('.')[-1]
            # Save the drawing to a PostScript file
            canvas = screen.getcanvas()
            canvas.postscript(file="drawing.ps", colormode='color')
            
            # Convert the PostScript file to PNG or JPG
            with Image.open("drawing.ps") as img:
                img.save(file_name+"."+file_extension)
        else:
            t.done()
            # print("Done")

        # Save the drawing to a PostScript file
        canvas = screen.getcanvas()
        canvas.postscript(file="drawing.ps", colormode='color')

        # Convert the PostScript file to PNG or JPG
        with Image.open("drawing.ps") as img:
            if path.endswith("png") or path.endswith("jpg"):
                img.save(path)
        


# class V2Drawing(Drawing):
#     def drawLine(self, x1, y1, x2, y2):
#         # Assume DP2's drawLine method requires reordering of parameters
#         print(f"V2 drawing line from ({x1},{y1}) to ({x2},{y2})")

#     def drawCircle(self, x, y, r):
#         print(f"V2 drawing circle at ({x},{y}) with radius {r}")

