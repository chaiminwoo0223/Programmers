# k진수에서 소수 개수 구하기
from math import sqrt

def solution(n, k):
    result = 0

    convert_numbers = convert(n, k)

    for convert_number in convert_numbers.split('0'):
        if convert_number and prime(int(convert_number)):
            result += 1

    return result

def convert(n, k):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)  # n을 k로 나눈 몫과 나머지
        rev_base += str(mod)

    return rev_base[::-1]

def prime(n):
    if n < 2:
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True
