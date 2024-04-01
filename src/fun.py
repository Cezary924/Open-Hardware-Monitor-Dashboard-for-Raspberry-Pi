
def find_component_loc(text, pc, rev = False):
    if rev:
        i = len(pc) - 1
        while(text not in pc[i]['Text']):
            if i > 0:
                i = i - 1
            else:
                return -1
        return i
    else:
        i = 0
        while(text not in pc[i]['Text']):
            if i < len(pc) - 1:
                i = i + 1
            else:
                return -1
        return i

def calculate_component_value(pc, text):
    i = find_component_loc(text, pc)
    if i == -1:
        raise Exception("No supported GPU!")
    return float(pc[i]['Value'][:-2])

def calculate_average_component_value(pc):
    avg = 0
    for element in pc:
        avg = avg + float(element['Value'][:-2])
    return float(avg/len(pc))

def find_cpu_loc(pc):
    i = find_component_loc("Intel", pc)
    if i == -1:
        i = find_component_loc("AMD", pc)
    if i == -1:
        raise Exception("No supported CPU!")
    return i
def find_cpu_load(i, pc):
    j = find_component_loc("Load", pc[i]['Children'])
    if j == -1:
        raise Exception("No supported CPU!")
    return calculate_average_component_value(pc[i]['Children'][j]['Children'])
def find_cpu_temp(i, pc):
    j = find_component_loc("Temperatures", pc[i]['Children'])
    if j == -1:
        raise Exception("No supported CPU!")
    return calculate_average_component_value(pc[i]['Children'][j]['Children'])

def find_ram_loc(pc):
    i = find_component_loc("Memory", pc)
    if i == -1:
        raise Exception("No supported RAM!")
    return i
def find_ram_load(i, pc):
    j = find_component_loc("Load", pc[i]['Children'])
    if j == -1:
        raise Exception("No supported RAM!")
    return calculate_average_component_value(pc[i]['Children'][j]['Children'])

def find_gpu_loc(pc):
    i = find_component_loc("NVIDIA", pc, True)
    if i == -1:
        i = find_component_loc("AMD", pc, True)
    if i == -1:
        raise Exception("No supported GPU!")
    return i
def find_gpu_load(i, pc):
    j = find_component_loc("Load", pc[i]['Children'])
    if j == -1:
        raise Exception("No supported GPU!")
    return calculate_component_value(pc[i]['Children'][j]['Children'], "Core")
def find_gpu_temp(i, pc):
    j = find_component_loc("Temperatures", pc[i]['Children'])
    if j == -1:
        raise Exception("No supported GPU!")
    return calculate_average_component_value(pc[i]['Children'][j]['Children'])
def find_gpu_memload(i, pc):
    j = find_component_loc("Load", pc[i]['Children'])
    if j == -1:
        raise Exception("No supported GPU!")
    return calculate_component_value(pc[i]['Children'][j]['Children'], "Memory")

