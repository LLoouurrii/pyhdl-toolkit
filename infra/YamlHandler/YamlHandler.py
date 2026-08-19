from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap

class YamlHandler:
    
    def __init__(self, name_yaml):
        self.yaml = YAML()
        self.name_yaml = name_yaml
    
    def write_yaml(self, data):
        yaml = YAML()
        with open(self.name_yaml, "a", encoding="utf-8") as file:
                
            yaml.dump(data, file)
    
    def line_break(self):
        with open(self.name_yaml, "a", encoding="utf-8") as file:
            file.write("\n")
            
    def clean_yaml(self):
        with open(self.name_yaml, "w", encoding="utf-8") as file:
            pass