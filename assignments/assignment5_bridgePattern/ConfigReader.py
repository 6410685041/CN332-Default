import json
import configparser

class ConfigAdapter:
    def __init__(self, configAdaptee):
        self.config_file = configAdaptee
        self.config_data = {}
        self.read_config()

    def read_config(self):
        self.config_file.read_config()

    def get(self, key, default=None):
        """Retrieves a value from the configuration data."""
        return self.config_data.get(key, default)
    
    def get(self,section, key, default=None):
        """Retrieves a value from the configuration data."""
        return self.config_data.get(section,key, default)

class JsonConfigAdaptee(ConfigAdapter):
    def read_config(self):
        """Reads the JSON configuration file."""
        try:
            with open(self.config_file, 'r') as file:
                self.config_data = json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {self.config_file} was not found.")
        except json.JSONDecodeError:
            print(f"Error: The file {self.config_file} contains invalid JSON.")

class IniConfigAdaptee(ConfigAdapter):
    def read_config(self):
        """Reads the INI configuration file."""
        self.config_data = configparser.ConfigParser()
        try:
            self.config_data.read(self.config_file)
        except configparser.Error as e:
            print(f"Error reading INI file {self.config_file}: {e}")

    def get(self, section, key, default=None):
        """Retrieves a value from a specific section in the INI configuration data."""
        try:
            # return self.config_data.get(section, key)
            return self.config_data.get(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return default

"""
# Example usage
json_reader = JsonConfigAdapter('config.json')
print(json_reader.get('some_key'))

ini_reader = IniConfigAdapter('config.ini')
print(ini_reader.get('SectionName', 'some_key'))
"""

ini_reader = IniConfigAdaptee('myhouse.ini')
# print(ini_reader.get(section='roof', key='color'))

# json_reader = JsonConfigAdapter('myhouse.json')
# print(json_reader.get(key='house')["roof"])

ConfigAdapter = ConfigAdapter(ini_reader)
print(ConfigAdapter.get(section="roof",key='color'))