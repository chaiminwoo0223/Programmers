# 시저 암호
from string import ascii_lowercase, ascii_uppercase

upper_alpha_list = list(ascii_uppercase)
lower_alpha_list = list(ascii_lowercase)


def solution(s, n):
    result = ""

    for c in s:
        if c.isupper():  # 대문자
            idx = (upper_alpha_list.index(c) + n) % 26
            result += upper_alpha_list[idx]
        elif c.islower():  # 소문자
            idx = (lower_alpha_list.index(c) + n) % 26
            result += lower_alpha_list[idx]
        else:
            result += " "

    return result
