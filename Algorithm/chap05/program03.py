# 소수 찾기
from itertools import permutations

# 소수 판별 함수(기본) <---> 소수 판별 함수(루트, 대칭성)
def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    primes = set()
    
    for i in range(1, len(numbers)+1):
        for j in set(permutations(numbers, i)):
            number = int("".join(j))
            if is_prime(number):
                primes.add(number)
                
    return len(primes)
