import requests

# get PC info from OpenHardwareMonitor Server website
def get_pc_info(config):
    res = requests.get("http://" + config['ip'] + ":" + config['port'] + "/data.json")
    if res.status_code != 200:
        raise Exception("Connection failed")
    try:
        res = res.json()['Children'][0]['Children']
    except Exception as e:
        raise Exception(str(e))
    return res
