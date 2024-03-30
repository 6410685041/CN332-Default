import INIConfigAdapter
from Shape import Triangle

config_ini_path = "../myhouse.ini"
config_json_path = "../myhouse.json"

ini_config = INIConfigAdapter(config_ini_path)
# json_config = JSONConfigAdapter(config_json_path)

ini_config.read_config()
# coordinate_roof = json_config.get(query={'key':'house'})['roof']['coordinate']
# color_roof = json_config.get(query={'key':'house'})['roof']['color']
# roof = Triangle(coordinate=coordinate_roof, color=color_roof)
# roof.draw()