from typing import Literal
from PIL import Image
import numpy as np

base = np.asarray(Image.open("./base.png"))

canvas = base.copy()
canvas.setflags(write=True)

def invert_axis(axis: Literal['x', 'y']):
    return 'x' if axis == 'y' else 'y'

def index(v: int):
    return int(112 + v * 10)

def draw_point(x: int, y: int, color = [255,74,121,255]):
    canvas[y][x] = color
    for n in range (-1, 2):
        canvas[y+n][x] = color 
        canvas[y][x+n] = color

def draw_line(x1: int, x2: int, y1: int, y2: int):    
    x1, x2 = index(x1), index(x2)
    y1, y2 = index(-y1), index(-y2)

    dx = abs(x1 - x2) 
    dy = abs(y1 - y2) 
    steps = max(dx, dy)
  
    xinc = dx/steps
    yinc = dy/steps

    if y1 - y2 >= 0:
        yinc *= -1
  
    x = x1
    y = y1
    
    for _ in range(steps):
        ix, iy = int(x), int(y)
        if not all(canvas[iy][ix]):
            canvas[iy][ix] =[74,168,255,255]

        x = x + xinc
        y = y + yinc

def linear_equation(axis: Literal['x', 'y'], equation: str, _start, _end):
    iaxis = invert_axis(axis)

    for num in range(_start, _end):
        curr = eval(equation.replace(iaxis, str(num)))
        
        if iaxis == 'x':
            draw_point(index(num), index(-curr))

        if iaxis == 'y': 
            draw_point(index(curr), index(-num))

        if num == _end - 1:
            start = eval(equation.replace(iaxis, str(_start)))
            
            if iaxis == 'x':
                draw_line(_start, num, start, curr)

            if iaxis == 'y':
                draw_line(start, curr, _start, num)


# linear_equation('y', '(x + 8) / 2', -3, 3)
# linear_equation('y', '-3 * x', -2, 2)

out = Image.fromarray(canvas)
out.save("./out.png")
