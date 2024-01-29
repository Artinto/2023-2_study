from collections import defaultdict
def solution(n, computers):
    graph = defaultdict(set)
    for idx, computer in enumerate(computers):
        for i, line in enumerate(computer):
            if i == idx:
                continue
            if line == 1:
                graph[idx].add(i)
    
    def dfs(graph, start, visited):
        visited.add(start)
        for node in graph[start]:
            if node not in visited:
                dfs(graph, node, visited)
                
    visited = set()
    answer = 0
    for i in range(n):
        if i not in visited:
            dfs(graph, i, visited)
            answer += 1
    return answer