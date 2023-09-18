from collections import defaultdict

def solution(n, wires):
    # answer를 전체 송전탑의 수로 초기화합니다.
    answer = n
    # 그래프를 나타내는 딕셔너리를 생성합니다. 각 송전탑 번호는 키로 사용되며, 연결된 송전탑들의 리스트가 값으로 저장됩니다.
    graph = defaultdict(list)

    # 모든 전선 정보에 대해 반복하면서 그래프를 구성합니다.
    for a, b in wires:
        graph[a].append(b)  # a와 b가 연결되어 있음을 표시합니다.
        graph[b].append(a)  # b와 a가 연결되어 있음을 표시합니다.

    # 모든 전선에 대해 한 번씩 제거하면서 두 개의 서브그래프로 분할하는 경우를 검사합니다.
    for a, b in wires:
        graph[a].remove(b)  # 현재 선택한 전선을 그래프에서 제거합니다.
        graph[b].remove(a)  

        visited = [0] * (n + 1)  # 방문 여부를 기록할 리스트입니다. 인덱스는 송전탑 번호에 해당하고 값은 방문 여부(0 또는 1)입니다.
        stack = [1]  # DFS 탐색을 위한 스택입니다. 시작점인 송전탑 1을 넣습니다.

        while stack:  
            node = stack.pop()  
            visited[node] = 1   # 현재 노드를 방문했음을 기록합니다.
            stack.extend(x for x in graph[node] if not visited[x])   # 아직 방문하지 않은 이웃 노드들을 스택에 추가합니다.

        count1 = sum(visited)   # 첫 번째 서브그래프의 크기(방문한 송전탑 수)
        count2 = n - count1     # 두 번째 서브그래프의 크기

        answer = min(answer, abs(count1 - count2))   # 첫 번째와 두 번째 서브그래프 사이의 크기 차이가 최소값보다 작으면 업데이트 합니다.

        graph[a].append(b)
        graph[b].append(a)

    return answer
