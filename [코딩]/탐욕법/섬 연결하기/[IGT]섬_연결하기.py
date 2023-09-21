def solution(n, costs):
    costs.sort(key=lambda x:x[2]) ## cost를 기준으로 오름차순 정렬
    connect = {costs[0][0],costs[0][1]}
    ## cost가 낮은 다리부터 건설, 다리가 건설되어 서로 연결된 섬들은 connect set에 추가
    ## 처음에는 cost가 제일 낮은 다리부터 건설한다고 가정, 그 다리에 연결된 두 섬을 set에 추가
    answer = costs[0][2]
    idx = 1
    etc = []
    while (len(connect) != n): ## 모든 섬들이 연결될 때까지
        i = costs[idx]
        s = {i[0],i[1]}
        if len(s & connect) == 1:
        ## 교집합 성분(섬)이 하나 -> 해당 섬을 최소 cost로 연결시키기 위해서 반드시 건설해야 하는 다리
            connect = connect|s
            answer += i[2]
            if etc != []: ## 다리를 새로 건설하는 과정에서 만약 보류된 다리가 있을 경우
                for j in reversed(etc):
                    costs.insert(idx+1,j)
                    ## 보류된 다리들을 cost가 낮은 순서로 끼워넣기(cost가 높은 순서부터 넣어야 함)
        elif len(s & connect) == 0:
        ## 교집합이 0집합 -> cost 가성비를 섣불리 판단할 수 없으므로 보류(etc)
            etc.append(i)
        idx += 1
    return answer
