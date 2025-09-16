# 나머지가 1이 되는 수 찾기
def solution(n):
    x = 1

    while n % x != 1:
        x += 1

    return x
