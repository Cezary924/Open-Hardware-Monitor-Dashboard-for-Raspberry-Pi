import os, sys, re, signal, time
import log, config, ohm, fun

# get path of directory containing bot script
dir = os.path.dirname(os.path.realpath(__file__)) + "/"

# change current working directory to 'dir'
os.chdir(dir)

# write stdout to both console and file
sys.stdout = log.Logger()

# find current version number
version = "Error!"
try:
    with open('../SECURITY.md', 'r') as file:
        content = file.read()
        match = re.compile(r'\b\d+\.\d+\b').search(content)
        if match:
            version = match.group()
except Exception as e:
    pass

# starting log message
log.print_log("", "", 1, version)

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

# main loop
while True:
    try:
        res = ohm.get_pc_info(configuration)
    except Exception as e:
        ohm.print_err(e)
    else:
        cpu = {}
        ram = {}
        gpu = {}
        try:
            c = fun.find_cpu_loc(res)
            cpu['load'] = fun.find_cpu_load(c, res)
            cpu['temp'] = fun.find_cpu_temp(c, res)
            r = fun.find_ram_loc(res)
            ram['load'] = fun.find_ram_load(r, res)
            g = fun.find_gpu_loc(res)
            gpu['load'] = fun.find_gpu_load(g, res)
            gpu['temp'] = fun.find_gpu_temp(g, res)
            gpu['memload'] = fun.find_gpu_memload(g, res)
        except Exception as e:
            fun.print_err(e)
        pc = {'cpu': cpu, 'ram': ram, 'gpu': gpu}
        log.print_log(str(pc))
    finally:
        time.sleep(updateInterval)