from math import sqrt
from typing import Literal

from canvas import Canvas
import re


def frange(start: float, stop: float, step: float):
    c = start

    while c < stop:
        yield c
        c += step


# --- #


def format2eval(expression: str):
    expression = expression.replace(' ', '')
    pos = 0

    while pos <= len(expression) - 1:
        char = expression[pos]
        next = expression[pos + 1] if pos + 1 < len(expression) else ''

        if char.isdigit() and (next == '(' or next == 'x' or next == 'y'):
            expression = expression[:pos + 1] + '*' + expression[pos + 1:]
            pos += 1

        pos += 1

    return expression


# --- #


def quadratic(a, b, c, x):
    return a * x * x + b * x + c


def bhaskara(a, b, c):
    delta = b * b - 4 * a * c

    if delta <= 0:
        return 0, 0

    d = 2 * a
    s = sqrt(delta)

    return (-b + s) / d, (-b - s) / d


# --- #


def get_slope(expression: str, axis: Literal['x', 'y']):
    _1 = eval(expression.replace(axis, '1'))
    _2 = eval(expression.replace(axis, '2'))
    return _2 - _1


def get_color(expression: str, axis, iaxis):
    equation = re.sub(r'>=|<=|>|<', '=', expression)[2:]
    a0 = eval(equation.replace(iaxis, '0'))
    result = eval(expression.replace(axis, str(a0)).replace(iaxis, '0'))

    if axis == 'y':
        return (
            Canvas.GREEN if not result else Canvas.RED,
            Canvas.GREEN if result else Canvas.RED
        )
    else:  # 'x'
        return (
            Canvas.GREEN if result else Canvas.RED,
            Canvas.GREEN if not result else Canvas.RED
        )


def is_variable(char):
    return char == 'x' or char == 'y'


def is_operator(operator):
    return operator == '=' or operator[0] == '>' or operator[0] == '<'
