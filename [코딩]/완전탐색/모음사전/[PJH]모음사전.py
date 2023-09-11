from itertools import product

def solution(word):
    answer = 0
    arr = []
    l1=['A','E','I','O','U']
    
    for r in range(1, 6): 
        for i in product(l1, repeat=r): 
            arr.append(''.join(i))
    
    arr.sort()
    
    for a in arr:
        if word == a:
            break
        answer += 1
    
    return answer+1
