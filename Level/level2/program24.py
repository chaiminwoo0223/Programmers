# 롤케이크 자르기
# del Counter
from collections import Counter

def solution(topping):
    result = 0
    left = Counter(topping)
    right = {}

    for t in topping:
        if t in right:
            right[t] += 1
        else:
            right[t] = 1

        left[t] -= 1

        if not left[t]:
            del left[t]  # Counter에서 개별 요소 삭제

        if len(left) == len(right):
            result += 1

    return result
