from utils import PROMPT, I2N, format
from canvas import Canvas

print('''
 __   __                                           __    
|  |_|__.-----.--.--.______.-----.----.---.-.-----|  |--.
|   _|  |     |  |  |______|  _  |   _|  _  |  _  |     |
|____|__|__|__|___  |      |___  |__| |___._|   __|__|__|
              |_____|      |_____|          |__|
''')

index = int(input(f'{PROMPT}'))
if index <= 0 or index >= 4:
    raise Exception("Index out of range")

def main(canvas = None):
    expr = format(input(f'Enter the {I2N[index - 1]}: '), index)

    match index:
        case 1:
            if (expr[0] != 'x' and expr[0] != 'y') or\
               (expr[1] != '>' and expr[1] != '<'):
                raise Exception("\033[0;31mInequality - Invalid Expression.\033[0m")
         
            inequality = expr[1] + ('=' if expr[2] == '=' else '')
            inequality_len = len(inequality)
            start = int(expr[1 + inequality_len:]) 
        
            canvas = Canvas('line')
        
            canvas.line(start, 11 if inequality[0] == '>' else -11, 0, 0, True, Canvas.RED)
            canvas.pointq(start, 0)
            canvas.pointr(1 if inequality[0] == '<' else 223, 2)
            canvas.pointro(2 if inequality[0] == '<' else 222, 0)
            canvas.pointro(2 if inequality[0] == '<' else 222, 4)

            if inequality_len == 1:
                canvas.pointro(canvas.offsetX(start), canvas.offsetY(), Canvas.BLACK)

            canvas.save()

        case 2:
            print('Under Development')

        case 3:
            if expr[0] != 'y' or expr[1] != '=':
                raise Exception("\033[0;31mLinear Equation - Invalid Expression.\033[0m")

            canvas = canvas if canvas else Canvas('graph')
            equation = expr[2:]

            for x in range(-10, 10):
                y = eval(equation.replace('x', str(x)))            
                canvas.point(x, -y)

            canvas.line(
                -10,
                10,
                -eval(equation.replace('x', '-10')),
                -eval(equation.replace('x', '10'))
            )
            
            if input("Would you like to graph another linear equation? (y/N) ") == 'y':
                main(canvas)
            else:
                canvas.save()

main()
