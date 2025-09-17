# 정수 내림차순으로 배치하기
def solution(n):
    numbers = sorted(str(n), reverse=True)
    result = ''.join(numbers)
    return int(result)
