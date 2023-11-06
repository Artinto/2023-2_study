def solution(m, n, puddles):
    answer = 0
    # 각 지점까지의 최단 경로 개수를 저장할 2차원 배열
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # 물에 잠긴 지역 표시
    for puddle in puddles:
        dp[puddle[0]][puddle[1]] = -1
    
    # 시작 지점의 최단 경로는 1로 초기화
    dp[1][1] = 1
    
    # 동적 계획법을 이용하여 최단 경로 개수 계산
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 집과 학교의 경우는 스킵
            if i == 1 and j == 1:
                continue
            # 물에 잠긴 지역이 아니라면 왼쪽과 위쪽에서 오는 경로를 더함
            if dp[i][j] != -1:
                from_left = dp[i - 1][j] if dp[i - 1][j] != -1 else 0
                from_above = dp[i][j - 1] if dp[i][j - 1] != -1 else 0
                dp[i][j] = (from_left + from_above) % 1000000007
        answer =dp[m][n]
    return answer
