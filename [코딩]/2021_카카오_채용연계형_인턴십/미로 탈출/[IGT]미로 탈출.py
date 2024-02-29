import heapq
def solution(n, start, end, roads, traps):
    len_traps = len(traps)
    traps_idx = {traps[i]:i for i in range(len_traps)}
    traps = set(traps) # time complexity of "() in ()" : set(O(1)) < list(O(n))
    bin_n = 2**len_traps
    time = [[] for _ in range(n+1)]
    for a,b,c in roads:
        time[a] += [(c,b,False)] # forward
        time[b] += [(c,a,True)] # backward
    dist = [[float("inf")]*bin_n for _ in range(n+1)]
    dist[start][0] = 0
    H = [(0,start,0)]
    while H:
        time_1,node_1,d = heapq.heappop(H)
        if node_1 == end:
            return time_1
        b = format(d,'b').zfill(len_traps)
        tnf_1 = (node_1 in traps and b[-1-traps_idx[node_1]] == '1') # (node is not in traps) or (node is in traps but don't work) >> True
        for time_2,node_2,tnf in time[node_1]:
            tnf_2 = (node_2 in traps and b[-1-traps_idx[node_2]] == '1')
            if tnf_1 ^ tnf_2 != tnf:
                continue
            else:
                t = time_1 + time_2
                if dist[node_2][d] > t:
                    dist[node_2][d] = t
                    if node_2 in traps:
                        x = traps_idx[node_2]
                        if b[-1-x] == '1':
                            D = d - 2**x
                        else:
                            D = d + 2**x
                    else:
                        D = d
                    heapq.heappush(H,(t,node_2,D))
