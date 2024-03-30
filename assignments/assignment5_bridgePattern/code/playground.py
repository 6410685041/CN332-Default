import configparser
from INIConfigAdapter import INIConfigAdapter

config_ini_path = "../myhouse.ini"

ini_config = INIConfigAdapter(config_ini_path)

# a = ini_config.get("roof", "color")
b = ini_config.get_all()

# print(a)
print(b)
# import json

