# K번째수
def solution(array, commands):
    answer = []
    for command in commands: 
        i, j, k = command # 핵심
        answer.append(sorted(array[i-1:j])[k-1])
    
    return answer
