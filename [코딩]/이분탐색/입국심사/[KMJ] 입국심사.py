def solution(n, times):
    # start : 입국심사가 가장 적게 걸리는 심사대에서 심사를 받는 경우 -> 모든 심사대가 min(times)인 경우
    # end : 입국심사가 가장 오래 걸리는 심사대에서만 심사를 받는 경우
    
    # 이분탐색을 위해 처음 start, end 지정
    low = min(times) * n / len(times)
    high = max(times) * n

    while low <= high: # 정답이 하나로 좁혀지면 while문 통과
        mid = (low + high) // 2
        people = 0
        
        for i in times:
            people += mid // i
            
            if people >= n: # people >= n : 시간이 충분, low와 mid 사이로 범위 좁히기 (우선 for문 탈출)
                break
            # for문을 다 돌았는데도 n에 도달하지 못함 : 시간이 부족, mid와 high 사이로 범위 좁히기
                
        if people < n: # 시간이 부족, mid와 high 사이로 범위 좁히기
            low = mid + 1
        
        else: # people >= n : 시간이 충분, low와 mid 사이로 범위 좁히기
            answer = mid
            high = mid - 1
        
    return answer
