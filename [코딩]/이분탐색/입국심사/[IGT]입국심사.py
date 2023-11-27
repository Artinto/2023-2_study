def solution(n, times):
    left, right = 1, min(times)*n
    # minimum : 1, maximum : 처리 속도가 제일 빠른 심사관이 모든 작업을 맡아서 했을 경우, 그 때 걸리는 시간
    while left <= right:
        mid = (left+right)//2
        s = sum([mid//t for t in times])
        # s : 임의의 시간 mid 동안 각 심사관들이 처리할 수 있는 인원 수의 합
        if s >= n:
            ans = mid
            right = mid-1
        else:
            left = mid+1
    return ans
