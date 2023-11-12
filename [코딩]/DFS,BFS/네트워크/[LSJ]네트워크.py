def solution(n, computers):
    count = 0  # 네트워크의 개수를 세는 변수
    visited = [0 for _ in range(n)]  # 각 컴퓨터(노드)가 방문된 상태를 저장하는 배열

    # 모든 컴퓨터에 대해서 반복
    for i in range(n):
        # 아직 방문하지 않은 컴퓨터인 경우
        if visited[i] == 0:
            stack = [i]  # 방문할 컴퓨터들을 저장하는 스택. 현재 컴퓨터부터 시작.
            
            # 아직 방문하지 않은 컴퓨터가 있으면 계속 반복
            while stack:
                node = stack.pop()  # 스택에서 하나의 컴퓨터를 꺼냄. 이 컴퓨터를 방문할 것임.
                visited[node] = 1  # 해당 컴퓨터를 방문했다고 표시
                
                # 모든 컴퓨터에 대해 반복
                for j in range(n):
                    # 현재 컴퓨터와 연결되어 있고, 아직 방문하지 않은 컴퓨터가 있으면
                    if computers[node][j] == 1 and visited[j] == 0:
                        stack.append(j)  # 스택에 추가. 이후에 방문할 것임.
                        
            count += 1  # 하나의 네트워크를 모두 방문했으므로 네트워크 개수를 하나 증가시킴

    return count  # 네트워크의 개수를 반환
