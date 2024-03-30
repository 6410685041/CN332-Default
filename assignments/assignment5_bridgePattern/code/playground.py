# import configparser
# from INIConfigAdapter import INIConfigAdapter

# config_ini_path = "../myhouse.ini"

# ini_config = INIConfigAdapter(config_ini_path)

# a = ini_config.get("roof", "color")
b = ini_config.get_all()

# print(a)
print(b)
# import json

# print(a)
import json
from JSONConfigAdapter import JSONConfigAdapter

# Assuming 'data.json' contains your JSON data
file_path = './temp/myhouse.json'


json_config = JSONConfigAdapter(file_path)

print(json_config.get_section())

