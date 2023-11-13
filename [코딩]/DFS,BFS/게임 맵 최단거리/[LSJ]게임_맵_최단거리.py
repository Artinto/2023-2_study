from collections import deque # 복잡도를 낮추기 위해 deque 사용
def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0] # 좌우 이동
    dy = [0, 0, -1, 1] # 상하 이동
    queue = deque() # 덱을 통해 큐 생성
    queue.append([0, 0]) # 초기 좌표 설정
    while queue: 
        x, y = queue.popleft() # x=0, y=0 . queue 비게 됨
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append([nx, ny])
    if maps[-1][-1] > 1:
      answer = maps[-1][-1] 
    else:
      answer = -1
    return answer
