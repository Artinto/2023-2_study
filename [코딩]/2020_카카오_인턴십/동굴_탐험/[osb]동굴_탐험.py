from collections import defaultdict, deque
n, path, order = 9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]	
answer = False
graph = defaultdict(set)
for edge in path:
    node1, node2 = edge[0], edge[1]
    graph[node1].add(node2)
    graph[node2].add(node1)
# 순서 정의를 위해 사용
# end_node는 start_node가 방문된 상태에서 방문해야함.
start_node = [0] * n
end_node = [0] * n 
visited = [0] * n # 방문 확인용 노드
queue = deque([0])
for edge in order:
    node1, node2= edge[0], edge[1]
    start_node[node1] = node2
    end_node[node2] = node1

def check_the_order(node2, visited):
    if end_node[node2] == 0: # 순서가 안정해진 노드
        return True
    if visited[end_node[node2]] == 0 and visited[node2] != 0: # 순서가 안지켜졌다면! False
        return False
    return True # 아니면 True

while queue:
    current = queue.popleft() # 현재노드
    visited[current] += 1
    print(current)
    if 0 not in visited: # 모두 방문했다면
        answer = True
        break
    for node in graph[current]:
        if check_the_order(node, visited): # 가능하다면
            queue.append(node)
