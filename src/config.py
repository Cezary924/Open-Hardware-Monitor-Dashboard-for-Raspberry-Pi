import json, os, re

import log

# check if configuration file exists
def check_file(path: str) -> bool:
    return os.path.isfile(path)

# create configuration file
def create_config(path: str) -> None:
    with open(path, 'w') as f:
        json.dump({"ip": "XXX.XXX.XXX.XXX", "port": "8085", "width": "480", "height": "320", "updateInterval": "3"}, f, indent = 4)
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
    if "ip" not in configuration.keys():
        raise Exception("No 'ip' key in the configuration file!")
    else:
        if re.search(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', configuration["ip"]) == None:
            raise Exception('Wrong IP address format!')
    if "port" not in configuration.keys():
        raise Exception("No 'port' key in the configuration file!")
    else:
        if re.search(r'^\d+$', configuration["port"]) == None:
            raise Exception('Wrong port format!')
    if "width" not in configuration.keys():
        raise Exception("No 'width' key in the configuration file!")
    else:
        if re.search(r'^\d+$', configuration["width"]) == None:
            raise Exception('Wrong width format!')
    try:
        configuration["width"] = int(configuration["width"])
    except Exception:
        raise Exception('Wrong width format!')
    if "height" not in configuration.keys():
        raise Exception("No 'height' key in the configuration file!")
    else:
        if re.search(r'^\d+$', configuration["height"]) == None:
            raise Exception('Wrong height format!')
    try:
        configuration["height"] = int(configuration["height"])
    except Exception:
        raise Exception('Wrong height format!')
    if "updateInterval" not in configuration.keys():
        raise Exception("No 'updateInterval' key in the configuration file!")
    else:
        if re.search(r'^\d+$', configuration["updateInterval"]) == None:
            raise Exception('Wrong updateInterval format!')
    try:
        configuration["updateInterval"] = int(configuration["updateInterval"])
    except Exception:
        raise Exception('Wrong updateInterval format!')

# print info about error during preparing configuration
def print_err(e: Exception) -> None:
    log.print_log("An error has occured while loading the config file.", str(e))