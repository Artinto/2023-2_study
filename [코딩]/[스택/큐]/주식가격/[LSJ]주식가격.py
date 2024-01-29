def solution(prices):
    answer = []
    for i in range(len(prices)): # prices의 요소 개수만큼 반복
        cnt = 0 # 가격이 떨어지지 않은 기간, 0으로 초기화
        for j in range(i+1, len(prices)): #i번째 요소 뒤의 요소들 확인
            if prices[j] < prices[i]: # 주식 가격이 떨어지면
                cnt = j-i # 인덱스 차이 = 가격이 떨어지지 않은 기간
                break
            elif j == len(prices) - 1: # 끝까지 가격이 떨어지지 않는다면
                cnt = j-i
        answer.append(cnt) # 반복마다 cnt 값 answer 리스트에 추가
    return answer
