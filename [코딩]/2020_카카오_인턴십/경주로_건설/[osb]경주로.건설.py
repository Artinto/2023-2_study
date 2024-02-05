board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
from collections import deque
move_array = [(0,1), (1,0), (-1, 0), (0,-1)] # 움직일수 있는 방향
queue = deque()
queue.append([0, 0, 0, 0])  # y, x, cost, last_move
visited = [[0]*len(board) for _ in range(len(board))]  # 2차원 배열로 변경
board[0][0] = -500
while queue:
    y, x, cost, last_move = queue.popleft()
    # 방문 처리
    visited[y][x] += 1
    for i, move in enumerate(move_array):
        new_y = y + move[0]
        new_x = x + move[1]
        if 0 <= new_y < len(board) and 0 <= new_x < len(board) and board[new_y][new_x] != 1: # 범위 안에 있고, 벽이 아닌 경우
            if i == last_move: # 이전방향과 같다면,
                new_cost = cost + 100
            else:
                new_cost = cost + 600
            if board[new_y][new_x] == 0 or board[new_y][new_x] > new_cost:  # 비용이 더 적다면
                board[new_y][new_x] = new_cost
                queue.append([new_y, new_x, new_cost, i])
print(board[-1][-1])


# 위 방법은 이제 같은 비용일 때 다른 방향성에 대해 고려가 안됨.
# 방문 요소를 이제 비용을 기준으로 함.
from collections import deque
def solution(board):
    N = len(board)
    move_array = [(0,1), (1,0), (-1, 0), (0,-1)] # 움직일 수 있는 방향: 우, 하, 상, 좌
    INF = float('inf')
    
    # 비용을 저장할 3차원 배열, 각 방향별로 비용을 저장
    costs = [[[INF]*N for _ in range(N)] for _ in range(4)]
    
    queue = deque()
    queue.append([0, 0, -1, 0])  # y, x 이전에 이동한 방향, 비용
    
    while queue:
        y, x, direction, cost = queue.popleft()
        for i, move in enumerate(move_array):
            new_y = y + move[0]
            new_x = x + move[1]
            if 0 <= new_y < N and 0 <= new_x < N and board[new_y][new_x] != 1: # 범위 안에 있고, 벽이 아닌 경우
                if direction == i or direction == -1: # 이전 방향과 같다면
                    new_cost = cost + 100
                else: # 이전 방향과 다르다면
                    new_cost = cost + 600
                # 새로운 비용이 기존 비용보다 작거나 같다면
                if new_cost < costs[i][new_y][new_x]:  
                    costs[i][new_y][new_x] = new_cost
                    queue.append([new_y, new_x, i, new_cost])
    
    # 도착점에 도달하는 각 방향의 최소 비용 중 가장 작은 비용을 반환
    return min(costs[0][-1][-1], costs[1][-1][-1], costs[2][-1][-1], costs[3][-1][-1])
