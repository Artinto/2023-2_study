def solution(distance, rocks, n):
    left = 1
    # 최소값 설정
    right = distance
    # 최대값 설정
    
    rocks.sort()
    rocks.append(distance)
    
    while left <= right:
        mid = (left+right)//2
        delete = 0
        # 이전 바위의 위치
        prev_rock = 0
        for rock in rocks:
            dist = rock - prev_rock
            if dist < mid:
                delete += 1
                if delete > n:
                    break
            else:
                prev_rock = rock
                
        if delete > n:
            right = mid -1
        else:
            answer = mid
            left = mid + 1
    return answer
