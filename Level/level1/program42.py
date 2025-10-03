# 숫자 문자열과 영단어
number_dictionary = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
}

def solution(s):
    for key, value in number_dictionary.items():
        s = s.replace(key, value)

    return int(s)