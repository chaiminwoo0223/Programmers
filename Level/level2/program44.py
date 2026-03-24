# 호텔 대실
# 시간, 분 -> 분
def solution(book_time):
    book_times = sorted([changeTime(time[0]), changeTime(time[1]) + 10] for time in book_time)
    rooms = []

    for book_time in book_times:
        if not rooms:
            rooms.append(book_time)
            continue

        for i, room in enumerate(rooms):
            if book_time[0] >= room[-1]:
                rooms[i] = room + book_time  # 핵심
                break
        else:
            rooms.append(book_time)

    return len(rooms)


def changeTime(time):
    return int(time[:2]) * 60 + int(time[3:])
