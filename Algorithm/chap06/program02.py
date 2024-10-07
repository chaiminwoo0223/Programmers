# 큰 수 만들기
# stack
def solution(numbers, k):
    result = []
    
    for number in numbers:
        while k > 0 and result and result[-1] < number:
            result.pop()
            k -= 1
        result.append(number)
    
    return ''.join(result)[:len(numbers)-k]
