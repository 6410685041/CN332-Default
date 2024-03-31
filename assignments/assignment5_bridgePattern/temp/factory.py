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

    def draw(self, save_as=None):
        file_name = save_as.split('.')[0:]
        file_extension = save_as.split('.')[-1]
        
        match file_extension:
            case 'json':
                pass
            case 'ini':
                pass
            case _:
                pass


f=Factory('myhouse.json')
data = f.config.get()

for i in data:
    # for j in data[i]:
    #     print(j, data[i][j])
    #     print('-----------------')
    print(i, data[i])