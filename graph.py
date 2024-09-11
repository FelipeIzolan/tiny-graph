from canvas import Canvas
from typing import Literal

I2N = [
    'Inequality',
    'Linear Inequality',
    'Linear Equation'
]


def err(title):
    raise Exception(f"Tiny-Graph - Invalid {title}.")


def format(exp: str, index: int):
    exp = exp.replace(' ', '')

    if index > 1:
        pos = 0

        while pos <= len(exp) - 1:
            char = exp[pos]
            next = exp[pos + 1] if pos + 1 < len(exp) else ''

            if char.isdigit() and (next == '(' or next == 'x' or next == 'y'):
                exp = exp[:pos + 1] + '*' + exp[pos + 1:]
                pos += 1

            pos += 1

    return exp


def get_slope(exp: str, axis: Literal['x', 'y']):
    return -eval(exp.replace(axis, '0')) + eval(exp.replace(axis, '1'))

# -------------------------------------- #


def is_variable(char):
    return char == 'x' or char == 'y'


def is_inequality_operator(ope):
    return ope[0] == '>' or ope[0] == '<'


def is_equality_operator(ope):
    return ope == '='


# -------------------------------------- #

def entry_point(index, ccanvas=None):
    exp = format(input(f'Enter the {I2N[index - 1]}: '), index)
    canvas = ccanvas or Canvas('graph' if index > 1 else 'line')

    match index:
        case 1:
            inequality(exp, canvas)
        case 2:
            linear_inequality(exp, canvas)
        case 3:
            linear_equation(exp, canvas)


def inequality(exp, canvas):
    if not is_variable(exp[0]) or\
       not is_inequality_operator(exp[1]):
        err("Inequality")

    operator = exp[1: (3 if exp[2] == '=' else 2)]
    number = int(exp[1 + len(operator):])
    dir = 1 if operator[0] == '>' else - 1

    canvas.line(number, 11 * dir, 0, 0, False, True, Canvas.GREEN)
    canvas.point(number, 0, False, False, True, Canvas.GREEN)
    canvas.point(1 if dir == -1 else 223, 2, False, True, False, Canvas.GREEN)
    canvas.point(2 if dir == -1 else 222, 0, True, True, False, Canvas.GREEN)
    canvas.point(2 if dir == -1 else 222, 4, True, True, False, Canvas.GREEN)

    if operator == '>' or operator == '<':
        canvas.point(number, 0, True, False, False, Canvas.BLACK)

    canvas.save()


def linear_inequality(exp, canvas):
    if not is_variable(exp[0]) or\
       not is_inequality_operator(exp[1]):
        err("Linear Inequality")

    operator = exp[1: (3 if exp[2] == '=' else 2)]
    inequality = exp[1 + len(operator):]

    if exp[0] == 'y':
        y0 = -eval(inequality.replace('x', '0'))
        slope = get_slope(inequality, 'x')
        result = eval(exp.replace('y', '1').replace('x', '1'))

        canvas.line(
            -10, 10,
            -eval(inequality.replace('x', '-10')),
            -eval(inequality.replace('x', '10')),
            operator == '>' or operator == '<'
        )

        canvas.arrow(
            1 if slope > 0 else -1,
            y0 + 1,
            'bl' if slope > 0 else 'br',
            canvas.GREEN if (slope > 0 and result) or (
                slope < 0 and not result) else canvas.RED
        )

        canvas.arrow(
            -1 if slope > 0 else 1,
            y0 - 1,
            'tl' if slope > 0 else 'tr',
            canvas.GREEN if (slope > 0 and not result) or (
                slope < 0 and result) else canvas.RED
        )

    if exp[0] == 'x':
        x0 = eval(inequality.replace('y', '0'))
        slope = get_slope(inequality, 'y')
        result = eval(exp.replace('y', '1').replace('x', '1'))

        canvas.line(
            eval(inequality.replace('y', '-10')),
            eval(inequality.replace('y', '10')),
            10, -10,
            operator == '>' or operator == '<'
        )

        canvas.arrow(
            x0 + 1,
            1 if slope > 0 else -1,
            'bl' if slope > 0 else 'tr',
            canvas.GREEN if (slope > 0 and not result) or (
                slope < 0 and result) else canvas.RED
        )

        canvas.arrow(
            x0 - 1,
            -1 if slope > 0 else 1,
            'tl' if slope > 0 else 'br',
            canvas.GREEN if (slope > 0 and result) or (
                slope < 0 and not result) else canvas.RED
        )

    if input("Continue? (y/N) ") == 'y':
        entry_point(2, canvas)
    else:
        canvas.save()


def linear_equation(exp, canvas):
    if not is_variable(exp[0]) or\
       not is_equality_operator(exp[1]):
        err("Linear Equation")

    equation = exp[2:]

    if exp[0] == 'y':
        for x in range(-10, 11):
            y = eval(equation.replace('x', str(x)))
            canvas.point(x, -y)

        canvas.line(
            -10, 10,
            -eval(equation.replace('x', '-10')),
            -eval(equation.replace('x', '10'))
        )

    if exp[0] == 'x':
        for y in range(-10, 11):
            x = eval(equation.replace('y', str(y)))
            canvas.point(x, -y)

        canvas.line(
            eval(equation.replace('y', '-10')),
            eval(equation.replace('y', '10')),
            10, -10,
        )

    if input("Continue? (y/N) ") == 'y':
        entry_point(3, canvas)
    else:
        canvas.save()