from collections import defaultdict, deque
def solution(n, edge):
    graph = defaultdict(set)
    for line in edge:
        node1, node2 = line
        graph[node1].add(node2)
        graph[node2].add(node1)
    sequence = [0 for _ in range(n+1)]
    sequence[1] =1
    queue = deque()
    queue.append(1) # 무조건 1부터 시작.
    while queue:
        current=queue.popleft() # 현재 방문
        for v in graph[current]:
            if sequence[v] == 0: 
                queue.append(v)
                sequence[v] = sequence[current] + 1 
    return sequence.count(max(sequence))