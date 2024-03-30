from ConfigAdapter import ConfigAdapter
from ConfigAdaptee import IniConfigAdaptee, JsonConfigAdaptee

class Configuration:
    def __init__(self, config_file):
        try:
            if config_file.endswith('.ini'):
                self.config = ConfigAdapter(IniConfigAdaptee(config_file))
            elif config_file.endswith('.json'):
                self.config = ConfigAdapter(JsonConfigAdaptee(config_file))
            else:
                raise ValueError("Invalid config file format")
        except Exception as e:
            print(f"Error: {e}")
    
    def get(self, query=None):
        return self.config.get()
    
    def draw(self):
        pass