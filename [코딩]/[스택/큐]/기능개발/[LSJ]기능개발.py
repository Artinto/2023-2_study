import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    q = deque()
 
    # 각 작업을 수행하는데 며칠이 걸리는지 계산하여 queue에 삽입
    for i in range(len(progresses)):
        progress_duration = math.ceil((100 - progresses[i]) / speeds[i]) # 2.55일 -> 3일로 계산해야하기 때문에 ceil 함수 사용
        q.append(progress_duration)
 
    while q:
        end_day = q.popleft() # 기준이 될 값을 가져옴
        cnt = 1
        
        # q에 다른 값들이 남아 있다면 같이 종료될 수 있는 작업 개수를 구함
        while q:
            comp_end_day = q.popleft() # 작업 종료일 비교
            if comp_end_day <= end_day: # 같거나 작은 경우 count 증가
                cnt += 1
            else: # 큰 경우(이후에 끝나는 경우)
                q.appendleft(comp_end_day) # 다시 q에 추가, 이 때 appendleft로 q의 첫부분에 추가(마치 스택)
                break
        answer.append(cnt)
    return answer
