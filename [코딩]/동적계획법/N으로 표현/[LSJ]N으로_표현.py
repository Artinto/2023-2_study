def solution(N, number):
    answer = 0
    dp = [set() for _ in range(8)] # N을 -개씩 사용해 만들 수 있는 숫자들 집합. 횟수가 8을 넘어가면 -1로 지정하므로 8개의 집합만 생성
    for i in range(1, 9):
        dp[i-1].add(int(str(N)*i)) # N이 사칙연산 없 연속으로 사용된 경우
        if i == 1: # 위에 포함되므로 패
            continue
        for j in range(i-1):
            for op1 in dp[j]: # N만 사용된것이 아닌 N(사칙연산)NN or NN(사칙연산)N과 같이 집합이 사용되므로
                for op2 in dp[i-j-2]: # dp의 index가 0부터 시작하므로 i-1-j-1
                    dp[i-1].add(op1 + op2) # 각각의 
                    dp[i-1].add(op1 - op2) # 사칙연산 결과를
                    dp[i-1].add(op1 * op2) # dp[i-1]에
                    if op2 != 0:
                        dp[i-1].add(op1 // op2) # 추가
    answer = -1   # 최솟값이 8을 넘어갔을 때 -1로 지
    for idx, val in enumerate(dp): # 내장함수 enumerate를 통해 index,value로 dp를 분리
        if number in val: # number 값이 dp에 있다면
            answer = idx + 1 # index+1 값을 answer로 저장
            break
    return answer
