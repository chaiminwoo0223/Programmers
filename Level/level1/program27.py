# 부족한 금액 계산하기
def solution(price, money, count):
    return - min(0, money - sum(price * (i+1) for i in range(count)))
