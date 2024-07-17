precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}

def infix_to_postfix(expression):
    stack = []
    output = []
    
    for token in expression:
        if token.isalnum():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while (stack and stack[-1] != '(' and precedence[token] <= precedence[stack[-1]]):
                output.append(stack.pop())
            stack.append(token)
            
    while stack:
        output.append(stack.pop())
    return ''.join(output)

expression = "3+4*2/(1-5)^2"
postfix_expression = infix_to_postfix(expression)
print(f'infix_expression: {expression}')
print(f'postfix_expression: {postfix_expression}')