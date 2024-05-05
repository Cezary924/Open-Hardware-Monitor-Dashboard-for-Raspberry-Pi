import os, sys, re, signal, time, copy
import tkinter as tk

import log, config, ohm, fun, sliders

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
window = None
def ctrl_c(signal = None, frame = None) -> None:
    global window
    if window != None:
        window.destroy()
        window = None
        log.print_log("The window has been destroyed.")
    log.print_log("", "", -1)
    sys.exit(0)
signal.signal(signal.SIGINT, ctrl_c)
def ctrl_c_window(signal = None) -> None:
    global window
    if window != None:
        window.withdraw()
        window.quit()
        window = None
        log.print_log("The window has been destroyed.")

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
        updateInterval = configuration['updateInterval']
    except:
        pass
    if updateInterval < 1:
        updateInterval = 1

# get dashboard type
dashboardType = 1
if 'dashboardType' in configuration:
    try:
        dashboardType = configuration['dashboardType']
    except:
        pass
    if dashboardType not in [1, 2]:
        dashboardType = 1

# window preparation
window = tk.Tk()
width, height, refreshRate = configuration['display']['width'], configuration['display']['height'], configuration['display']['refreshRate']
window.resizable(False, False)
window.geometry(str(width) + "x" + str(height))
window.after(100, lambda: window.wm_attributes('-fullscreen', 'true'))
sliders.set_values(width, height, refreshRate, updateInterval)
if dashboardType == 2:
    #sliders.draw_sliders_2(window, [[["CPU", "Load [%]"], ["RAM", "Load [%]"], ["GPU", "Load [%]"]], 
    pass#                          [["CPU", "Temp [°C]"], ["VRAM", "Load [%]"], ["GPU", "Temp [°C]"]]])
else:
    sliders.draw_sliders_1(window, [[["CPU", "Load [%]"], ["RAM", "Load [%]"], ["GPU", "Load [%]"]], 
                              [["CPU", "Temp [°C]"], ["VRAM", "Load [%]"], ["GPU", "Temp [°C]"]]])
window.bind("<Control-c>", ctrl_c_window)
window.protocol("WM_DELETE_WINDOW", ctrl_c_window)
window.update()
log.print_log("The window has been created.")

def update_sliders_async(window, t, old_data, data):
    sliders.animate_sliders(window, t, [old_data['cpu']['load'], old_data['ram']['load'], old_data['gpu']['load'], 
                                  old_data['cpu']['temp'], old_data['gpu']['memload'], old_data['gpu']['temp']], 
                                  [data['cpu']['load'], data['ram']['load'], data['gpu']['load'], 
                                  data['cpu']['temp'], data['gpu']['memload'], data['gpu']['temp']])

cpu = {'load': 0.00, 'temp': 0.00}
ram = {'load': 0.00}
gpu = {'load': 0.00, 'temp': 0.00, 'memload': 0.00}
pc = {'cpu': cpu, 'ram': ram, 'gpu': gpu}
pc_old = None

# main loop
while True:
    try:
        res = ohm.get_pc_info(configuration)
    except Exception as e:
        ohm.print_err(e)
    else:
        try:
            pc_old = copy.deepcopy(pc)
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
        if window != None:
            update_sliders_async(window, dashboardType, pc_old, pc)
    finally:
        time.sleep(updateInterval)
        try:
            window.update()
        except Exception as e:
            pass