# 괄호 회전하기
# 회전
# 스택
def check(a, b):
    if a == '(' and b == ')':
        return True
    elif a == '[' and b == ']':
        return True
    elif a == '{' and b == '}':
        return True
    else:
        return False


def solution(s):
    if len(s) % 2 == 1:
        return 0

    count = len(s)

    for i in range(len(s)):
        stack = []

        for j in range(len(s)):
            if stack and check(stack[-1], s[j]):
                stack.pop()
            else:
                stack.append(s[j])

        if stack:
            count -= 1

        s = s[1:len(s)] + s[0]  # 왼쪽으로 회전

    return count
