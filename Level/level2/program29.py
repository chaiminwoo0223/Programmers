# [3차] n진수 게임
def solution(n, t, m, p):
    result = ""
    numbers = ""
    x = 0

    while True:
        numbers += convert(x, n)

        if 1 <= p < len(numbers):
            result += numbers[p - 1]
            p += m

        if len(result) == t:
            return result

        x += 1

def convert(x, n):
    rev_base = ""

    if x == 0:
        return "0"

    while x > 0:
        x, mod = divmod(x, n)

        if mod == 10:
            rev_base += "A"
        elif mod == 11:
            rev_base += "B"
        elif mod == 12:
            rev_base += "C"
        elif mod == 13:
            rev_base += "D"
        elif mod == 14:
            rev_base += "E"
        elif mod == 15:
            rev_base += "F"
        else:
            rev_base += str(mod)

    return rev_base[::-1]
