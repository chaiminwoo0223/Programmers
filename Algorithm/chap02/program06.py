# 주식가격
def solution(prices):
    answer = []
    
    for i in range(len(prices)-1):
        maintain = 0
        
        for j in range(i+1, len(prices)):
            maintain += 1
            if prices[i] > prices[j]:
                break
                
        answer.append(maintain)
        
    answer.append(0)
    
    return answer