from collections import deque # 복잡도를 낮추기 위해 deque 사용
def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0] # 좌우 이동
    dy = [0, 0, -1, 1] # 상하 이동
    queue = deque() # 덱을 통해 큐 생성
    queue.append([0, 0]) # 초기 좌표 설정
    while queue: 
        x, y = queue.popleft() # x=0, y=0 . queue 비게 됨
        for i in range(4): # 상하좌우로 1칸씩 움직여봄
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]): # 움직여진 곳이 지도 내의 장소 내에 있고 
                if maps[nx][ny] == 1: # 움직일 곳이 아직 안 지나간 '길'이면
                    maps[nx][ny] = maps[x][y] + 1 # 거리 +1
                    queue.append([nx, ny]) # 현 좌표 입력
    if maps[-1][-1] > 1: # 이동 완료했다면
      answer = maps[-1][-1] # 거리 반환
    else:
      answer = -1 # 막혔다면 -1 반환
    return answer
