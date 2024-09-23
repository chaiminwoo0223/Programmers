# 이진 변환 반복하기
def solution(s):
    count = [0, 0]
    
    while len(s) != 1:
        count[1] += s.count("0") # 제거할 0의 개수
        s = s.replace("0", "") # s의 모든 0을 제거합니다.
        s = bin(len(s))[2:] # len(s)를 2진법으로 표현한 문자열로 바꿉니다.
        count[0] += 1 # 이진 변환 횟수
        print(s)
    
    return count
