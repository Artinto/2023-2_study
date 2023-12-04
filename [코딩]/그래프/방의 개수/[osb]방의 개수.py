'''
방의 생성의 경우:
방문한 노드를 재방문 했을 경우 + 재방문 시 새로운 간선(edge)를 통해 방문햇을 경우에만 생성
모래시계의 경우에는 위의 경우이지만 동시에 두개의 방이 생기는 문제가 있으므로 이동을 두배씩 해줘
가운데의 점인 새로운 노드를 생성해서 문제를 해결할 수 있다.

'''

def solution(arrows):
    answer = 0
    move = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # 8방향 이동
    current_node = (0,0)
    visited_nodes = set()  # 방문한 노드 저장
    visited_edges = set()  # 방문한 경로 저장
    visited_nodes.add(current_node)# 현재 노드 추가.
    
    for arrow in arrows:
        for _ in range(2):
            # 새로운 노드로 이동.
            new_node = (current_node[0] + move[arrow][0], current_node[1] + move[arrow][1])
            # 방이 생성되는 경우.
            if new_node in visited_nodes and (current_node, new_node) not in visited_edges:
                answer += 1
            
            visited_nodes.add(new_node)
             # 양방향 간선 모두 저장
            visited_edges.add((current_node, new_node))
            visited_edges.add((new_node, current_node)) 
            current_node = new_node  # 현재 위치 업데이트

    return answer
