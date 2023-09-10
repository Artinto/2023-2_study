# 순열을 구해주는 모듈
from intertools import permutations

def soltion(k, dungeons):
  # 반환 값인 answer를 0으로 초기화
    answer = 0
    # dungeons의 개수만큼 dungeons 수열 생성
    for p in permutations(dungeons, len(dungeons)):
        tmp = k
        cnt = 0
        
        for need, spend in p:
            if tmp >= need:
                tmp -= spend
                cnt += 1
        answer = max(answer, cnt)
    return answer
                
            
