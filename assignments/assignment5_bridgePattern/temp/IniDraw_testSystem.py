from ConfigAdapter import ConfigAdapter
from ConfigAdaptee import IniConfigAdaptee
from Shape.shape import Rectangle, Triangle, Circle

ini_reader = IniConfigAdaptee('myhouse.ini')
adapter = ConfigAdapter(ini_reader)
# print(adapter.get(query={'section':'house', 'key':'color'}),adapter.get(query={'section':'house', 'key':'coordinate'}))

coordinate = adapter.get(query={'section':'house', 'key':'coordinate'})
color = adapter.get(query={'section':'house', 'key':'color'})
all = adapter.get()
rectangle = Rectangle(coordinate=coordinate, color=color)
# rectangle.draw()

for i in all:
    print(i)
    for j in all[i]:
        print(j, all[i][j])
    print('-----------------')
    
coordinate_rec = adapter.get(query={'section':'house', 'key':'coordinate'})
color_rec = adapter.get(query={'section':'house', 'key':'color'})
rectangle = Rectangle(coordinate=coordinate_rec, color=color_rec)
rectangle.draw()

coordinate_tri = adapter.get(query={'section':'roof', 'key':'coordinate'})
color_tri = adapter.get(query={'section':'roof', 'key':'color'})
triangle = Triangle(coordinate=coordinate_tri, color=color_tri)
triangle.draw()

coordinate_cir = adapter.get(query={'section':'window', 'key':'coordinate'})
color_cir = adapter.get(query={'section':'window', 'key':'color'})
radius_cir = adapter.get(query={'section':'window', 'key':'radius'})
circle = Circle(coordinate=coordinate_cir, color=color_cir, radius=radius_cir)
circle.draw()
