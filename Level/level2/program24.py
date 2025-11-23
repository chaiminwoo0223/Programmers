# 롤케이크 자르기
from collections import Counter

def solution(topping):
    result = 0
    left = {}
    right = Counter(topping)

    for t in topping:
        if t in left:
            left[t] += 1
        else:
            left[t] = 1

        right[t] -= 1

        if not right[t]:
            del right[t]

        if len(left.keys()) == len(right.keys()):  # Counter에서 개별 요소 삭제
            result += 1

    return result
