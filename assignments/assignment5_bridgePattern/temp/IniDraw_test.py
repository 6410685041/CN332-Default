import turtle as t
import math
import re

from ConfigAdapter import ConfigAdapter
from ConfigAdaptee import IniConfigAdaptee, JsonConfigAdaptee

# for transfer from string to tuple
def parse_points(input_str):
    # Removing parentheses and splitting by commas
    points = input_str.strip('()').split('),(')
    # Converting each point from string to a tuple of integers
    return [tuple(map(int, point.split(','))) for point in points]

# for calculate angle
def calculate_angle(A, B, C):
    # Create vectors AB and BC
    AB = (B[0] - A[0], B[1] - A[1])
    BC = (C[0] - B[0], C[1] - B[1])

    # Calculate the dot product of AB and BC
    dot_product = AB[0] * BC[0] + AB[1] * BC[1]

    # Calculate the magnitudes of AB and BC
    magnitude_AB = math.sqrt(AB[0] ** 2 + AB[1] ** 2)
    magnitude_BC = math.sqrt(BC[0] ** 2 + BC[1] ** 2)

    # Calculate the cosine of the angle using the dot product formula
    cos_angle = dot_product / (magnitude_AB * magnitude_BC)

    # Calculate the angle in radians and then convert to degrees
    angle = math.acos(cos_angle)  # Angle in radians
    angle_degrees = math.degrees(angle)  # Convert to degrees

    return angle_degrees

BOUND = 100

# # INI file
ini_reader = IniConfigAdaptee('myhouse.ini')
adapter = ConfigAdapter(ini_reader)

coordinate_rectangle = adapter.get(query={'section':'house', 'key':'coordinate'})
rectangleCoordinate = parse_points(coordinate_rectangle)
print(rectangleCoordinate)
rectangleCoordinate.sort()
print(rectangleCoordinate)

width = abs(rectangleCoordinate[0][0]-rectangleCoordinate[1][0])*BOUND
height = abs(rectangleCoordinate[0][1]-rectangleCoordinate[1][1])*BOUND

coordinate_triangle = adapter.get(query={'section':'roof', 'key':'coordinate'})
triangleCoordinate = parse_points(coordinate_triangle)

angle = []
angle.append(calculate_angle(triangleCoordinate[0],triangleCoordinate[1],triangleCoordinate[2]))
angle.append(calculate_angle(triangleCoordinate[1],triangleCoordinate[2],triangleCoordinate[0]))

t.color(adapter.get(query={'section':'house', 'key':'color'}))
t.begin_fill() 

# rectangle
for _ in range(2): 
  t.forward(width) 
  t.right(90)
  t.forward(height) 
  t.right(90)
t.end_fill() 

t.color(adapter.get(query={'section':'roof', 'key':'color'}))
t.begin_fill() 

# triangle
t.forward(100) 
for i in range(2): 
  t.right(angle[i]) 
  t.forward(100) 
t.end_fill()