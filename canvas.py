from typing import Literal
from PIL import Image
import numpy as np

class Canvas:
    RED = [255, 74, 121, 255]
    GREEN = [43, 255, 128, 255]
    BLUE = [74, 168, 255, 255]
    BLACK = [33, 33, 33, 255]
    YELLOW = [255, 210, 140, 255]

    def __init__(self, base: Literal['graph', 'line']) -> None:
        self.__canvas = np.asarray(Image.open(f'./{base}.png')).copy()
        self.__canvas.setflags(write = True)
        self.base = base

    def __getitem__(self, item):
        return self.__canvas[item]
    
    def valid(self, x, y, offset = True):
        if offset: x, y = self.offsetX(x), self.offsetY(y)
        if self.base == "line": return x >= 0 and x <= 224
        if self.base == "graph": return x >= 0 and x <= 224 and y >= 0 and y <= 224
        return False
    
    def offsetX(self, x: int = 0):
        if self.base == 'line': return 112 + x * 10
        if self.base == 'graph': return 112 + x * 10
        return x 
    
    def offsetY(self, y: int = 0):
        if self.base == 'line': return 2
        if self.base == 'graph': return 112 + y * 10
        return y

    def point(self, x: int, y: int, raw = False, quad = False, one = False, color = RED):
        if not raw and self.valid(x,y):
            x, y = self.offsetX(x), self.offsetY(y)

        self.__canvas[y][x] = color

        if one: 
            return

        if quad:
            for i in range (-1, 2):
                for j in range(-1, 2):
                    self.__canvas[y+i][x+j] = color
        else:
            for n in range (-1, 2):
                self.__canvas[y+n][x] = color
                self.__canvas[y][x+n] = color

    def line(self, x1: int, x2: int, y1: int, y2: int, dotted = False, overlap = False, color = BLUE):
        x1, x2 = self.offsetX(x1), self.offsetX(x2)
        y1, y2 = self.offsetY(y1), self.offsetY(y2)
        
        dx = abs(x1 - x2)
        dy = abs(y1 - y2) 
        steps = max(dx, dy) 

        xinc = dx/steps
        yinc = dy/steps

        if x1 - x2 >= 0:
            xinc *= -1

        if y1 - y2 >= 0:
            yinc *= -1

        x = x1
        y = y1

        for i in range(steps):
            ix, iy = int(x), int(y)

            if self.valid(ix, iy, False) and\
               (not all(self.__canvas[iy][ix]) or overlap) and\
               (not dotted or (dotted and i % 2 == 0)):
                self.__canvas[iy][ix] = color

            x = x + xinc
            y = y + yinc

    def arrow(self, x: int, y: int, dir: Literal['top-left', 'top-right', 'bottom-left', 'bottom-right'], color = RED):
        x, y = self.offsetX(x), self.offsetY(y)
        self.point(x, y, True, True, False, color)
        self.point(x, y + (1 if dir.startswith('top') else -1), True, False, True, [0, 0, 0, 0])

        if dir.startswith("top"):
            self.point(x + (1 if dir.endswith('left') else -1), y, True, False, True, [0, 0, 0, 0])

        if dir.startswith("bottom"):
            self.point(x + (1 if dir.endswith('right') else -1), y, True, False, True, [0, 0, 0, 0])

    def save(self, path = './out.png'):
        if not path.endswith('.png'):
            raise Exception('\033[0;31mCanvas - Invalid path.\033[0m')

        out = Image.fromarray(self.__canvas)
        out.save(path)
