def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x:x[2])
    island = set([costs[0][0], costs[0][1]])
    print(costs)
    answer = costs[0][2]
    while len(island)!=n:
        for i in range(1, len(costs)):    
            if costs[i][0] in island and costs[i][1] in island:
                continue
            if costs[i][0] in island or costs[i][1] in island:
                island.update([costs[i][0], costs[i][1]])
                answer += costs[i][2]
                break
    return answer
