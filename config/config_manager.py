import yaml

class ConfigManager:

    _config = None

    @classmethod
    def initialize(cls, environment):

        if cls._config is None:
            with open(f"config/{environment}.yaml", "r") as file:
                cls._config = yaml.safe_load(file)

    @classmethod
    def get(cls, key):
        return cls._config[key]