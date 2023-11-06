def solution(arr):
    INF = 1001
    num_list = []
    opr_list = []
    for i in range(len(arr)):
        if i%2 == 0:
            num_list.append(arr[i])
        else:
            opr_list.append(arr[i])
    n = len(num_list)
    min_dp = [[INF for _ in range(n)] for _ in range(n)]
    max_dp = [[-INF for _ in range(n)] for _ in range(n)]
    for step in range(len(num_list)): #i와 j의 간격.
        for i in range(len(num_list)-step): #i부터 j까지의 연산을 수행함.
            j = i + step
            if step==0: # 1단계시
                max_dp[i][i] = min_dp[i][i] = int(num_list[i]) # 숫자로 변환
                continue
            for k in range(i, j): # i 부터 j까지 돌면서, 괄호를 하나는 늘리고, 하나는 줄여서 각각의 범위 연산을 수행함.
                if opr_list[k] == '+': # 연산이 + 일 경우:
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k+1][j]) # + 일 경우 최댓값은 최댓값 + 최댓값임.
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k+1][j]) # + 일 경우 최솟값은 최솟값 + 최솟값임.
                elif opr_list[k] == '-':    # 연산이 - 일 경우.
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j]) # - 일 경우 최댓값은 최댓값 - 최솟값임.
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j])# - 일 경우 최솟값은 최솟값 - 최댓값임.

    return max_dp[0][-1]
