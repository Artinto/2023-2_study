import heapq 

def solution(operations):
    max_heap = []  # 최댓값을 저장할 최대 힙
    min_heap = []  # 최솟값을 저장할 최소 힙

    for op in operations: 
        if op.startswith("I"):  # 연산이 "I"로 시작하면
            num = int(op.split()[1])  # 숫자를 추출
            heapq.heappush(max_heap, -num)  # 최대 힙에 -num 삽입 (최댓값을 뽑기 위해)
            heapq.heappush(min_heap, num)  # 최소 힙에 num 삽입
        elif op == "D 1":  # 연산이 "D 1"인 경우 (최댓값 삭제)
            if max_heap:  # 최대 힙이 비어있지 않으면
                max_num = -heapq.heappop(max_heap)  # 최대 힙에서 가장 큰 값을 뽑아 max_num에 저장
                min_heap.remove(max_num)  # 최소 힙에서 max_num 삭제
        elif op == "D -1":  # 연산이 "D -1"인 경우 (최솟값 삭제)
            if min_heap:  # 최소 힙이 비어있지 않으면
                min_num = heapq.heappop(min_heap)  # 최소 힙에서 가장 작은 값을 뽑아 min_num에 저장
                max_heap.remove(-min_num)  # 최대 힙에서 -min_num 삭제

    if not max_heap or not min_heap:  # 최대 힙과 최소 힙 중 하나라도 비어있는 경우
        return [0, 0]
    else: 
        return [-max_heap[0], min_heap[0]]  # [최댓값, 최솟값] 반환
