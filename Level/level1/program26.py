# 약수의 개수와 덧셈
def solution(left, right):
    result = 0

    for number in range(left, right+1):
        count = [1 for i in range(1, number+1) if number % i == 0]

        if sum(count) % 2 == 0:
            result += number
        else:
            result -= number

    return result
