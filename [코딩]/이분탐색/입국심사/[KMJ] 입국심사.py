import math
def solution(n, times):
    low = min(times) * (math.ceil(n / len(times)))
    # low = 1로 하는 경우가 많은데, 계산량 더 줄이기 위해
    # low = min(times) * (n / len(times))도 가능
    high = max(times) * n

    while low <= high:
        mid = (low + high) // 2
        people = 0
        for i in times:
            people += mid // i
            if people >= n:
                break
        if people >= n:
            answer = mid
            high = mid - 1
        elif people < n:
            low = mid + 1
            
    return answer
