def solution(N, number):
    dp = [set() for i in range(9)] 
    # 사용 횟수에 따라 가능한 숫자를 담을 리스트 dp를 생성
    # dp리스트는 1~8까지의 index를 가진다
    for i in range(1, 9): 
    # N의 개수를 1부터 8까지 증가시키는 루프
        dp[i].add(int(str(N)*i)) 
        # N을 i번 반복한 값을 dp[]집합에 추가
        for j in range(i//2 + 1):
        # 이중 루프를 시작하여 j개의 N을 사용한 경우를 고려
        # i//2를 사용하는 이유는 중복되는 연산을 피하기 위해서
            for first in dp[j]:
            # 집합에서 j개의 N을 사용한 경우의 수 반복
                for second in dp[i-j]:
                # 집합에서 나머지개의 N을 사용한 경우의 수 반복
                    dp[i].add(first + second)
                    dp[i].add(first - second)
                    dp[i].add(second - first)
                    dp[i].add(first * second)
                    # 덧셈,뺄셈,뺄셈(반대),곱셈 결과 추가
                    if second != 0 :
                    # 만약 second가 0이 아니라면
                        dp[i].add(first // second)
                        # 나눗셈 결과를 추가
                    if first != 0 :
                    # 만약 first가 0이 아니라면    
                        dp[i].add(second // first)
                        # 나눗셈 결과를 추가
                    
        if number in dp[i]:
        # 만약 목표숫자인 number가 dp 집합 안에 있다면
            return i
            # i를 return
    return -1
    # 목표숫자가 없다면 -1를 반환
                
