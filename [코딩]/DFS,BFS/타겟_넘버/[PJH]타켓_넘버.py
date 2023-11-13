import itertools

def solution(numbers, target):
    # numbers의 각 요소 x에 대해 (x, -x) 튜플을 만들어 리스트 l에 저장
    l = [(x, -x) for x in numbers]
    
    # itertools.product 함수를 이용해 l의 모든 요소들에 대한 데카르트 곱을 구하고,
    # 그 결과에 대해 sum 함수를 적용하여 각 조합의 합을 구한 후,
    # 이를 다시 리스트로 묶어 s에 저장
    s = list(map(sum, itertools.product(*l)))
    
    # 리스트 s에 있는 요소들 중 target과 같은 것의 개수를 반환
    return s.count(target)
