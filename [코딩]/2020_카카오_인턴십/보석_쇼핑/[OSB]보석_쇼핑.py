# 10번까지 정답
from itertools import combinations_with_replacement
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
gem_category = set(gems)
min_length = float('inf')  # 현재까지의 최소 구간 길이

combis = combinations_with_replacement(for_combi_list, 2) # 중복을 포함해서 뽑기.
answer = []
for combi in  combis:
    idx1, idx2 = combi[0], combi[1] 
    try_set = gems[idx1-1:idx2] # 0:0, 1:1 은 안되므로 포함.
    if len(try_set) == len(gem_category): # 만약 종류별로 다샀다면 answer에 추가
        length = idx2-idx1+1
        if min_length > length: # 최소 길이가 갱신되면
            min_length = length
            answer = [idx1, idx2+1]
        break
print(answer)

# 15번까지 정답 but 활용성 점수 0
def solution(gems): 
    gem_category = set(gems)
    gem_num = len(gem_category)
    min_length = float('inf')  # 현재까지의 최소 구간 길이

    answer = []
    for left in range(len(gems)):
        temp = set()
        for right in range(left, len(gems)):
            temp.add(gems[right])
            if len(temp) == gem_num: # 보석의 수가 같고
                if right - left < min_length: # 최소 길이라면
                    min_length = right - left # 업데이트
                    answer = [left+1, right+1]  # 인덱스가 1부터 시작.
                break # 굳이 뒤까지 탐색 X
    return answer

# 투 포인터로 해결 가능.