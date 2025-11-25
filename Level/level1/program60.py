# [1차] 다트 게임
def solution(dartResult):
    start = 0
    end = len(dartResult)
    result = [0]

    while start < end:
        if '10' == dartResult[start:start + 2] and start + 2 < end:
            result, start = calculator(dartResult, start, end, result, 2)

        else:
            result, start = calculator(dartResult, start, end, result, 1)

    return sum(result)

def bonus(x, dart):
    if dart == 'S':
        return x
    elif dart == 'D':
        return x ** 2
    else:
        return x ** 3

def option(num1, num2, dart):
    if dart == '*':
        return num1 * 2, num2 * 2
    else:
        return num1, -num2

def option_calculator(num1, num2, start, dart):
    if dart in ['*', '#']:
        num1, num2 = option(num1, num2, dart)
        return num1, num2, start + 1
    else:
        return num1, num2, start

def calculator(dartResult, start, end, result, plus):
    # 보너스
    num1 = result.pop()
    num2 = bonus(int(dartResult[start:start + plus]), dartResult[start + plus])
    start += (plus + 1)

    # 옵션
    if start < end:
        num1, num2, start = option_calculator(num1, num2, start, dartResult[start])

    result.append(num1)
    result.append(num2)

    return result, start
