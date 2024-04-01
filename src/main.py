import os, requests

# get path of directory containing bot script
dir = os.path.dirname(os.path.realpath(__file__)) + "/"

# change current working directory to 'dir'
os.chdir(dir)

# read config from configuration file
#TODO errors
with open("../config/config.ini") as f:
    config = dict(x.rstrip().split(": ") for x in f)

#TODO errors
res = requests.get("http://" + config['ip'] + ":" + config['port'] + "/data.json")

if res.status_code != 200:
    raise Exception("Connection failed")

res = res.json()
