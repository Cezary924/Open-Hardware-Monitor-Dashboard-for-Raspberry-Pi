import requests

import log

# get PC info from OpenHardwareMonitor Server website
def get_pc_info(config):
    try:
        res = requests.get("http://" + config['ip'] + ":" + config['port'] + "/data.json")
    except Exception as e:
        raise Exception("Connection timed out!")
    else:
        if res.status_code != 200:
            raise Exception("Connection failed!")
        try:
            res = res.json()['Children'][0]['Children']
        except Exception as e:
            raise Exception(str(e))
        return res

# print info about error during requesting to Homebridge API
def print_err(e: Exception) -> None:
    log.print_log("An error has occured while requesting the OHM Server data.", str(e))