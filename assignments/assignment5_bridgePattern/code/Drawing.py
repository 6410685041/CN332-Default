from abc import ABC, abstractmethod
import turtle as t
from Shape import Triangle, Rectangle, Circle
from PIL import Image, EpsImagePlugin

EpsImagePlugin.gs_mac_path = '/usr/local/bin/gs'  # Example for macOS

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
        t.begin_fill()
        t.penup()
        t.goto(coordinates[0][0], coordinates[0][1])
        t.pendown()
 
        for (x, y) in coordinates:
           t.goto(x, y)
        t.end_fill()


    def drawCircle(self, radius, coordinates):
        t.begin_fill()
        radius = float(radius)
        t.penup()
        t.goto(coordinates[0][0], coordinates[0][1]-radius)
        t.pendown()
        t.circle(radius)
        t.end_fill()

    def draw(self, path=None):
        t.setup(width=1080, height=720)
        screen = t.Screen()
        for _, section_value in self.details.items():
            t.color(section_value["color"])
            match section_value["shape"]:
                case 'triangle':
                    coordinates = section_value["coordinate"]
                    coordinates.append(coordinates[0])
                    Triangle(self, coordinates=coordinates).draw()
                case 'rectangle':
                    coordinates = section_value["coordinate"]
                    coordinates.sort()
                    coordinate_1 = (coordinates[1][0],coordinates[0][1])
                    coordinate_2 = (coordinates[0][0],coordinates[1][1])
                    coordinates.insert(1, coordinate_1)
                    coordinates.append(coordinate_2)
                    coordinates.append(coordinates[0])
                    Rectangle(self, coordinates=coordinates).draw()
                case "circle":
                    Circle(self, radius=section_value["radius"], coordinates=section_value["coordinate"]).draw()
                case _:
                    print("Shape not found")

        if path:
            file_name = '.'.join(path.split('.')[:-1])
            file_extension = path.split('.')[-1]
            print(file_extension)

            # Save the drawing to a PostScript file
            canvas = screen.getcanvas()
            canvas.postscript(file="drawing.ps", colormode='color')
            
            # Convert the PostScript file to PNG or JPG
            with Image.open("drawing.ps") as img:
                img.save(file_name+"."+file_extension)
        else:
            t.done()

        


# class V2Drawing(Drawing):
#     def drawLine(self, x1, y1, x2, y2):
#         # Assume DP2's drawLine method requires reordering of parameters
#         print(f"V2 drawing line from ({x1},{y1}) to ({x2},{y2})")

#     def drawCircle(self, x, y, r):
#         print(f"V2 drawing circle at ({x},{y}) with radius {r}")

