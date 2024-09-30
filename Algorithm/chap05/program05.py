# 피로도
# permutations(): 리스트 -> 튜플 형태의 모든 순열
from itertools import permutations

def solution(k, dungeons):
    max_count = 0

    for permutation in permutations(dungeons):
        cost = k
        count = 0
        for dungeon in permutation:
            if cost >= dungeon[0]:
                cost -= dungeon[1]
                count += 1
        max_count = max(max_count, count)
    
    return max_count
