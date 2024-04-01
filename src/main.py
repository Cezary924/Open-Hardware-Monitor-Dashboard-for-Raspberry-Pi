import os, sys, re, signal, time
import log, config, ohm, fun

# get path of directory containing bot script
dir = os.path.dirname(os.path.realpath(__file__)) + "/"

# change current working directory to 'dir'
os.chdir(dir)

# write stdout to both console and file
sys.stdout = log.Logger()

# handle exit (also with CTRL + C)
def ctrl_c(signal = None, frame = None) -> None:
    log.print_log("", "", -1)
    sys.exit(0)
signal.signal(signal.SIGINT, ctrl_c)

# check if configuration file exists
config_file_path = '../config/config.ini'
if not config.check_file(config_file_path):
    config.create_config(config_file_path)
    ctrl_c()

# load configuration from file & check its correctness
try:
    configuration = config.load_config(config_file_path)
    config.check_correctness(configuration, config_file_path)
except Exception as e:
    if str(e) != '':
        config.print_err(e)
    ctrl_c()

# get update interval
updateInterval = 3
if 'updateInterval' in configuration:
    try:
        updateInterval = int(configuration['updateInterval'])
    except:
        pass
    if updateInterval < 1:
        updateInterval = 1
