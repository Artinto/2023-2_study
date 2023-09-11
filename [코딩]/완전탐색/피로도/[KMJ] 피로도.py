from itertools import permutations

def solution(k, dungeons):
    answer = -1
    cases = list(permutations(dungeons, len(dungeons)))
    for i in cases:
        limit = k
        count = 0
        for need, consume in i:
            if limit >= need:
                limit -= consume
                count += 1
            else:
                break
        answer = max(answer, count)
    return answer
