# [1차] 뉴스 클러스터링
# &: 교집합, |: 합집합
# Counter &와 |는 정확히 다중집합 연산을 위해 설계
from collections import Counter


def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    set1 = [str1[i:i + 2] for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()]
    set2 = [str2[j:j + 2] for j in range(len(str2) - 1) if str2[j:j + 2].isalpha()]

    counter1 = Counter(set1)
    counter2 = Counter(set2)

    inter = list((counter1 & counter2).elements())  # 교집합
    union = list((counter1 | counter2).elements())  # 합집합

    if len(inter) == 0 and len(union) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)
