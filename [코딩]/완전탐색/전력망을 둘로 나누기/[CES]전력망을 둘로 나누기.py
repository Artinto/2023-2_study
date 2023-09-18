from collections import defaultdict

def solution(n, wires):
    answer = n
    graph = defaultdict(list)


    for a, b in wires:
        graph[a].append(b) 
        graph[b].append(a)  

    for a, b in wires:
        graph[a].remove(b) 
        graph[b].remove(a)  

        visited = [0] * (n + 1)
        stack = [1]  

        while stack:  
            node = stack.pop()  
            visited[node] = 1  
            stack.extend(x for x in graph[node] if not visited[x])  
        count1 = sum(visited)  
        count2 = n - count1    

        answer = min(answer, abs(count1 - count2))  
        graph[a].append(b)
        graph[b].append(a)

    return answer
