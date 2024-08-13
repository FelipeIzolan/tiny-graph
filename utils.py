I2N = [
'Inequality (number-line)',
'Linear Inequality (graph)',
'Linear Equation'
]

PROMPT = f'''What do you want to draw?
{''.join(f'{index + 1} - {element}\n' for index, element in enumerate(I2N))}
Enter a number: '''

def format(expr: str, index: int):
    expr = expr.replace(' ', '')
    
    if index > 1:
        pos = 0
        
        while pos <= len(expr) - 1:
            char = expr[pos]
            next = expr[pos + 1] if pos + 1 < len(expr) else ''

            if char.isdigit() and (next == '(' or next == 'x'):
                expr = expr[:pos + 1] + '*' + expr[pos + 1:]
                pos += 1

            pos += 1

    return expr
