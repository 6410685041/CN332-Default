import json
from .Configuration import Configuration

class JSONConfigAdapter(Configuration):

    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self.adaptee = json.load(file)

    def get_all(self):
        data = {}
        for section in self.adaptee:
            data[section] = {}
            for key, val in self.adaptee[section].items():
                if key=="coordinate":
                    val = self.get(section, 'coordinate')
                data[section][key] = val
    
        return data
    
    def get(self, section, key):
        data = self.adaptee[section][key]
        
        # convert coordinate string to tuple of floats
        if key == "coordinate":
            points = data.strip('()').split('),(')
            return [tuple(map(float, point.split(','))) for point in points]
        return data
    
    def get_section(self):
        return list(self.adaptee.keys())