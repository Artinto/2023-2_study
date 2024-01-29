from collections import deque

def solution(prices):
    # 물건의 가격 변동 정보가 담긴 리스트를 입력 받음
    queue = deque(prices)
    # 물건의 가격 변동 정보를 큐에 담고 입력으로 받은 prices 리스트를 큐로 변환하여 저장
    answer = []
    # 각 물건에 대한 가격 하락까지 걸린 시간을 담는 리스트 -> 초기화
    while queue:
        # 큐에 원소가 남아있는 동안 루프 실행
        # 모든 물건에 대한 가격 하락 시간 계산
        price = queue.popleft()
        # queue에서 물건의 가격을 꺼내서 price 변수에 저장
        sec = 0
        # 현재 물건이 하락하는데 걸린 시간의 변수의 sec을 0으로 초기화
        for q in queue:
            # 현재 물건의 가격과 그 이후 물건들의 가격 비교하면서 반복문을 돌린다
            sec += 1
            # 시간을 1초씩 누적하여 더함
            if price > q:
                # 가격이 하락됐다면
                break 
                # 루프 중단
        answer.append(sec)        
        # 현재 물건에 대한 가격 하락까지 걸린시간을 answer 리스트에 추가
    return answer
# 위의 도출된 answer 값을 반환
