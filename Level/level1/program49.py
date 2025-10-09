# 2016년
def solution(a, b):
    days = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    calendars = [31, 29, 31, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    n = sum(calendars[i] for i in range(a - 1)) + b

    return days[n % 7]
