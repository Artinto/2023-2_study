def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)] # 다른 컴퓨터와의 관계 검사 여부

    def dfs(computer): 
        visited[computer] = 1
        for peer in range(n):
            if computers[computer][peer] == 1 and visited[peer] == 0:
                dfs(peer)

    for computer in range(n):
        if visited[computer] == 0:
            dfs(computer)
            answer += 1

    return answer
