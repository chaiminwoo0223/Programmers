# [1차] 비밀지도
def binary_number(x, num):
    result = ""

    for _ in range(x):
        if num % 2 == 0:
            result += " "
        else:
            result += "#"

        num //= 2

    return result


def solution(n, arr1, arr2):
    password1 = [binary_number(n, arr) for arr in arr1]
    password2 = [binary_number(n, arr) for arr in arr2]
    password = []

    for i in range(n):
        result = ""

        for j in range(n):
            if password1[i][j] == "#" or password2[i][j] == "#":
                result += "#"
            else:
                result += " "

        password.append(result[::-1])

    return password
