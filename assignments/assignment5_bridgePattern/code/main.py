from Factory import Factory

config_ini_path = "../myhouse.ini"
config_json_path = "../myhouse.json"

f = Factory(config_ini_path)

d = f.getDrawing()
d.draw("main.png")
# coordinate_roof = json_config.get(query={'key':'house'})['roof']['coordinate']
# color_roof = json_config.get(query={'key':'house'})['roof']['color']
# roof = Triangle(coordinate=coordinate_roof, color=color_roof)
# roof.draw()