import heapq

def solution(jobs):
    time, now, i = 0, 0, 0
    start = -1
    heap = []
    
    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        [heapq.heappush(heap, [j[1], j[0]]) for j in jobs if start < j[0] <= now] # 소요시간이 짧은 순으로 저장하기 위해 [j[1],j[0]] 순서로 저장

        if len(heap) > 0: # 처리할 작업이 있는 경우
            cur = heapq.heappop(heap)
            start = now
            now += cur[0] # 소요시간 기준으로 저장하여 현재시간(작업전) + 소요시간 = 현재시간(작업후)
            time += now - cur[1] # 작업 요청시간부터 종료시간까지의 시간 계산
            i += 1
        else: # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1
                
    answer = time // len(jobs)
    return answer
