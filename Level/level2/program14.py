# N개의 최소공배수
def lcm(elements, number):
    while True:
        count = 0

        for element in elements:
            if number % element != 0:
                number += 1
                break
            else:
                count += 1

        if count == len(elements):
            return number

def solution(arr):
    return lcm(arr, max(arr))
