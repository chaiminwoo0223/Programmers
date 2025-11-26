# 로또의 최고 순위와 최저 순위
# 조건을 정확히 반영해야 문제가 풀린다.
from collections import Counter

def solution(lottos, win_nums):
    lottos = Counter(lottos)
    win_nums = Counter(win_nums)

    count1 = len(lottos) - len(lottos - win_nums)
    count2 = count1 + (lottos - win_nums)[0]

    return [calculator(count2), calculator(count1)]

def calculator(x):
    if x < 2:
        return 6
    else:
        return 7 - x
