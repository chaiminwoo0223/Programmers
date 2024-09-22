# 올바른 괄호
def solution(s):
    stack = [] # 스택: 후입선출
    
    for char in s:
        if char == '(':
            stack.append('(')
        else:
            if '(' in stack:
                stack.pop()
            else:
                return False
    
    if len(stack) == 0:
        return True
    else:
        return False
