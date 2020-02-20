import json

class ConfigManager():
    '''
    Manages system variables to config.json
    '''

    def __init__(self):
        self.config_dict: dict = {} #Empty dictionary
        self.file_name: str = "./modules/config/config.json"
    
    def set_config(self, key: str, value: str) -> None:
        '''
        Set a configuration value with a given key and value

        @key: str -> the key
        @value: str -> value of the key
        @returns: None
        '''

        self.config_dict = json.loads(open(self.file_name, "r", encoding="utf-8").read())
        #self.config_dict.
        self.config_dict[key] = value
        with open(self.file_name, "w", encoding="utf-8") as f:
            f.writelines(json.dumps(self.config_dict, indent=4))

    def get_config(self, key: str) -> str:
        '''
        Returns value of config variable based on key
        
        @key: str -> the key to find in .json file
        @returns: str -> the value of environment variable
        '''

        self.config_dict = json.loads(open(self.file_name, "r", encoding="utf-8").read())
        return self.config_dict[key]