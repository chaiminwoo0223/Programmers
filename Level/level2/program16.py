# 예상 대진표
def solution(n, a, b):
    count = 0

    while a != b:
        count += 1
        a, b = (a + 1) // 2, (b + 1) // 2

    return count
