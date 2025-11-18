# 튜플
# split("k")
# sort(key=len)
def solution(s):
    s = s.replace("{{", "").replace("}}", "").split("},{")
    s.sort(key=len)

    result = []

    for numbers in s:
        for number in map(int, numbers.split(",")):
            if number not in result:
                result.append(number)

    return result