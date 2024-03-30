from INIConfigAdapter import INIConfigAdapter
from JSONConfigAdapter import JSONConfigAdapter
from Drawing import V1Drawing

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
        shapes = {}
        colors = []
        for object in self.config.get_section:
            shapes[self.config.get(object,"shape")] = self.config.get(object, "coordinate")
            colors.append(self.config.get(object, "color"))
        return V1Drawing(shapes, colors)
        
    


            
f=Factory('../myhouse.json')
