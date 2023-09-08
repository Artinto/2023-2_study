from itertools import permutations
def solution(k, dungeons):
    dungeons.sort(reverse=True) # 최소 필요도 순으로 정렬.
    len_dun=len(dungeons)
    temp_list = [str(i) for i in range(len_dun)]
    try_list = list(permutations(temp_list, len_dun))
    answer_list = []
    for sequence in try_list:
        answer = 0
        status = k
        for index in sequence:
            index = int(index)
            if status >= dungeons[index][0]: # 가능?
                status-=dungeons[index][1] # 던전 돌기
                answer+=1
        answer_list.append(answer)
    return max(answer_list)
