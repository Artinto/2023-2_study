import heapq

def solution(scoville, K):
    heap = []
    count = 0

    # scoville의 원소를 heap에 추가
    for i in range(len(scoville)):
        heapq.heappush(heap, scoville[i])

    # heap의 첫 번째 원소가 K 이상이 될 때까지 반복
    while heap[0] < K:
        # heap에 원소가 2개 미만인 경우 -1 반환
        if len(heap) < 2:
            return -1

        # heap에서 가장 작은 원소와 두 번째로 작은 원소를 추출하고 조건에 맞게 계산
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        new_scov = first + (second * 2)

        # 계산한 값을 heap에 추가
        heapq.heappush(heap, new_scov)
        count += 1  # 섞은 횟수 추가
    answer = count
    
    return answer
