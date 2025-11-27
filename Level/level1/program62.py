# 햄버거 만들기
# 아래서부터, 빵 – 야채 – 고기 - 빵, 1 - 2 - 3 - 1
# 빵: 1, 야채: 2, 고기: 3
# 스택
def solution(ingredients):
    result = 0
    stack = []

    for ingredient in ingredients:
        stack.append(ingredient)

        if stack[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                stack.pop()

            result += 1

    return result