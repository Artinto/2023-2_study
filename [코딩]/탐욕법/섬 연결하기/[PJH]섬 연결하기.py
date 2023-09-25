def solution(n, costs):
    # 각 노드의 부모 노드를 자기 자신으로 초기화
    parent = [i for i in range(n)]
    
    # 비용을 기준으로 오름차순 정렬, 이렇게 하면 비용이 가장 작은 간선부터 처리
    costs.sort(key=lambda x: x[2])
    
    # find 함수는 주어진 노드의 루트(대표) 노드를 찾음
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    # union 함수는 주어진 두 노드 a, b가 속한 트리(집합)을 합치고 즉, a와 b가 같은 트리에 속하도록 만듦
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        
        if root_x != root_y:
            parent[root_y] = root_x

    # 크루스칼 알고리즘을 적용하여 최소 신장 트리를 찾음
    answer = 0
    for a, b, cost in costs:
        if find(a) != find(b):  # a와 b가 다른 집합에 속해 있다면,
            union(a, b)  # a와 b를 같은 집합으로 합치고,
            answer += cost  # 해당 간선의 비용을 결과값에 추가
            
    return answer
