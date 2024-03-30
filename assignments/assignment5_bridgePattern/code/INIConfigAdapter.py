from Configuration import Configuration
import configparser

class INIConfigAdapter(Configuration):
    def __init__(self, file_path):
        self.shape = []
        self.adaptee = configparser.ConfigParser()
        self.adaptee.read(file_path)

    def get_sections(self):
        return self.adaptee.sections()

    def get_all(self):
        data = {}
        for section in self.adaptee.sections():
            data[section] = {}
            for key, val in self.adaptee.items(section):
                data[section][key] = val
    
        return data
    
    def get(self, section, key):
        return self.adaptee.get(section, key)
        

