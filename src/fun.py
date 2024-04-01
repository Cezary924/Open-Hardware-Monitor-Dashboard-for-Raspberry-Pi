
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

