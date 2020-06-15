import yaml


class BaseApi:
    def yaml_load(self, file):
        return yaml.safe_load(open(file))

