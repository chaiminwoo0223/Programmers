# 베스트앨범
# zip -> (a, b)
from collections import Counter

def solution(genres, plays):
    result = []
    counter1 = Counter()
    counter2 = Counter()

    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in counter1.keys():
            counter1[genre] = [(i, play)]
        else:
            counter1[genre].append((i, play))  # 핵심

        if genre not in counter2.keys():
            counter2[genre] = play
        else:
            counter2[genre] += play

    for genre, _ in sorted(counter2.items(), key=lambda x: -x[1]):
        for i, play in sorted(counter1[genre], key=lambda x: (-x[1], x[0]))[:2]:
              result.append(i)

    return result