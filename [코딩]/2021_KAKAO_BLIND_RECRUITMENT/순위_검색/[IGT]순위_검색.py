from collections import defaultdict as dd
from bisect import bisect_left
def solution(info, query):
    answer = []
    score = dd(list)
    for i in info:
        I = i.split()
        for a in [I[0],'-']:
            for b in [I[1],'-']:
                for c in [I[2],'-']:
                    for d in [I[3],'-']:
                        score[a+b+c+d] += [int(I[4])]
    for value in score.values():
        value.sort()  
    for q in query:
        Q,S = q.replace(' and ','').split()
        if Q in score:
            target = int(S)
            n = len(score[Q])
            idx = bisect_left(score[Q],target)
            answer += [n-idx]
        else:
            answer += [0]
    return answer
