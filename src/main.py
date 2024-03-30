import os

# get path of directory containing bot script
dir = os.path.dirname(os.path.realpath(__file__)) + "/"

# change current working directory to 'dir'
os.chdir(dir)

with open("../config/config.ini") as f:
    config = dict(x.rstrip().split(": ") for x in f)

print(config)