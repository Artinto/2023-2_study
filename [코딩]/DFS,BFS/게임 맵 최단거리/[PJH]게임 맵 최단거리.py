def solution(maps):
    # 이동 방향 설정 (좌, 상, 우, 하)
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    
    # 맵의 크기
    n = len(maps)
    m = len(maps[0])
    
    # 방문 여부 및 거리를 저장하는 2차원 리스트 초기화
    visited = [[-1]*m for _ in range(n)]
    visited[0][0] = 1
    
    # BFS를 위한 큐, 시작 위치 추가
    queue = [[0, 0]]
    
    while queue:
        # 현재 위치
        x, y = queue.pop(0)
        
        for direction in directions:
            nx, ny = x + direction[0], y + direction[1]
            
            # 맵을 벗어나지 않는지, 벽이 아닌지, 방문하지 않았는지 확인
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1 and visited[nx][ny] == -1:
                # 현재 위치까지의 거리 + 1을 저장
                visited[nx][ny] = visited[x][y] + 1
                # 다음 위치를 큐에 추가
                queue.append([nx, ny])
                
    # 상대 팀 진영까지의 최단 거리 반환, 도달할 수 없는 경우 -1 반환
    return visited[-1][-1]
