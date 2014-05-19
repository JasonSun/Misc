nCase = input()
for i in range(nCase):
    expr = raw_input()
    operators = []
    operands = []
    for index in range(len(expr)):
        if expr[index] == ')':
            tmpExpr = operators.pop() + operands.pop() + operands.pop()
            operands.pop()
            operands.append(tmpExpr)

        elif expr[index] == '+' or expr[index] == '-'\
        or expr[index] == '*' or expr[index] == '/' or expr[index] == '^':
            operators.append(expr[index])
        else:
            operands.append(expr[index])
    RPN = operands.pop()
    print RPN[-1::-1]
