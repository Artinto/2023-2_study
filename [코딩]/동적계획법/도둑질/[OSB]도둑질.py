def solution(money):
    case1 = [0] * len(money) # 빈 리스트 선언
    # 첫 집을 무조건 터는 경우
    case1[0] = money[0]
    case1[1] = max(money[0], money[1])
    
    for i in range(2, len(money)-1): 
        case1[i] = max(case1[i-1], money[i]+case1[i-2]) # 현재 나를 선택 vs 전위치 최고선택 값
    # 마지막 집을 무조건 터는 경우
    case2 = [0] * len(money)
    case2[0] = 0 
    case2[1] = money[1]
    for i in range(2, len(money)):
        case2[i] = max(case2[i-1], money[i]+case2[i-2])
    # 두가지 경우중 최대.
    answer = max(max(case1), max(case2))
    return answer
