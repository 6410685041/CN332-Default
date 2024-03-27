from ConfigAdapter import ConfigAdapter
from ConfigAdaptee import IniConfigAdaptee, JsonConfigAdaptee

"""
# Example usage
json_reader = JsonConfigAdapter('config.json')
print(json_reader.get('some_key'))

ini_reader = IniConfigAdapter('config.ini')
print(ini_reader.get('SectionName', 'some_key'))
"""

ini_reader = IniConfigAdaptee('myhouse.ini')
ini_adapter = ConfigAdapter(ini_reader)
print("ini file")
print(ini_adapter.get(query={'section':'roof', 'key':'color'}))


json_reader = JsonConfigAdaptee('myhouse.json')
json_adapter = ConfigAdapter(json_reader)
print("json file")
print(json_adapter.get(query={'key':'house'}))