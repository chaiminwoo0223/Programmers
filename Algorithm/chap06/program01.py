# 체육복
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    for i in lost[:]: # 얕은 복사본 순회(순회 영향 없음)
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
    for i in lost[:]: # 얕은 복사본 순회(순회 영향 없음)
        if (i-1) in reserve:
            reserve.remove(i-1)
            lost.remove(i)
        elif (i+1) in reserve:
            reserve.remove(i+1)
            lost.remove(i)
            
    answer = n - len(lost)
    return answer
