def solution(n, computers):
    # 컴퓨터를 방문했는지 체크하는 리스트, 초기에는 모든 컴퓨터를 방문하지 않았으므로 0으로 초기화
    visited = [0 for i in range(n)]
    
    # DFS를 위한 스택
    dfs = []
    
    # 네트워크의 개수를 저장하는 변수
    answer = 0
    
    # 모든 컴퓨터에 대해 탐색을 수행
    while 0 in visited:
        # 방문하지 않은 컴퓨터를 찾아서 스택에 추가
        x = visited.index(0)
        dfs.append(x)
        visited[x] = 1
        
        # DFS를 통해 연결된 컴퓨터를 모두 방문
        while dfs:
            # 스택에서 컴퓨터를 하나 꺼내어 방문
            node = dfs.pop()
            visited[node] = 1
            
            # 꺼낸 컴퓨터와 연결된 모든 컴퓨터에 대해 방문하지 않았다면 스택에 추가
            for i in range(n):
                if visited[i] == 0 and computers[node][i] == 1:
                    dfs.append(i)
                    
        # 한 네트워크에 대한 탐색이 끝났으므로 네트워크 개수를 증가시킴
        answer += 1
        
    # 찾은 네트워크의 개수를 반환
    return answer
