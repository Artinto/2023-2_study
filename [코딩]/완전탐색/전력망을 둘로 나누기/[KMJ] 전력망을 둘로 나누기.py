# 전선을 하나씩 끊어서 계산하기
# 끊어서 생기는 그룹을 계산하기
# 가장 작은 차이를 구하기

def dfs(graph, node, visited): # 해당하는 그룹의 송전탑 개수를 저장하기 위한 함수
    
    # node는 현재 송전탑의 위치
    visited[node] = True # 송전탑의 개수를 셀 때 중복으로 세지 않게 하기 위해 사용하는 flag
                         # 방문하기 전에는 False
    
    size = 1  # 현재 그룹의 송전탑 개수를 저장할 변수

    for neighbor in graph[node]: # graph[node]는 송전탑 리스트 중 현재 노드와 연결된 것만 반복
        if not visited[neighbor]: # 이웃노드(연결된 노드)에 방문하지 않았다면 (false라면)
            size += dfs(graph, neighbor, visited) # 재귀함수를 통한 크기 계산
                                                  # 현재 노드와 연결된 이웃노드와 연결된 이웃노드 ...
                                                  # 모두 방문하면 더 이상 연결된 것이 없음

    return size

def solution(n, wires):
    answer = float('inf') # 초기값은 무한으로
    
    graph = [[] for _ in range(n + 1)] # 연결되어있는 송전탑들을 나타내기 위한 리스트
                                       # 크기는 n의 개수만큼
    
    # 서로 연결되어 있는 송전탑 리스트를 graph에 작성 #
    for a, b in wires:
        graph[a].append(b) # a, b가 붙어있으므로 a번째 그래프에 b를 추가
                           # [1,3],[2,3],[3,4] -> 
                           # grape[1] = 3, grape[2] = 3, grape = [1,2,4], graph[4] = 3
        graph[b].append(a) # 방향성(순서)이 없으므로 반대가 되는 경우에도 추가
    
    # 차례로 하나씩 끊어보면서 차이를 계산 #
    for a, b in wires:
        graph[a].remove(b) # remove를 통해 연결을 끊어냄
        graph[b].remove(a)
        
        # 두 그룹의 송전탑 개수 계산
        visited = [False] * (n + 1) # 송전탑의 개수를 셀 때 중복으로 세지 않게 하기 위해 사용하는 flag
        group1_size = dfs(graph, a, visited) # dfs함수를 통해 그룹의 크기 구함
        group2_size = n - group1_size # dfs함수를 통해 다른 그룹의 크기 구함
        
        # 두 그룹의 송전탑 개수 차이 계산
        diff = abs(group1_size - group2_size)
        
        # 최소 차이 업데이트
        answer = min(answer, diff) # 현재 거리와 이전에 계산한 거리 중 작은 수를 answer에 다시 대입
        
        # 전선을 다시 연결하여 다음 경우를 시도할 수 있도록 복원
        graph[a].append(b)
        graph[b].append(a)
    
    return answer
