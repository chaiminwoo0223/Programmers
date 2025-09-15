# 자연수 뒤집어 배열로 만들기
# reversed 함수
def solution(n):
    numbers = list(map(int, reversed(str(n))))

    return numbers