def solution(people, limit):
    people.sort() # 몸무게 순으로 정렬
    answer = 0
    i, j = 0, len(people) - 1

    while i <= j:
        if people[i] + people[j] <= limit: # 가장 가벼운 사람과 가장 무거운 사람을 같이 태울 수 있다면,
            i += 1
        j -= 1
        answer += 1

    return answer
