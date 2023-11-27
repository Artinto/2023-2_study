def solution(distance, rocks, n):
    rocks.sort()
    # 앞쪽에 있는 바위부터 바위 간 거리 검사
    rocks.append(distance)
    # 모든 바위들 간의 거리 검사가 끝났다면, 마지막 바위와 끝 지점(distance) 사이의 거리도 확인이 필요
    left, right = 1,distance
    while left <= right:
        N,now,mid = n,0,(left+right)//2
        # N : 제거 가능한 바위 수, now : 현재 위치(0부터 시작)
        for r in rocks:
            if r-now < mid:
            # 현재 위치로부터 바로 앞에 있는 바위까지의 거리가, 찾고자 하는 값 mid보다 작다면
                N -= 1
                # 바위 제거
                if N < 0:
                # 제거할 수 있는 바위가 없다면
                    right = mid - 1
                    # 바위들 간의 거리의 최솟값은 그보다 작음
                    break
            else:
                now = r
                # 문제가 없다면 해당 바위로 기준 위치를 이동한 뒤 계속 확인
        else:
        # 모든 바위에 대해 확인한 결과 문제가 없다면
            left = mid + 1
            # 바위들 간의 거리의 최솟값 기준을 더 올리고 다시 확인
            ans = mid
    return ans
