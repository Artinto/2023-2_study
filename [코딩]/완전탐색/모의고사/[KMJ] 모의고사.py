def solution(answers):
    answer = []
    correct = [0, 0, 0]
    pers1 = [1, 2, 3, 4, 5]
    pers2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pers3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for idx, val in enumerate(answers):
        # print(idx, val)
        if pers1[idx%5] == val:
            correct[0] += 1
        if pers2[idx%8] == val:
            correct[1] += 1
        if pers3[idx%10] == val:
            correct[2] += 1
            
    for pers, count in enumerate(correct):
        if correct == max(correct):
            answer.append(pers+1)  
    return answer
