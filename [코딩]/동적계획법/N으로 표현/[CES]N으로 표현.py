# N이 i개 있는 만큼 set을 만들어주기
# dp[i]는 dp[i-1]의 구성요소로 사칙 연산이 구성 되어있다
# 최종 dp[i] set에서 number가 존재하면 i를 반환
# 발견 못하면 -1 출력
def solution(N, number):
    answer = -1
    dp = []
    # 이 리스트는 동적 프로그래밍(DP)의 중간 결과를 저장할 목적으로 사용
    for i in range(1,9):
    # i는 N의 개수
        A_case = set()
        # 가능한 모든 숫자 조합을 저장할 용도로 사용
        C_number = int(str(N)*i)
        # N을 i만큼 곱한 값을 정수 형태로 C_number에 저장
        A_case.add(C_number)
        # A_case 집합에 C_number를 추가. 이것은 현재 i개의 N만 사용해서 만들 수 있는 숫자를 저장
        
            for j in range(0, i-1):
            # j개를 사용해서 만든 값 
                for op1 in dp[j]:
                # dp 리스트에서 이전 단계에서 계산한 j개의 N을 사용한 경우의 수를 반복
                    A_case.add(op1-op2)
                    A_case.add(op1+op2)
                    A_case.add(op1*op2)
                    # A_case 집합에 op1과 op2 간의 뺄셈, 덧셈, 곱셈 결과를 추가
                    if op2 != 0:
                        A_case.add(op1//op2)
                        # 만약 op2가 0이 아니라면, 나눗셈 결과를 A_case에 추가
            if number in A_case:
                # 목표 숫자인 number가 A_case 집합 안에 있다면,목표로 하는 숫자를 만들 수 있는 경우
                answer = i
                # answer 변수를 i로 설정하고, 이것은 N을 몇 번 사용하여 목표 숫자를 만들 수 있는지를 나타냄
                break
                # 목표 숫자를 만들었으므로 루프를 종료
            dp.append(A_case)
            # 이번 루프에서 계산한 A_case 집합을 dp 리스트에 추가
        return answer
        # answer 값 반환 (최종 결과 도출)
                        
                
