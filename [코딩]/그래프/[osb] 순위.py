from collections import defaultdict, deque
def solution(n, results):
    win_graph = defaultdict(set)
    loss_graph = defaultdict(set)
    for line in results:
        node1, node2 = line
        win_graph[node1].add(node2)
        loss_graph[node2].add(node1)
    # 초기화

    win_dict, loss_dict = {i:{} for i in range(1, n+1)}, {i:{} for i in range(1, n+1)}
    for i in range(1, n+1): # 각 노드에 대해 이기고 진노드 찾기.
        queue=deque()
        queue.append(i)
        visited= [0 for _ in range(n+1)]
        while queue: # 내가 이긴 노드 찾기
            current=queue.popleft()
            win_dict[current][current]=1 # 내 자신 추가
            if current not in loss_graph:
                continue
            for node in loss_graph[current]:
                if visited[node] == 0:
                    visited[node]= 1
                    for j in win_dict[current]: 
                        win_dict[node][j]=1
                    queue.append(node)
        #-----------------------------------------------------------------
        queue=deque()
        queue.append(i)
        visited= [0 for _ in range(n+1)]
        while queue: # 내가 진 노드 찾기
            current=queue.popleft()
            loss_dict[current][current]=1 # 내 자신 추가.
            if current not in win_graph:
                continue
            for node in win_graph[current]:
                if visited[node] == 0:
                    visited[node]= 1
                    for j in loss_dict[current]: 
                        loss_dict[node][j]=1
                    queue.append(node)

    count=0 
    for i in loss_dict:
        if len(loss_dict[i])-1+len(win_dict[i]) == n: # 합이 n이면 순위가 정해짐. 
            count+=1
    # 진 노드 파악
    return count