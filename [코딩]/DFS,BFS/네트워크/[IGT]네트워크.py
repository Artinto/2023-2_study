def solution(n, computers):
    C = [x for x in range(n)] # 모든 computer들의 numebr를 list로 나열
    answer = 0
    while C:
        visited = []        # 방문한 적이 있는 computer
        queue = []         # 방문 예정인 computer
        queue.append(C[0]) # 아직 확인하지 않은 computer들 중 하나를 꺼내서 큐에 추가
        while queue:
            node = queue.pop(0) # 큐에 들어있는 computer 중 첫 번째를 pop & return
            if node not in visited:  # 만약 방문한 적이 없었다면
                visited.append(node) # visited에 추가함으로써 해당 computer는 더 이상 확인할 필요가 없다고 지정
                queue.extend([idx for idx, i in enumerate(computers[node]) if i==1 and idx!=node]) # 그 computer에 연결된 다른 computer들을 다음에 확인하기 위해 큐에 추가
                # 만약 처음 확인한 computer가 1번 computer였다면, 1번 computer에 연결된 다른 모든 computer들을 큐에 추가하고, 1번은 visited에 추가
        answer += 1 # 하나의 computer에 연결된 connection들을 전부 확인했으며, 이것이 하나의 network가 된다
        C = [x for x in C if x not in visited] # 전체 computer list에서 방문한 computer의 number를 제외
    return answer
