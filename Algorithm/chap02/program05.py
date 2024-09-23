# 다리를 지나는 트럭
from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque([0] * bridge_length)
    bridge_weight = 0
    answer = 0
    
    for truck_weight in truck_weights:
        while True:
            bridge_weight -= queue.popleft()
            
            if (bridge_weight + truck_weight) <= weight:
                bridge_weight += truck_weight
                queue.append(truck_weight)
                answer += 1
                break
            else:
                queue.append(0)
                answer += 1
                
    answer += bridge_length # 마지막 트럭이 완전히 다리를 건너는 추가 시간
    
    return answer
