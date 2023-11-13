def solution(n, computers):
    C = {x for x in range(n)}
    answer = 0
    while C:
        visited = set()
        queue = list()
        queue.append(list(C)[0])
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                queue.extend([idx for idx, i in enumerate(computers[node]) if i==1 and idx!=node])
        answer += 1
        C -= visited
    return answer
