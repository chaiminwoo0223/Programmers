# 최댓값과 최솟값
# 파이썬 변수는 "덮어쓰기"가 가능하다.
# map(타입 변환 함수, 반복 가능한 객체(리스트, 딕셔너리, 집합, 튜플, 문자열))
def solution(s):
    s = list(map(int, s.split())) # iterator --> 리스트
    return str(min(s)) + " " + str(max(s))
