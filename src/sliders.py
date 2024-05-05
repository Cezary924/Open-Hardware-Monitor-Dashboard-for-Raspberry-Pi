import tkinter as tk
import math

width, height, refreshRate, updateInterval, box_width, box_height, max_i, max_j, arc_w, x1, y1, x2, y2, x, y, r = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
canvas = []
pointers = []
def set_values(_width, _height, _refreshRate, _updateInterval, _max_i = 2, _max_j = 3):
    global width, height, refreshRate, updateInterval, box_width, box_height, max_i, max_j, arc_w, x1, y1, x2, y2, x, y, r
    width = _width
    height = _height
    refreshRate = _refreshRate
    updateInterval = _updateInterval
    max_i = _max_i
    max_j = _max_j
    box_width = _width/_max_j
    box_height = _height/_max_i
    smallest = 0
    if box_width > box_height:
        smallest = box_height
    else:
        smallest = box_width
    margin = 10
    smallest -= 2*margin
    arc_w = int(smallest/(1.5*margin))
    x1, y1, x2, y2 = (box_width-smallest)/2, (box_height-smallest)/2+arc_w*2, box_width-((box_width-smallest)/2), box_height-((box_height-smallest)/2+arc_w*2)+arc_w*4
    x, y, r = (x2-x1)/2+(box_width-x2), (y2-y1)/2+(box_height-y2), (x2-x1)/2.5

def animate_sliders(window, t, olov, nlov, step = 0):
    global refreshRate, updateInterval
    delta = [(olov[0] - nlov[0])/(refreshRate * updateInterval), (olov[1] - nlov[1])/(refreshRate * updateInterval),
             (olov[2] - nlov[2])/(refreshRate * updateInterval), (olov[3] - nlov[3])/(refreshRate * updateInterval),
             (olov[4] - nlov[4])/(refreshRate * updateInterval), (olov[5] - nlov[5])/(refreshRate * updateInterval)]
    current_values = [olov[0] - delta[0] * step, olov[1] - delta[1] * step,
                      olov[2] - delta[2] * step, olov[3] - delta[3] * step,
                      olov[4] - delta[4] * step, olov[5] - delta[5] * step]
    try:
        if t == 2:
            pass#update_sliders_2([[current_values[0], current_values[1], current_values[2]], [current_values[3], current_values[4], current_values[5]]])
        else:
            update_sliders_1([[current_values[0], current_values[1], current_values[2]], [current_values[3], current_values[4], current_values[5]]])
        if step < refreshRate * updateInterval:
            step += 1
            window.update()
            window.after(int(step/(refreshRate*updateInterval)), animate_sliders, window, t, olov, nlov, step)
    except:
        pass

def draw_sliders_1(window, list_of_text):
    global canvas, pointers, max_i, max_j
    for i in range(max_i):
        _canvas = []
        _pointers = []
        for j in range(max_j):
            c = tk.Canvas(window, width = width/max_j, height = height/max_i, bg = 'black', highlightthickness = 0)
            c.grid(column=j, row=i)
            rgb1 = (234, 0, 0)
            rgb2 = (234, 234, 0)
            rgb3 = (0, 234, 0)
            q = 0
            while q < 180:
                if q < 60 - 8:
                    c.create_arc(x1, y1, x2, y2, start = q, extent = 2, outline = "#%02x%02x%02x" % rgb1, width = arc_w, style=tk.ARC)
                elif q < 120 + 8:
                    c.create_arc(x1, y1, x2, y2, start = q, extent = 2, outline = "#%02x%02x%02x" % rgb2, width = arc_w, style=tk.ARC)
                else:
                    c.create_arc(x1, y1, x2, y2, start = q, extent = 2, outline = "#%02x%02x%02x" % rgb3, width = arc_w, style=tk.ARC)
                q += 8
            in_radian = math.radians(180)
            line = c.create_line(x, y+4*arc_w, (x+r*math.cos(in_radian)), (y+4*arc_w-r*math.sin(in_radian)), width = int(arc_w/2), arrow = 'last', fill = "white")
            circle = c.create_oval(x-arc_w*1.35, y+arc_w*2.35, x+arc_w*1.35, y+arc_w*5.15, fill = 'blue', outline = "")
            c.create_text(x, y+7*arc_w, text = list_of_text[i][j][0], fill = "white", font = f'Helvetica {str(arc_w+6)} bold')
            c.create_text(x, y+9*arc_w, text = list_of_text[i][j][1], fill = "white", font = f'Helvetica {str(arc_w+2)} italic')
            label = c.create_text(x+1, y-2+4*arc_w, text = "-", fill = "white", font = f'Helvetica {str(arc_w+2)}')
            _canvas.append(c)
            _pointers.append((line, circle, label))
        canvas.append(_canvas)
        pointers.append(_pointers)

def update_sliders_1(list_of_values):
    global canvas, pointers, max_i, max_j
    for i in range(max_i):
        for j in range(max_j):
            canvas[i][j].delete(pointers[i][j][0])
            canvas[i][j].delete(pointers[i][j][1])
            canvas[i][j].delete(pointers[i][j][2])
            val = int(list_of_values[i][j] * 1.8)
            if val > 180:
                val = 180
            elif val < 0:
                val = 0
            in_radian = math.radians(180-val)
            line = canvas[i][j].create_line(x, y+4*arc_w, (x+r*math.cos(in_radian)), (y+4*arc_w-r*math.sin(in_radian)), width = int(arc_w/2), arrow = 'last', fill = "white")
            circle = canvas[i][j].create_oval(x-arc_w*1.35, y+arc_w*2.35, x+arc_w*1.35, y+arc_w*5.15, fill = 'blue', outline = "")
            label = canvas[i][j].create_text(x+1, y-2+4*arc_w, text = str(int(list_of_values[i][j])), fill = "white", font = f'Helvetica {str(arc_w+2)}')
            pointers[i][j] = (line, circle, label)

