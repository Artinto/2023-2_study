def solution(expression):
    n,num,operator = '',list(),list()
    ans = 0
    for e in expression:
        if e.isdigit():
            n += e
        else:
            num += [int(n)]
            operator += [e]
            n = ''
    num += [int(n)]
    for P in [('+','-','*'),('+','*','-'),('-','+','*'),('-','*','+'),('*','+','-'),('*','-','+')]:
        N,O = num[:],operator[:]
        for p in P:
            while p in O:
                idx = O.index(p)
                if p == '+':
                    N[idx] += N[idx+1]
                elif p == '-':
                    N[idx] -= N[idx+1]
                else:
                    N[idx] *= N[idx+1]
                del N[idx+1]
                del O[idx]
        ans = max(ans,abs(N[0]))
    return ans
