from Configuration import Configuration
import configparser

class INIConfigAdapter(Configuration):
    def __init__(self, file_path):
        self.shape = []
        self.adaptee = configparser.ConfigParser()
        self.adaptee.read(file_path)

    def get_sections(self):
        for section in self.adaptee.sections():
            print(section)

    def get_all(self):
        # Iterate over all sections
        for section in self.adaptee.sections():
            print(f"[{section}]")
            # Iterate over all keys in each section
            for key in self.adaptee[section]:
                # Accessing each value by key
                value = self.adaptee[section][key]
                print(f"{key} = {value}")
            print()
    
    def draw():
        pass
    
    def get(self, section, key):
        return self.adaptee.get(section, key)
        

