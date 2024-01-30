import heapq
def solution(board):
    m = len(board)
    BFS = [[1000000]*(2*m) for _ in range(2*m)]
    BFS[0][1] = 100
    BFS[1][0] = 100
    for i in range(m):
        for j in range(m):
            if board[i][j]==1:
                BFS[2*i+1][2*j] = BFS[2*i-1][2*j] = BFS[2*i][2*j+1] = BFS[2*i][2*j-1] = -1
    Q = [[100,0,1],[100,1,0]]
    while Q:
        d,a,b = heapq.heappop(Q)
        if a%2:
            XY = [(a-2,b),(a+2,b),(a-1,b-1),(a+1,b+1),(a+1,b-1),(a-1,b+1)]
        else:
            XY = [(a,b-2),(a,b+2),(a-1,b-1),(a+1,b+1),(a+1,b-1),(a-1,b+1)]
        for n,(x,y) in enumerate(XY):
            if 0<=x<(2*m-1) and 0<=y<(2*m-1) and BFS[x][y] != -1:
                if n<2 and BFS[x][y] > d+100:
                    BFS[x][y] = d+100
                    heapq.heappush(Q,[d+100,x,y])
                elif n>1 and BFS[x][y] > d+600:
                    BFS[x][y] = d+600
                    heapq.heappush(Q,[d+600,x,y])
    ans = sorted([BFS[2*m-3][2*m-2],BFS[2*m-2][2*m-3]])
    return (ans[0] if ans[0] != -1 else ans[1])
