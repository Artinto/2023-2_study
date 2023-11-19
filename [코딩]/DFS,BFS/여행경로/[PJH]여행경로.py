from collections import defaultdict

def solution(tickets):
    answer = []
    routes = defaultdict(list)
    for start, end in sorted(tickets, reverse=True): # 알파벳 순서가 앞서는 경로를 먼저 방문하도록 정렬
        routes[start].append(end) # 각 출발지에서 갈수 있는 도착지 리스트 추가
    path = [] # 경로 리스트 초기화
    def dfs(start):
        while routes[start]:
            dfs(routes[start].pop())
        path.append(start)
    dfs("ICN")
    answer = path[::-1] # 다시 경로를 역순으로 바꿔줌
    return answer

