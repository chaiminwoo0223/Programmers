# 카펫
# 결국 구해야 하는 것은 테두리의 (가로+2), (세로+2) 길이
import math

def solution(brown, yellow):
    total = brown + yellow
    
    for height in range(1, int(math.sqrt(total))+1):
        if total % height == 0:
            width = total // height
            if (width - 2) * (height - 2) == yellow: # 테두리
                return [width, height]
