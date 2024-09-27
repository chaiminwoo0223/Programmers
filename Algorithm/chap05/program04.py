import math

def solution(brown, yellow):
    quadrangle = brown + yellow
    
    if yellow % math.sqrt(yellow) == 0: # 정사각형
        return [int(math.sqrt(yellow)) + 2, int(math.sqrt(yellow)) + 2]
    
    for i in range(1, brown+1): # 그 외
        for j in range(1, i+1):
            if (i * j) == quadrangle:
                return [i, j]

print(solution(3004, 2996))