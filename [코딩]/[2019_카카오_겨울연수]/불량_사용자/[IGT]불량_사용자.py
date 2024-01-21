from itertools import permutations as p
def solution(user_id, banned_id):
    L = dict()
    ans = list()
    for b in set(banned_id):
        L[b] = list()
        for u in user_id:
            if len(b) == len(u):
                for x,y in zip(b,u):
                    if x!="*" and x!=y:
                        break
                else:
                    L[b] += [u]
    for s in p(range(len(user_id)),len(banned_id)):
        if sorted(s) not in ans:
            for i,j in enumerate(s):
                if user_id[j] not in L[banned_id[i]]:
                    break
            else:
                ans += [sorted(s)]
    return len(ans)
