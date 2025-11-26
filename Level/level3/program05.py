# 이중우선순위큐
# 순서 중요: 우선순위 큐가 비어있으므로 최댓값 삭제 연산이 무시됩니다.
import heapq

def solution(operations):
    min_heap = []
    max_heap = []

    for operation in operations:
        if operation[0] == 'I':
            heapq.heappush(min_heap, int(operation[2:]))
            heapq.heappush(max_heap, -int(operation[2:]))

        if min_heap and max_heap and operation[0] == 'D':
            if int(operation[2:]) == -1:  # 최솟값 삭제
                max_heap = delete(min_heap, max_heap)
            else:  # 최댓값 삭제
                min_heap = delete(max_heap, min_heap)

    if min_heap:
        return [max(min_heap), min(min_heap)]
    else:
        return [0, 0]

def delete(heap1, heap2):
    x = -heapq.heappop(heap1)

    if x in heap2:
        heap2.remove(x)
        heapq.heapify(heap2)

    return heap2
