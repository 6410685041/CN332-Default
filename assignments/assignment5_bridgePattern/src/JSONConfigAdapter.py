import json
from .Configuration import Configuration

class JSONConfigAdapter(Configuration):

    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self.adaptee = json.load(file)

    def get_all(self):
        return self.adaptee
    
    def get(self, section, key):
        return self.adaptee[section][key]
    
    def get_section(self):
        return list(self.adaptee.keys())