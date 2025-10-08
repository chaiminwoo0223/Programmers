# 할인 행사
# zip
from collections import Counter

def solution(want, number, discount):
    count = 0
    want_number = dict(zip(want, number))

    for i in range(len(discount) - 10 + 1):
        if want_number == Counter(discount[i:i + 10]):
            count += 1

    return count
