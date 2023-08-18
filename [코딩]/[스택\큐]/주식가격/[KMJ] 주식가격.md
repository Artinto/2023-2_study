# 지문 이해 : https://school.programmers.co.kr/questions/20326?question=20326
from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices) # prices를 deque로 변환
    while prices:
        price = prices.popleft() # 가장 먼저 넣었던 값 꺼내서 price에 저장
        count = 0
        
        for i in prices:
            count += 1 # 다음날 가격이 떨어져도 1 카운트
            if i < price: # 가격이 떨어지면 for문 탈출
                break
        answer.append(count) # count값 answer에 추가, 마지막날은 for문을 안돌아서 count값 0
        
    return answer

# list로 하면 효율성 실패
'''
def solution(prices):
    answer = []
    
    while prices:
        price = prices.pop(0)
        count = 0
        
        for i in prices:
            count += 1
            if i < price:
                break
        answer.append(count)
    
    return answer
'''
