# 숫자의 표현
def solution(number):
    count = 0
        
    # 연속한 자연수들의 합
    for i in range(number):
        total = 0
        while total < number:
            i += 1
            total += i
        if total == number:
            count += 1
    
    return count
