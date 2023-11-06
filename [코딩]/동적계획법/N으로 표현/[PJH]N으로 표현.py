def solution(N, number):
    if N == number:
        return 1

    # 사칙연산 결과를 저장할 집합 리스트 초기화
    s = [set() for x in range(8)]
    
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))  # 숫자 N 자체를 이어붙인 수 추가

    for i in range(1, len(s)):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)

            if number in s[i]:
                return i+1
    
    return -1
