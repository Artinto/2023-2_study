def solution(m, n, puddles):
    a = [[0]*(m+1) for _ in range(n+1)]
    for [x,y] in puddles:
        a[y][x] = -1
    a[0][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i][j] == 0:
                a[i][j] = a[i-1][j] + a[i][j-1]
            else:
                a[i][j] = 0
    return (a[n][m]%1000000007)
