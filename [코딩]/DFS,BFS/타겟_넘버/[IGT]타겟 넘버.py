def solution(numbers, target):
    N = [0]
    for num in numbers:
        nn = []
        for n in N:
            nn.append(n + num)
            nn.append(n - num)
        N = nn
    return N.count(target)

'''
[4,1,2,1] >> 4

      +4                -4
  +1      -1        +1      -1
+2  -2  +2  -2    +2  -2  +2  -2
'''
