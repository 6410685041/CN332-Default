from src.Factory import Factory

config_path = "myhouse.ini"
# config_path = "./myhouse.json"

f = Factory(config_path)

d = f.getDrawing()
# d.draw("my_house.png")
# d.draw("my_house.jpg")
d.draw("test.png")
# coordinate_roof = json_config.get(query={'key':'house'})['roof']['coordinate']
# color_roof = json_config.get(query={'key':'house'})['roof']['color']
# roof = Triangle(coordinate=coordinate_roof, color=color_roof)
# roof.draw()