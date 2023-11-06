def solution(money):
    answer = 0
    x1, y1 = money[0], money[1] # 첫번째 집 털었을 때
    x2, y2 = 0, money[1] # 첫번째 집 안털었을 때
    next_1, next_2 = money[0]+money[2], money[2] 
    for i in money[3:]:
        x1, y1, next_1 = y1, next_1, max(x1, y1) + i
        x2, y2, next_2 = y2, next_2, max(x2, y2) + i
    #answer = max(x1, y1, next_1, x2, y2, next_2) # next_1은 첫번째, 마지막 포함이므로 제외
    answer = max(x1,y1, x2, y2, next_2)
    return answer
