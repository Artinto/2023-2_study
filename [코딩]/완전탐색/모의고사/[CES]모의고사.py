def solution(answers):
    answer = []
    
    lis =[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3 ,1 ,1 ,2 ,2 ,4 ,4 ,5 ,5]]
    
    cnt = [0] * 3
    
    for i in range(len(answers)):
        if answers[i] == lis[0][i % len(lis[0])]: 
            cnt[0] += 1
        if answers[i] == lis[1][i % len(lis[1])]:
            cnt[1] += 1
        if answers[i] == lis[2][i % len(lis[2])]:
            cnt[2] += 1
    
    winner = max(cnt)
    
    for i in range(len(cnt)):
        if cnt[i] == winner:
            answer.append(i+1)
        
    return answer
