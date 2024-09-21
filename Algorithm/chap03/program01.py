# 더 맵게
import heapq # 최소 힙

def solution(scoville, K):
    heapq.heapify(scoville) # 리스트를 힙으로 변환
        
    # 섞은 횟수
    count = 0
    while len(scoville) > 1 and scoville[0] < K:
        first_score = heapq.heappop(scoville)  # 가장 작은 스코빌 지수 꺼내기
        second_score = heapq.heappop(scoville)  # 두 번째로 작은 스코빌 지수 꺼내기
        new_score = first_score + (second_score * 2)  # 새로운 스코빌 지수 계산하기
        heapq.heappush(scoville, new_score)  # 새로운 스코빌 지수 추가하기
        count += 1
    
    # K 이상의 스코빌 지수가 없으면, -1
    if scoville[0] < K:
        return -1
    
    return count
