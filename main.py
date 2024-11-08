from canvas import Canvas
from graph import inequality, linear_equation, linear_inequality, quadratic_equation
from utils import format2eval, is_operator, is_variable

print('''
 __   __                                           __
|  |_|__.-----.--.--.______.-----.----.---.-.-----|  |--.
|   _|  |     |  |  |______|  _  |   _|  _  |  _  |     |
|____|__|__|__|___  |      |___  |__| |___._|   __|__|__|
              |_____|      |_____|          |__|

1 - Inequality
2 - Linear Inequality
3 - Linear Equation
4 - Quadratic Equation
''')

index = int(input("Select a option: "))
if index < 1 or index > 4:
    raise Exception("Index out of range")


I2N = [
    'Inequality',
    'Linear Inequality',
    'Linear Equation',
]


def main(c=None):
    canvas = c or Canvas('graph' if index > 1 else 'line')

    match index:
        case 1 | 2 | 3:
            expression = format2eval(input(f'Enter the {I2N[index - 1]}: '))

            if not is_variable(expression[0]) or not is_operator(expression[1]):
                raise Exception("Tiny-Graph - Invalid Expression.")

            if index == 1:
                inequality(canvas, expression)
            if index == 2:
                linear_inequality(canvas, expression)
            if index == 3:
                linear_equation(canvas, expression)
        case 4:
            a = int(input('a: '))
            b = int(input('b: '))
            c = int(input('c: '))
            quadratic_equation(canvas, a, b, c)

    if index > 1 and input("Continue? (y/N) "):
        main(canvas)
    else:
        canvas.save()


main()
