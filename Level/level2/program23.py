# 튜플
# split("k")
# sort(key=len)
def solution(s):
    result = []

    s = s[2:-2].split("},{")
    s.sort(key=len)

    for numbers in s:
        numbers = numbers.split(",")

        for number in numbers:
            if int(number) not in result:
                result.append(int(number))

    return result
