# 서울에서 김서방 찾기
def solution(seoul):
    for i, element in enumerate(seoul):
        if element == "Kim":
            return f'김서방은 {i}에 있다'
