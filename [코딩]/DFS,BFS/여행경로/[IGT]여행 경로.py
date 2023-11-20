from collections import defaultdict as dd
def solution(tickets):
    D = dd(list)
    for a,b in sorted(tickets):
        D[a].append(b)
    print(D)
    return ["ICN"] + DFS("ICN",D,len(tickets))

def DFS(leave,T,n):
    if n:
        for i in range(len(T[leave])):
            arrive = T[leave].pop(0)
            temp = DFS(arrive,T,n-1)
            if temp != 0:
                return [arrive] + temp
            T[leave].append(arrive)
        else:
            return 0
    else:
        return []
