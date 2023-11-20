from collections import defaultdict as dd
def solution(tickets):
    D = dd(list)
    for a,b in sorted(tickets):
        D[a].append(b)
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
            # 0을 return하는 조건 : n != 0 임에도 len(T[leave])가 0 이거나 T[leave] 안의 모든 경우의 수에 대해 temp == 0 인 경우(갈 수 있는 곳이 없음)
    else:
        return []
