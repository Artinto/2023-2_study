def solution(answers):
    answer = []
    
    lis =[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3 ,1 ,1 ,2 ,2 ,4 ,4 ,5 ,5]]
    
    cnt = [0] * 3
    
    for i in range(len(answers)):
        if answers[i] == lis[0][i % len(lis[0])]: # i % len(lis[0])은 lis[0]의 길이를 넘어서면 인덱스를 처음으로 돌려놓음, lis[i]안에 원소갯수를 기준으로 계속 반복되기 때문에 길이로 나누어 나머지값을 이용하여 튜플을 이용
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
