# 짝지어 제거하기
# 스택
# 시간복잡도
def solution(s):
    stack = []
    
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
            
    if stack:
        return 0
    else:
        return 1
