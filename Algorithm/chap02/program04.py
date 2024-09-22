# 프로세스
# any(): 내부의 조건이 하나라도 참이면 True, 모두 거짓이면 False 리턴
from collections import deque

def solution(priorities, location):
    result = 0
    queue = deque([(p, i) for i, p in enumerate(priorities)]) # (우선순위, 인덱스)
    
    while queue:
        current = queue.popleft() # 1.큐에서 대기 중인 프로세스 하나를 꺼냅니다.
        
        if any(current[0] < process[0] for process in queue): # 2.대기 중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면,
            queue.append(current) # 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
        else: # 3.만약 그런 프로세스가 없다면, 
            result += 1 # 방금 꺼낸 프로세스를 실행합니다.
            if current[1] == location: # 4.방금 꺼낸 프로세스가 찾고자 하는 인덱스를 가지고 있다면,
                return result # 해당 프로세스가 몇번째로 실행되는지 리턴합니다.
