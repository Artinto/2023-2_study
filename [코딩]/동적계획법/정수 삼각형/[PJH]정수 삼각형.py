def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:  # 왼쪽 끝 경우
                triangle[i][j] += triangle[i-1][j]
            elif j == i:  # 오른쪽 끝 경우
                triangle[i][j] += triangle[i-1][j-1]
            else:  # 중간에 위치한 경우
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1])  # 마지막 행에서 가장 큰 값을 반환

