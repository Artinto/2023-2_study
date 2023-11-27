# 이분법 사용
def solution(n, times):
    answer = 0
    
    left, right = 1, max(times)*n
    # 끝과 끝인 최소값과 최대값을 각각의 변수에 저장
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break
        
        if people >=n:
            answer = mid
            right = mid-1
        elif people < n:
            left = mid +1
        
    return answer
