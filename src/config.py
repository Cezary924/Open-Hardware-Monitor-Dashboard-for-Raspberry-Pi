import json, os

import log

# check if configuration file exists
def check_file(path: str) -> bool:
    return os.path.isfile(path)

# create configuration file
def create_config(path: str) -> None:
    with open(path, 'w') as f:
        json.dump({"ip": "XXX.XXX.XXX.XXX", "port": "XXXX", "updateInterval": "XXXXXX"}, f, indent = 4)
    log.print_log("A config file has been created successfully.", "Please, edit the configuration and run the script again.")

# save configuartion to file
def save_config(path: str, config_dict: dict) -> None:
    with open(path, 'w') as f:
        json.dump(config_dict, f, indent = 4)

# load configuartion from file
def load_config(path: str) -> dict:
    with open(path, 'r') as f:
        loaded_config = json.load(f)
    return loaded_config

# check correctness of loaded configuration
def check_correctness(configuration: dict, path: str) -> None:
    #TODO
    pass

# print info about error during preparing configuration
def print_err(e: Exception) -> None:
    log.print_log("An error has occured while loading the config file.", str(e))