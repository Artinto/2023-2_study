from itertools import permutations # 순열

def solution(k, dungeons):
    answer = 0
    for i in permutations(dungeons,len(dungeons)): # 던전의 요소들을 던전의 길이의 순열들로 만든 후 반복
        current_fatigue = k 
        cnt = 0
        for need_fatigue, used_fatigue in i: # 만들어진 순열들 내에서 반복
          if current_fatigue >= need_fatigue:
            current_fatigue -= used_fatigue
            cnt += 1
        answer = max(answer,cnt) # 던전을 도는 횟수의 최대값이 갱신될 때마다 적용
    return answer
