from canvas import Canvas
from utils import bhaskara, frange, get_color, get_slope, quadratic


def inequality(canvas: Canvas, expression: str):
    operator = expression[1: (3 if expression[2] == '=' else 2)]
    number = int(expression[1 + len(operator):])
    dir = 1 if operator[0] == '>' else - 1

    canvas.line(number, 11 * dir, 0, 0, False, True, Canvas.GREEN)
    canvas.point(number, 0, False, True, False, True, Canvas.GREEN)

    canvas.point(1 if dir == -1 else 223, 2, False,
                 False, True, True, Canvas.GREEN)
    canvas.point(2 if dir == -1 else 222, 0, True,
                 False, True, True, Canvas.GREEN)
    canvas.point(2 if dir == -1 else 222, 4, True,
                 False, True, True, Canvas.GREEN)

    if operator == '>' or operator == '<':
        canvas.point(number, 0, True, False, False, True, Canvas.BLACK)


def linear_inequality(canvas: Canvas, expression: str):
    axis = expression[0]
    iaxis = 'x' if axis == 'y' else 'y'

    operator = expression[1:(3 if expression[2] == '=' else 2)]
    inequality = expression[1+len(operator):]

    slope = get_slope(inequality, iaxis)
    p0 = eval(inequality.replace(iaxis, '0')) * (-1 if axis == 'y' else 1)

    top, bottom = get_color(expression, slope)

    canvas.arrow(
        p0 - 1 if axis == 'x' else -1 if slope > 0 else 1,
        p0 - 1 if axis == 'y' else -1 if slope > 0 else 1,
        'tl' if slope > 0 else 'tr',
        top
    )

    canvas.arrow(
        p0 + 1 if axis == 'x' else 1 if slope > 0 else -1,
        p0 + 1 if axis == 'y' else 1 if slope > 0 else -1,
        'bl' if slope > 0 else 'br',
        bottom
    )

    canvas.line(
        eval(inequality.replace('y', '-10')) if axis == 'x' else -10,
        eval(inequality.replace('y', '10')) if axis == 'x' else 10,
        -eval(inequality.replace('x', '-10')) if axis == 'y' else 10,
        -eval(inequality.replace('x', '10')) if axis == 'y' else -10,
        operator == '>' or operator == '<'
    )


def linear_equation(canvas: Canvas, expression: str):
    axis = expression[0]
    iaxis = 'x' if axis == 'y' else 'y'

    equation = expression[2:]

    for a1 in range(-10, 11):
        a2 = eval(equation.replace(iaxis, str(a1)))
        canvas.point(
            a2 if axis == 'x' else a1,
            -(a2 if axis == 'y' else a1)
        )

    canvas.line(
        eval(equation.replace('y', '-10')) if axis == 'x' else -10,
        eval(equation.replace('y', '10')) if axis == 'x' else 10,
        -eval(equation.replace('x', '-10')) if axis == 'y' else 10,
        -eval(equation.replace('x', '10')) if axis == 'y' else -10,
    )


def quadratic_equation(canvas: Canvas, a: int, b: int, c: int):
    for x in frange(-8.0, 8.0, 0.01):  # <- line
        y = -quadratic(a, b, c, x)
        canvas.point(x, y, True, False, False, False, canvas.BLUE)

    x_sym = -b / (2 * a)
    canvas.point(
        x_sym,
        -quadratic(a, b, c, x_sym)
    )

    x1, x2 = bhaskara(a, b, c)
    if x1 and x2:
        canvas.point(x1, 0)
        canvas.point(x2, 0)
