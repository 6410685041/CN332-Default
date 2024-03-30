class Configuration:
    def __init__(self, config):
        self.data = self.get()
    
    def get(self, query=None):
        return self.config.get()