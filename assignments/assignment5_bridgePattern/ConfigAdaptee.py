import configparser
import json
from ConfigAdapter import ConfigAdapter

class IniConfigAdaptee(ConfigAdapter):
    def read_config(self):
        """Reads the INI configuration file."""
        self.config_data = configparser.ConfigParser()
        try:
            self.config_data.read(self.config_file)
        except configparser.Error as e:
            print(f"Error reading INI file {self.config_file}: {e}")

    def get(self, query, default=None):
        """Retrieves a value from a specific section in the INI configuration data."""
        try:
            # return self.config_data.get(section, key)
            section = query['section']
            key = query['key']
            return self.config_data.get(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return default

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
            
    def get(self, query, default=None):
        """Retrieves a value from a specific section in the JSON configuration data."""
        try:
            # return self.config_data.get(section, key)
            return self.config_data.get(query['key'])
        except KeyError:
            return default