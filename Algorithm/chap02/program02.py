# 기능개발
def solution(progresses, speeds):
    distribution = []
    while progresses:
        count = 0
        while progresses[0] < 100:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
        
        while progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            if not progresses: break
        distribution.append(count)
        
    return distribution
    
