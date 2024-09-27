# 다음 큰 숫자
# 문자열.count('s'): 문자열 안에서 특정 문자 s의 개수를 리턴한다.
def solution(number):
    next_number = number

    while True:
        next_number = next_number + 1
        print(next_number, bin(next_number))
        if str(bin(next_number)[2:]).count('1') == str(bin(number)[2:]).count('1'):
            return next_number
