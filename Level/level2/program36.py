# 주차 요금 계산
# fees: 기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)
# records: 시각 차량번호 내역(시각을 기준으로 오름차순 정렬)
from math import ceil

def solution(fees, records):
    total = {}
    dictionary = {}
    result = []

    for record in records:
        time, number, r = record.split(" ")

        if r == 'IN':
            dictionary[number] = timeCalculator(time)
        else:
            totalCalculator(total, dictionary, number, time)
            del dictionary[number]

    for key in dictionary.keys():
        totalCalculator(total, dictionary, key, "23:59")

    for key in sorted(total):
        if total[key] > fees[0]:
            result.append(fees[1] + ceil((total[key] - fees[0]) / fees[2]) * fees[3])
        else:
            result.append(fees[1])

    return result

def totalCalculator(total, dictionary, number, time):
    dictionary[number] = timeCalculator(time) - dictionary[number]

    if number not in total.keys():
        total[number] = dictionary[number]
    else:
        total[number] += dictionary[number]


def timeCalculator(time):
    hour, minute = time.split(':')
    return (int(hour) * 60) + int(minute)
