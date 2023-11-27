def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort() # 바위 사이의 거리를 구하기 위해 오름차순으로 정렬
    
    # start : 바위 사이의 최소 distance = 1
    # end : 바위 사이의 최대 distance = distance

    # 이분탐색을 위해 처음 start, end 지정
    start, end = 1, distance
    
    answer = 0 

    while start <= end: # 정답이 하나로 좁혀지면 while문 통과
        
        mid = ( start + end ) // 2 # 바위 사이의 최솟값 기준
        count = 0 # 제거한 바위의 개수 count
        left = 0 # 왼쪽 바위의 위치 : 첫 왼쪽은 출발지점인 0으로 지정
        
        for i in range(len(rocks)):
            right = rocks[i]  # 오른쪽 바위의 위치

            if right - left < mid: # 바위 사이의 거리가 mid보다 작으면 돌 제거
                count += 1 # 제거 증가

            else:
                left = right # mid보다 크면 돌 제거 안하고 for문 돌리기 위해 세팅

            if n < count: # 제거해야 하는 돌보다 많이 제거되면 for문 탈출
                break
        
        # for문 탈출 후
        if count <= n: # 제거된 돌이 부족, mid와 end 사이로 범위 좁히기 (더 많은 돌 제거)
            answer = mid
            start = mid + 1

        else: # 제거된 돌이 너무 많음, start와 mid 사이로 범위 좁히기 (더 적은 돌 제거)
            end = mid - 1

    return answer
