def solution(maps):
    n,m = len(maps),len(maps[0])         # n : 세로 길이 / m : 가로 길이
    queue = [(0,0)]                      # 큐 : 초기값은 현재 위치의 좌표값, 이후 앞으로 가야 할(아직 가보지 못한 곳) 좌표값들을 append
    d = [(1,0),(-1,0),(0,1),(0,-1)]      # d[0] : +y방향으로 한 칸 이동 / d[1] : -y방향으로 한 칸 이동 / d[2] : +x방향으로 한 칸 이동 / d[3] : -x방향으로 한 칸 이동
    while queue:                         # 아직 못 가본 곳이 있다면
        x,y = queue.pop(0)               # 그곳들의 좌표들 중 하나를 pop & return
        for i in range(4):
            xx,yy = x+d[i][0], y+d[i][1]                        # 현재 위치 (x,y)에서 위/아래/왼쪽/오른쪽으로 한 칸 이동한 곳의 좌표를 (xx,yy)라고 할 때
            if 0<=xx<=n-1 and 0<=yy<=m-1 and maps[xx][yy] == 1: # (xx,yy)가 map을 벗어나지 않으며 벽(value == 0)이 아님과 동시에 처음 방문한다면
                maps[xx][yy] += maps[x][y]                      # (xx,yy)의 value는 (0,0)에서 해당 위치까지의 최단 거리이며, 이는 이전 위치였던 (x,y)의 value에 1을 더한 값과 같다
                queue.append((xx,yy))                           # (xx,yy)를 큐에 추가했기 때문에 while문이 반복된다
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1
    # 더 이상 갈 수 있는 곳이 없을 때 while문 종료
    # 만약 목적지의 좌표가 1이라면 목적지에 도달할 수 없다는 뜻이므로 -1을 return
    # 1이 아니라면 해당 좌표의 value를 return
