import json
import configparser

class ConfigReader:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_data = {}
        self.read_config()

    def read_config(self):
        """To be implemented by subclasses."""
        raise NotImplementedError

    def get(self, key, default=None):
        """Retrieves a value from the configuration data."""
        return self.config_data.get(key, default)

class JsonConfigReader(ConfigReader):
    def read_config(self):
        """Reads the JSON configuration file."""
        try:
            with open(self.config_file, 'r') as file:
                self.config_data = json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {self.config_file} was not found.")
        except json.JSONDecodeError:
            print(f"Error: The file {self.config_file} contains invalid JSON.")

class IniConfigReader(ConfigReader):
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
            return self.config_data.get(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return default

"""
# Example usage
json_reader = JsonConfigReader('config.json')
print(json_reader.get('some_key'))

ini_reader = IniConfigReader('config.ini')
print(ini_reader.get('SectionName', 'some_key'))
"""

ini_reader = IniConfigReader('myhouse.ini')
print(ini_reader.get('roof', 'color'))
