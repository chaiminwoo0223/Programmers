# 최솟값 만들기
# map(지정 함수, 반복 가능한 객체1, 반복 가능한 객체2, ...)
def solution(A,B):
    return sum(map(lambda a, b : a * b, sorted(A), sorted(B, reverse=True)))
