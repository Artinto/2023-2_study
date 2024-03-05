from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(information, queries):
    # 결과 값을 저장할 list
    answer = []
    # 정보를 저장할 dictionary, key는 조건, value는 점수 list
    dic = defaultdict(list)
    
    # 모든 정보를 순회
    for info in information:
        info = info.split()  # 정보를 분리
        condition = info[:-1]  # 마지막 점수를 제외한 조건
        score = int(info[-1])  # 점수

        # 조건을 바탕으로 모든 경우의 수를 생성
        for i in range(5):
            case = list(combinations([0,1,2,3], i))
            for c in case:
                tmp = condition.copy()
                # 생성된 경우의 수에 따라 조건을 바꿈
                for idx in c:
                    tmp[idx] = "-"
                key = ''.join(tmp)
                dic[key].append(score)  # 바뀐 조건을 dictionary에 추가

    # dictionary에 저장된 점수를 오름차순으로 정렬
    for value in dic.values():
        value.sort()   

    # 모든 쿼리를 순회
    for query in queries:
        query = query.replace("and ", "")
        query = query.split()
        target_key = ''.join(query[:-1])  # 쿼리에서 점수를 제외한 조건
        target_score = int(query[-1])  # 쿼리에서 점수
        count = 0
        # 쿼리의 조건이 dictionary에 존재하면
        if target_key in dic:
            target_list = dic[target_key]
            # binary search를 이용해 target_score 이상인 첫 번째 원소의 위치를 찾고,
            # 그 위치부터 끝까지가 target_score 이상인 점수의 개수
            idx = bisect_left(target_list, target_score)
            count = len(target_list) - idx
        # 해당 조건을 만족하는 사람의 수를 answer에 추가
        answer.append(count)      
    return answer  # 결과 반환
