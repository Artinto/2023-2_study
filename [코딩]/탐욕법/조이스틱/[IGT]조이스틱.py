def solution(name):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alp_idx = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,12,11,10,9,8,7,6,5,4,3,2,1]
    answer = -1
    idx = 0
    while (idx != len(name)):
        if name[idx] != 'A':
            answer += alp_idx[alphabet.index(name[idx])]
        elif name[idx] == 'A': # name = "...XA..." / X : name[idx-1]
            n = idx
            while (n+1 != len(name)) and (name[n] == 'A'):
                n += 1
            if (name[n] == 'A'): # name = "...XA...A" / X : name[idx-1]
                break
                
            # name = "...XA...Y..." / X : name[idx-1], Y : name[n]
            if ((idx-1) + (len(name)-n)) < (n - (idx-1)): # 왼쪽으로 이동
                answer += idx-1
                for j in range(len(name)-1,n-1,-1):
                    answer += alp_idx[alphabet.index(name[j])]
                answer += len(name)-n
                break
            else: # 오른쪽으로 이동
                True
        idx += 1
        answer += 1
    return answer

## 오른쪽으로만 진행
## 첫 번째 A가 나오는 순간 if문
## 첫 번째 A 이후 A가 아닌 문자가 나올 때를 기점으로
## (...XA...Y...)
## 1) X에서 왼쪽으로 출발해서 Y까지 도달할 때(end)
##    (조이스틱을 좌우로 움직이는 횟수는, idx(X) + idx(X) + (len(name)-idx(Y)))
## 2) X에서 오른쪽으로 출발해서 Y까지 도달할 때
## 2-1) Y가 마지막 문자가 아닌 경우 다시 처음으로 돌아감
