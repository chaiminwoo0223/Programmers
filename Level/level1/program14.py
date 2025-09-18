# 하샤드 수
def solution(x):
    numbers = [int(i) for i in str(x)]

    return x % sum(numbers) == 0
