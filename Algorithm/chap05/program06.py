# 모음 사전
from itertools import product

def solution(word):
    dictionary = [''.join(j) for i in range(1, 6) for j in product(['A', 'E', 'I', 'O', 'U'], repeat = i)] 
    dictionary = sorted(dictionary)
    return dictionary.index(word) + 1
