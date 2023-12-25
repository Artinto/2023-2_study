def solution(n, results):
    win, lose = [set() for _ in range(n+1)], [set() for _ in range(n+1)]
    for a,b in results:
        win[a].add(b)
        lose[b].add(a)
    for x in range(1,n+1):
        for w in lose[x]:
            win[w].update(win[x])
        for l in win[x]:
            lose[l].update(lose[x])
    return sum((len(win[i])+len(lose[i]) == n-1) for i in range(1,n+1))
