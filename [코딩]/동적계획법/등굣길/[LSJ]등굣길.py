def solution(m, n, puddles):
    answer = 0
    puddles = [[q,p] for [p,q] in puddles] #좌표 거꾸로인거 웅덩이에도 적용
    dp = [[0] * (m + 1) for i in range(n + 1)]  # 격자 생성 (0으로 채워놓음)
    dp[1][1] = 1 # 집의 위치 (1,1) 부터 경로 시작, 경우의 수 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: continue 
            if [i, j] in puddles: # 웅덩이를 지나는 경우
              dp[i][j] = 0 # 그 경로의 값을 0으로 지정
            else: 
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007 # 왼쪽 칸과 위쪽 칸의 0~1 숫자 합이 해당 칸을 지나는 경로의 수
    answer = dp[n][m] # 다 더해진 값
    return answer
