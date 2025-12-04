# 숫자 짝꿍
# keys, elements를 이용해 범위를 줄여보자.
from collections import Counter

def solution(X, Y):
    z = Counter(X) & Counter(Y)

    if len(z.keys()) == 1 and "0" in z.keys():
        return "0"
    elif len(z.keys()) != 0:
        return "".join(sorted(z.elements(), reverse=True))
    else:
        return "-1"
