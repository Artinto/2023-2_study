def solution(people, limit):
    people.sort() ## [50,50,70,80]
    i = 0
    j = len(people) - 1
    answer = 0
    while (i < j):
        if (people[i] + people[j] <= limit): # 두 사람이 탈 수 있는가?
            answer += 1
            i += 1
            j -= 1
        else:
            answer += 1
            j -= 1
        if i == j: # 혼자 남게 된 경우
            answer += 1
            break
    return answer



def solution(people, limit):
    people.sort()
    i = 0
    j = len(people) - 1
    answer = 0
    while (i <= j):
        if (people[i] + people[j] <= limit):
            i += 1
        answer += 1
        j -= 1
    return answer
