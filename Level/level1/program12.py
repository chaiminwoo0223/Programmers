# 문자열 내 p와 y의 개수
# string.count(k)
def solution(s):
    s = s.lower()
    return s.count('p') == s.count('y')
