from itertools import permutations

def solution(k, dungeons):
    max_count = 0
    for perm in permutations(dungeons):  # 모든 가능한 던전 조합에 대해 반복
        count = 0
        fatigue = k
        for dungeon in perm:   # 각 조합에서 던전을 하나씩 방문
            if fatigue >= dungeon[0]:  # 만약 현재 피로도가 해당 던전의 최소 필요 피로도보다 크거나 같다면,
                fatigue -= dungeon[1]   # 해당 던전의 소모 피로도만큼 피로도를 감소시키고,
                count += 1     # 방문한 던전 수를 증가
            else:   # 만약 현재 피로도가 해당 던전의 최소 필요 피로도보다 작다면,
                break   # 반복문을 종료
        max_count = max(max_count, count)   # 방문한 던이 최대값인지 확인하고, 그렇다면 값을 업데이트

    return max_count
