from Configuration import Configuration

class Factory:
    def __init__(self, config_file):
        config = Configuration(config_file)

    def get(self):
        pass

f=Factory('myhouse.json')
data = f.get()

for i in data:
    # for j in data[i]:
    #     print(j, data[i][j])
    #     print('-----------------')
    print(i, data[i])