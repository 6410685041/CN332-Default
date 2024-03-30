from ConfigAdapter import ConfigAdapter
from ConfigAdaptee import IniConfigAdaptee, JsonConfigAdaptee

class Factory:
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

    def draw(self):
        pass

f=Factory('myhouse.json')
data = f.get()

for i in data:
    # for j in data[i]:
    #     print(j, data[i][j])
    #     print('-----------------')
    print(i, data[i])