def solution(gems):
    L = R = 0
    D = dict.fromkeys(gems,0)
    ans = [len(gems)+1]
    for idx,g in enumerate(gems):
        D[g] += 1
        if all(D.values()):
            R = idx
            while all(D.values()):
                D[gems[L]] -= 1
                L += 1
            if R-L+2 < ans[0]:
                ans = [R-L+2,L,R+1]
    return ans[1:]

################################################

from collections import defaultdict as dd
def solution(gems):
    L = R = 0
    D = dd(int)
    n = len(set(gems))
    ans = [100001]
    for idx,g in enumerate(gems):
        D[g] += 1
        if len(D) == n:
            R = idx
            while len(D) == n:
                x = gems[L]
                D[x] -= 1
                if D[x] == 0:
                    del D[x]
                L += 1
            if R-L+2 < ans[0]:
                ans = [R-L+2,L,R+1]
    return ans[1:]
