# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    result = [element for element in arr if element % divisor == 0]

    return sorted(result) if result else [-1]
