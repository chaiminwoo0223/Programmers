# 유연근무제
# 모든 시각은 시에 100을 곱하고, 분을 더한 정수로 표현됩니다.
# 단, 토요일, 일요일의 출근 시각은 이벤트에 영향을 끼치지 않습니다. (Pass)
def solution(schedules, timelogs, startday):
    result = 0

    for i, schedule in enumerate(schedules):
        s = startday
        t = True

        for timelog in timelogs[i]:
            if s == 6:
                s = 7
                continue
            elif s == 7:
                s = 1
                continue
            else:
                if calculator(schedule) >= timelog:
                    s += 1
                else:
                    t = False
                    break

        if t:
            result += 1

    return result

def calculator(schedule):
    schedule += 10

    if str(schedule)[-2:-1] == '6':
        print("->", schedule + 40)
        return schedule + 40

    return schedule
