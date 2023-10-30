def solution(money):
    dp1 = [0] * len(money) # 집의 개수만큼 0 값들을 가진 리스트 생성
    dp1[0] = money[0] # 첫번째 집 털었을 때
    dp1[1] = max(money[0], money[1]) # 첫 번째 집과 두번째 집 둘 중 어디 털지

    dp2 = [0] * len(money) # 집의 개수만큼 0 값들을 가진 리스트 생성
    dp2[0] = 0 # 첫번째 집을 안 털었으므르 0
    dp2[1] = money[1] # 첫번째 집을 안 털었으므로 두번째집 값만 가져옴
    
  for i in range(2, len(money)-1): # 마지막 집을 털지 않는 경우
        dp1[i] = max(dp1[i-1], money[i]+dp1[i-2]) # 직전의 집만 턴 값과 현재 집+2칸 전의 집을 턴 경우 비교 큰 값 고름

    for i in range(2, len(money)): # 첫번째 집을 털지 않는 경우
        dp2[i] = max(dp2[i-1], money[i]+dp2[i-2]) # 직전의 집만 턴 값과 현재 집+2칸 전의 집을 턴 경우 비교 큰 값 고름

    return max(max(dp1), max(dp2)) # 두 경우 중 최댓값
