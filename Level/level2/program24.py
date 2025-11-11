# 롤케이크 자르기
# Counter
# del
from collections import Counter

def solution(toppings):
    answer = 0
    left = Counter(toppings)
    right = {}

    for topping in toppings:
        if topping in right:
            right[topping] += 1
        else:
            right[topping] = 1

        left[topping] -= 1

        if not left[topping]:
            del left[topping]  # Counter에서 개별 요소 삭제

        if len(left) == len(right):
            answer += 1

    return answer
