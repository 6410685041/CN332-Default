import json
import configparser
from abc import ABC, abstractmethod

# Interface for configuration reading
class ConfigReader(ABC):
    @abstractmethod
    def get(self, section, option):
        pass

    @abstractmethod
    def set(self, section, option, value):
        pass

# Adapter for INI files
class IniConfigAdapter(ConfigReader):
    def __init__(self, filepath):
        self.config = configparser.ConfigParser()
        self.config.read(filepath)

    def get(self, section, option):
        try:
            return self.config.get(section, option)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return None

    def set(self, section, option, value):
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, option, value)
        with open(filepath, 'w') as file:
            self.config.write(file)

# Adapter for JSON files
class JsonConfigAdapter(ConfigReader):
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.config = json.load(file)

    def get(self, section, option):
        try:
            # Assuming JSON structure is a dictionary of dictionaries
            return self.config[section][option]
        except KeyError:
            return None

    def set(self, section, option, value):
        if section not in self.config:
            self.config[section] = {}
        self.config[section][option] = value
        with open(self.filepath, 'w') as file:
            json.dump(self.config, file, indent=4)
