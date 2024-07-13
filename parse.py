from typing import Literal, Tuple

type TokenType = Tuple[Literal['number', 'variable', 'operator', 'parentheses', 'equal'], str]

def parse(equation: str) -> list[TokenType]:
    operators = ['+','-','*','/']

    tokens = []
    token = ''

    def prevType():
        return tokens[len(tokens) - 1][0]

    def anyNoDigit(char):
        return char in operators or char == 'x' or char == 'y' or char == '(' or char == ')' or char == '='

    for index, char in enumerate(equation):
        if char == ' ':
            continue

        if char.isdigit() or char == '.':
            token += char

        if token and (anyNoDigit(char) or index == len(equation) - 1):
            tokens.append(('number', token))
            token = '' 

        if char == '=':
            tokens.append(('equal', char))

        if char == 'x' or char == 'y':
            if prevType() == 'number':
                tokens.append(('operator', '*'))

            tokens.append(('variable', char))

        if char == '(' or char == ')':
            if char == '(' and prevType() == 'number':
                tokens.append(('operator', '*'))

            tokens.append(('parentheses', char))

        if char in operators:
            tokens.append(('operator', char)) 

    return tokens
