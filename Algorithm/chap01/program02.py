# 완주하지 못한 선수
from collections import Counter

def solution(participant, completion):
    result = Counter(participant) - Counter(completion)
    return list(result)[-1]
