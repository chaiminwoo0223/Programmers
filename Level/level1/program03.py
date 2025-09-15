# 자릿수 더하기
def solution(n):
    number = str(n)
    count = 0

    for i in range(len(number)):
        count += int(number[i])

    return count