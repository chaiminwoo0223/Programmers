# 대충 만든 자판
# break
# 키를 최소 몇 번 눌러야 하는가?
from collections import Counter

def solution(keymap, targets):
    result = [0] * len(targets)
    counter = Counter()

    for key in keymap:
        for i, k in enumerate(key, start=1):
            if k not in counter or (k in counter and i < counter[k]):
                counter[k] = i

    for j, target in enumerate(targets):
        for t in target:
            if t in counter:
                result[j] += counter[t]
            else:
                result[j] = -1
                break

    return result