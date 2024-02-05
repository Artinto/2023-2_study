from collections import deque

def solution(board):
    n = len(board)
    costs = [[[float('inf')]*4 for _ in range(n)] for _ in range(n)]
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]  # 상, 좌, 하, 우
    queue = deque([(0, 0, -1, 0)])  # x, y, direction, cost

    while queue:
        x, y, direction, cost = queue.popleft()
        for i in range(4):  # 4방향으로 이동
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                ncost = cost + 100 if direction == -1 or direction == i else cost + 600
                if costs[nx][ny][i] > ncost:
                    costs[nx][ny][i] = ncost
                    queue.append((nx, ny, i, ncost))

    return min(costs[n-1][n-1])
