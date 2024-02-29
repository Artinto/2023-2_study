from collections import deque
def manhatan(p1, p2):
    x1,y1,x2,y2 = p1[0],p1[1], p2[0],p2[1]
    distance = abs(x1-x2)+abs(y1-y2)
    return distance

def solution(places):
    # 단어 분리.
    graphs = []
    p_room = []
    for place in places:
        graph = []
        p_list = []
        for idx1, room in enumerate(place):
            for idx2, d in enumerate(room):
                if d =='P':
                    p_list.append((idx2, idx1))
            temp = list(room)
            graph.append(temp)
        p_room.append(p_list)
        graphs.append(graph)
        
    def check_distance(graph, p_list):
        for p_idx, p in enumerate(p_list):
            for p_other in p_list[p_idx+1:]:
                distance = manhatan(p, p_other)
                if distance >2: # 2보다 크면 Pass
                    continue
                elif distance ==2:
                    # y축 거리가 2라면
                    if p[0] == p_other[0]:
                        new_y=  max(p[1], p_other[1])-1
                        if graph[new_y][p[0]] == 'X':
                            continue
                        else:
                            return 0 
                    elif p[1] == p_other[1]: # x축으로 거리가 2라면
                        new_x =  max(p[0], p_other[0])-1
                        if graph[p[1]][new_x] == 'X':
                            continue
                        else:
                            return 0 
                    else: # 대각선인 경우
                        if graph[p_other[1]][p[0]] == 'X' and graph[p[1]][p_other[0]] == 'X':
                            continue
                        else:
                            print(p, p_other)
                            return 0
                else:
                    
                    return 0
        return 1
    answer = []
    for room_idx, p_list in enumerate(p_room):
        graph = graphs[room_idx]
        temp = check_distance(graph, p_list)
        answer.append(temp)                    
    
    return answer