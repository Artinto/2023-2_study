def solution(participant, completion):
    dic = {}
    sum = 0
    for i in participant:
        dic[hash(i)] = i
        sum += hash(i)
    for j in completion:
        sum -= hash(j)
    answer = dic[sum]
    return answer
