from utils import PROMPT, I2N, format, get_slope
from canvas import Canvas

print('''
 __   __                                           __    
|  |_|__.-----.--.--.______.-----.----.---.-.-----|  |--.
|   _|  |     |  |  |______|  _  |   _|  _  |  _  |     |
|____|__|__|__|___  |      |___  |__| |___._|   __|__|__|
              |_____|      |_____|          |__|
''')

index = int(input(f'{PROMPT}'))
if index < 1 or index > 3:
    raise Exception("Index out of range")

def main(canvas = None):
    expr = format(input(f'Enter the {I2N[index - 1]}: '), index)

    match index:
        case 1:
            if (expr[0] != 'x' and expr[0] != 'y') or\
               (expr[1] != '>' and expr[1] != '<'):
                raise Exception("\033[0;31mInequality - Invalid Expression.\033[0m")
         
            operator = expr[1] + ('=' if expr[2] == '=' else '')
            number = int(expr[1 + len(operator):]) 
        
            canvas = Canvas('line')
        
            canvas.line(number, 11 if operator[0] == '>' else -11, 0, 0, False, True, canvas.GREEN)
            canvas.point(number, 0, False, True, False, canvas.GREEN)
            canvas.point(1 if operator[0] == '<' else 223, 2, True, False, False, canvas.GREEN)
            canvas.point(2 if operator[0] == '<' else 222, 0, True, False, True, canvas.GREEN)
            canvas.point(2 if operator[0] == '<' else 222, 4, True, False, True, canvas.GREEN)

            if len(operator) == 1:
                canvas.point(canvas.offsetX(number), canvas.offsetY(), True, False, True, canvas.BLACK)

            canvas.save()

        case 2:
            if (expr[1] != '<' and expr[1] != '>') or\
                expr[0] != 'y':
                raise Exception("\033[0;31mLinear Inequality - Invalid Expression.\033[0m")

            operator = expr[1] + ('=' if expr[2] == '=' else '')
            inequality = expr[1 + len(operator):]
            
            expr = 'y' + operator + ('=' if operator == '<' or operator == '>' else '') + inequality

            result = eval(expr.replace('y', '0').replace('x', '0'))
            canvas = Canvas("graph")

            canvas.line(
                -10, 10,
                -eval(inequality.replace('x', '-10')),
                -eval(inequality.replace('x', '10')),
                operator == '>' or operator == '<'
            )
            
            y0 = -eval(inequality.replace('x', '0')) 
            slope = get_slope(inequality)
            
            canvas.arrow(
                1 if slope > 0 else -1, 
                y0 + 1, 
                'bottom-left' if slope > 0 else 'bottom-right', 
                canvas.GREEN if (result and operator[0] == '<') or (not result and operator[0] == '>') else canvas.RED
            )

            canvas.arrow(
                -1 if slope > 0 else 1,
                y0 - 1,
                'top-left' if slope > 0 else 'top-right',
                canvas.GREEN if (result and operator[0] == '>') or (not result and operator[0] == '<') else canvas.RED
            )

            canvas.save()

        case 3:
            if expr[0] != 'y' or expr[1] != '=':
                raise Exception("\033[0;31mLinear Equation - Invalid Expression.\033[0m")

            canvas = canvas if canvas else Canvas('graph')
            equation = expr[2:]

            for x in range(-10, 10):
                y = eval(equation.replace('x', str(x)))            
                canvas.point(x, -y)

            canvas.line(
                -10, 10,
                -eval(equation.replace('x', '-10')),
                -eval(equation.replace('x', '10'))
            )

            if input("Continue? (y/N) ") == 'y':
                main(canvas)
            else:
                canvas.save()

main()
