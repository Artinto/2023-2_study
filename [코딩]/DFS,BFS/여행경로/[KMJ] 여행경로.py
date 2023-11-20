def solution(tickets):
    # tickets.sort(key = lambda x: (x[0], x[1])) # 알파벳 순으로 티켓 정렬
    
    routes = {} # tickets를 딕셔너리 형태로 변환

    for start, fin in tickets:
        routes[start] = routes.get(start, []) + [fin]
        # key : start, value : fin(여러개 가능)
        # {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}
        
    for a in routes:
        routes[a].sort(reverse=True) # routes 내림차순으로 정렬

    # 처음에는 ICN에서 출발하므로 ICN 넣어주고 시작
    go = ['ICN'] # 여행 경로가 저장되는 리스트
    path = [] # 백트래킹을 위한 리스트

    while go: # first가 비워지면 while문 통과
        now = go[-1] # 현재 탐색중인 나라
        
        if not now in routes or not routes[now]: # 갈 수 없는 경우
            # now가 key로 존재하지 않거나
            # 이미 갔던 곳이라 now의 value가 존재하지 않는 경우
            
            path.append(go.pop()) # 현재 위치를 path에 넣고 이전으로 돌아가기 (백트래킹)
            
        else: # 갈 수 있는 경우
            go.append(routes[now].pop()) # now의 경로를 go에 넣어서 다시 경로 탐색 (이전 도착지 -> 다음 출발지)

    return path[::-1] # 백트래킹 때문에 역순으로 저장되므로 뒤에서부터 반환
