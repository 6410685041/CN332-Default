from ConfigAdapter import ConfigAdapter
from ConfigAdaptee import IniConfigAdaptee
from Shape.shape import Rectangle

ini_reader = IniConfigAdaptee('myhouse.ini')
adapter = ConfigAdapter(ini_reader)
# print(adapter.get(query={'section':'house', 'key':'color'}),adapter.get(query={'section':'house', 'key':'coordinate'}))

coordinate = adapter.get(query={'section':'house', 'key':'coordinate'})
color = adapter.get(query={'section':'house', 'key':'color'})
rectangle = Rectangle(coordinate=coordinate, color=color)
rectangle.draw()