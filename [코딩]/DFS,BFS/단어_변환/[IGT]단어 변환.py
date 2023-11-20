def solution(begin, target, words):
    ans, l, begin = 0, len(begin), [begin]
    while (target not in begin) and begin:
        L, C = list(), list()
        for W in words:
            for B in begin:
                n = 0
                for b,w in zip(B,W):
                    if b == w:
                        n += 1
                if l - n == 1:
                    L.append(W)
                    break
            else:
                C.append(W)
        begin, words = L[:], C[:]
        ans += 1
    return ans if target in begin else 0
