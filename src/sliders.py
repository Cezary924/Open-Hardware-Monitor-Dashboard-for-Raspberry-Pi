import tkinter as tk
import math

width, height, max_i, max_j, arc_w, x1, y1, x2, y2, x, y, r = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
canvas = []
pointers = []
def set_values(_width, _height, _max_i = 2, _max_j = 3):
    global width, height, max_i, max_j, arc_w, x1, y1, x2, y2, x, y, r
    width = _width
    height = _height
    max_i = _max_i
    max_j = _max_j
    arc_w = 10
    x1, y1, x2, y2 = 10, 10, width/max_j-10, height/max_i-10
    x, y, r = (x2-x1)/2+10, (y2-y1)/2+10, 66

def draw_sliders(window, list_of_text):
    global canvas, pointers, max_i, max_j
    for i in range(max_i):
        _canvas = []
        _pointers = []
        for j in range(max_j):
            c = tk.Canvas(window, width = width/max_j, height = height/max_i, bg = 'black', highlightthickness = 0)
            c.grid(column=j, row=i)
            c.create_arc(x1, y1, x2, y2, start = 0, extent = 60, outline = 'red', width = arc_w, style=tk.ARC)
            c.create_arc(x1, y1, x2, y2, start = 60, extent = 60, outline = 'yellow', width = arc_w, style=tk.ARC)
            c.create_arc(x1, y1, x2, y2, start = 120, extent = 60, outline = 'green', width = arc_w, style=tk.ARC)
            in_radian = math.radians(180)
            line = c.create_line(x, y, (x+r*math.cos(in_radian)), (y-r*math.sin(in_radian)), width = int(arc_w/2), arrow = 'last', fill = "white")
            circle = c.create_oval(x-10, y-10, x+10, y+10, fill = 'blue', outline = "")
            c.create_text(x, y+30, text = list_of_text[i][j][0], fill = "white", font = 'Helvetica 16 bold')
            c.create_text(x, y+50, text = list_of_text[i][j][1], fill = "white", font = 'Helvetica 12 italic')
            label = c.create_text(x+1, y+1, text = "-", fill = "white", font = 'Helvetica 10')
            _canvas.append(c)
            _pointers.append((line, circle, label))
        canvas.append(_canvas)
        pointers.append(_pointers)

def update_sliders(window, list_of_values):
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
            line = canvas[i][j].create_line(x, y, (x+r*math.cos(in_radian)), (y-r*math.sin(in_radian)), width = int(arc_w/2), arrow = 'last', fill = "white")
            circle = canvas[i][j].create_oval(x-10, y-10, x+10, y+10, fill = 'blue', outline = "")
            label = canvas[i][j].create_text(x+1, y+1, text = str(list_of_values[i][j]), fill = "white", font = 'Helvetica 10')
            pointers[i][j] = (line, circle, label)