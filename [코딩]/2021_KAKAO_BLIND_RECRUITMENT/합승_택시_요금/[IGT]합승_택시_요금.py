import heapq
def solution(n, s, a, b, fares):
    ans = []
    route = [[] for _ in range(n+1)]
    for x,y,z in fares:
        route[x] += [(z,y)]
        route[y] += [(z,x)]
    for start in [s,a,b]:
        H = [(0,start)]
        dist = [float("inf")]*(n+1)
        dist[start] = 0
        while H:
            now_cost,now_node = heapq.heappop(H)
            if dist[now_node] >= now_cost:
                for next_cost,next_node in route[now_node]:
                    total_cost = now_cost + next_cost
                    if total_cost < dist[next_node]:
                        dist[next_node] = total_cost
                        heapq.heappush(H,(total_cost,next_node))
        ans += [dist]
    return min(x+y+z for (x,y,z) in zip(*ans))
