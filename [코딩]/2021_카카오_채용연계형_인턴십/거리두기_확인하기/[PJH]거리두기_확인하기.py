from collections import deque

dx = [-1, 1, 0, 0]  # 상하좌우 이동을 위한 x축 이동 리스트
dy = [0, 0, -1, 1]  # 상하좌우 이동을 위한 y축 이동 리스트

# BFS 함수 정의
def bfs(place, x, y, visited):
    queue = deque([(x, y, 0)])  # 큐에 초기값 (x, y, 맨해튼 거리)
    visited[x][y] = True  # 초기 위치 방문 처리

    while queue:
        x, y, dist = queue.popleft()  # 큐에서 위치와 맨해튼 거리 정보 꺼냄

        if dist == 2:  # 맨해튼 거리 2까지만 검사
            break

        for i in range(4):  # 상하좌우 위치에 대해 반복
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:  # 방문하지 않은 위치라면
                if place[nx][ny] == 'O':  # 빈 테이블이라면
                    queue.append((nx, ny, dist + 1))  # 큐에 넣음
                    visited[nx][ny] = True  # 방문 처리
                elif place[nx][ny] == 'P':  # 다른 사람이 앉아 있으면
                    return False  # 거리두기를 지키지 않은 경우
    return True  # 거리두기를 지킨 경우

# 솔루션 함수 정의
def solution(places):
    answer = []

    for place in places:  # 각 대기실에 대해 반복
        visited = [[False]*5 for _ in range(5)]  # 방문 처리를 위한 리스트 초기화
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P' and not bfs(place, i, j, visited):  # 사람이 앉아 있고, 거리두기를 지키지 않은 경우
                    answer.append(0)  # 0 추가
                    break
            else:
                continue
            break
        else:
            answer.append(1)  # 모든 사람이 거리두기를 지킨 경우 1 추가

    return answer
