from .INIConfigAdapter import INIConfigAdapter
from .JSONConfigAdapter import JSONConfigAdapter
from .Drawing import V1Drawing

class Factory:
    def __init__(self, config_file):
        try:
            if config_file.endswith('.ini'):
                self.config = INIConfigAdapter(config_file)
            elif config_file.endswith('.json'):
                self.config = JSONConfigAdapter(config_file)
            else:
                raise ValueError("Invalid config file format")
        except Exception as e:
            print(f"Error: {e}")
    
    def getDrawing(self):
        details = self.config.get_all()
        return V1Drawing(details)
