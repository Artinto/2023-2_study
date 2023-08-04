# clothes 리스트의 각 아이템을 루프하면서 옷 이름과 종류를 변수 clothe와 type로 받음
def solution(clothes):
    hash_map = {}
    # hash_map은 각 옷 종류를 키로 가지고, 해당 종류의 개수를 값으로 가지는 딕셔너리
    for clothe, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1
        # hash_map에 해당 종류의 옷이 이미 존재한다면, 해당 종류의 값에 1을 더한다
    answer = 1
    # 결과값을 저장할 answer변수를 1로 초기화
    for type in hash_map: 
        # 각 옷 종류별로 루프를 돌면서 해당 종류의 옷을 입거나 입지 않는 경우를 고려하여 경우의 수를 계산
        answer *= (hash_map[type] + 1)
    # 각 종류별로 옷을 입을 경우와 입지 않을 경우를 고려하여 (해당 종류의 개수 + 1)을 answer에 곱함
    return answer - 1
# 모든 종류의 옷을 입지 않는 경우 제외
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
