def solution(answers):
    len_answer = len(answers)
    answer = []
    index = 0
    per1=[1,2,3,4,5] # 5반복
    per2=[2,1,2,3,2,4,2,5] # 8반복
    per3=[3,3,1,1,2,2,4,4,5,5] # 10반복
    scores = [0,0,0]
    while len_answer:
        if per1[index%len(per1)] == answers[index]:
            scores[0] +=1
        if per2[index%len(per2)] == answers[index]:
            scores[1] +=1
        if per3[index%len(per3)] == answers[index]:
            scores[2] +=1
        index += 1
        len_answer-=1
    max_score = max(scores)
    for index, score in enumerate(scores):
        if score == max_score:
            answer.append(index+1)
    return answer
