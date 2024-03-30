class ConfigAdapter:
    def __init__(self, configAdaptee):
        self.config_file = configAdaptee
        self.config_data = {}
        self.read_config()

    def read_config(self):
        self.config_file.read_config()
    
    def get(self, query=None):
        """Retrieves a value from the configuration data."""
        return self.config_file.get(query)