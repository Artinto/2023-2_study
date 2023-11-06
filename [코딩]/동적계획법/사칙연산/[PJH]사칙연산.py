def solution(arr):
    # 숫자와 연산자를 구분하여 저장
    arr = [int(arr[i]) if i % 2 == 0 else arr[i] for i in range(len(arr))]
    
    # 숫자의 개수
    n = len(arr) // 2 + 1
    
    # dp_max와 dp_min은 각 구간의 최댓값과 최솟값을 저장할 2차원 리스트
    dp_max = [[0]*n for _ in range(n)]
    dp_min = [[0]*n for _ in range(n)]
    
    # 초기값 설정
    for i in range(n):
        dp_max[i][i] = arr[i*2]  # 최댓값
        dp_min[i][i] = arr[i*2]  # 최솟값
    
    # 각 구간에 대해 최댓값과 최솟값을 계산
    for cnt in range(2, n+1):
        for i in range(n-cnt+1):
            j = i + cnt - 1
            # 최댓값 계산: i에서 j까지의 구간에서 가능한 모든 연산을 고려
            dp_max[i][j] = max(
                dp_max[i][k-1] + (dp_max[k][j] if arr[(k-1)*2+1] == '+' else -dp_min[k][j]) for k in range(i+1, j+1)
            )
            # 최솟값 계산: i에서 j까지의 구간에서 가능한 모든 연산을 고려
            dp_min[i][j] = min(
                dp_min[i][k-1] + (dp_min[k][j] if arr[(k-1)*2+1] == '+' else -dp_max[k][j]) for k in range(i+1, j+1)
            )
    
    # 전체 구간의 최댓값 반환
    return dp_max[0][n-1]
