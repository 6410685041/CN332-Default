from ConfigAdapter import ConfigAdapter
from ConfigAdaptee import JsonConfigAdaptee
from Shape.shape import Rectangle, Triangle, Circle

json_reader = JsonConfigAdaptee('myhouse.json')
adapter = ConfigAdapter(json_reader)

# print(adapter.get(query={'key':'house'}))

coordinate_roof = adapter.get(query={'key':'house'})['roof']['coordinate']
color_roof = adapter.get(query={'key':'house'})['roof']['color']
roof = Triangle(coordinate=coordinate_roof, color=color_roof)
roof.draw()