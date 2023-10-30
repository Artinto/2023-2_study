def solution(triangle):
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    # dp는 삼각형과 같은 크기의 2D배열로, 모든 원소를 0으로 초기화
    dp[0][0] = triangle[0][0]
    # dp의 첫번 째 원소를 삼각형의 첫 번째 숫자로 초기화
    for i in range(0, len(triangle) - 1):
    # 두 번째 행부터 마지막 행까지 순회하는 루프 시작
    #  -> 삼각형의 아랫부분에서부터 최대 합을 찾아간다
        for j in range(len(triangle[i])):
        # 현재 행의 원소를 순회하는 루프를 시작한다
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
        # 현재 위치에서 아래 행으로 이동하는 경우 현재까지의 최대합과 아래 행의 숫자를 더한 값을 위와 같은 변수에 저장하고 이전 최대 합과 현재 숫자를 비교하여 더 큰 값을 선택한다
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])
        # 현재 위치에서 아래 행의 다음 숫자로 이동하는 경우, 현재까지의 최대 합 dp[i][j]과 아래 행의 다음 숫자 triangle[i + 1][j + 1]을 더한 값을 dp[i + 1][j + 1]에 저장

    return max(dp[-1])
    # 마지막 행의 모든 원소 중에서 최댓값을 반환한다
