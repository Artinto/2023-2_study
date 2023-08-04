def solution(clothes):
    # 딕셔너리를 사용하여 의상의 종류를 키로, 해당 종류에 속하는 의상 이름들을 값으로 저장
    clothes_dict = {}
    for name, kind in clothes:
        # 만약 해당 종류가 clothes_dict에 없으면, 새로운 키로 추가하고 해당 의상 이름을 값으로 설정
        if kind not in clothes_dict:
            clothes_dict[kind] = [name]
        # 만약 해당 종류가 clothes_dict에 이미 존재하면, 해당 종류의 값 리스트에 의상 이름을 추가
        else:
            clothes_dict[kind].append(name)
    
    # 각 의상 종류마다 (의상 개수 + 1)을 곱하여 경우의 수 계산
    # +1은 의상을 하나도 선택하지 않는 경우를 포함하기 위함
    answer = 1
    for kind in clothes_dict:
        answer *= (len(clothes_dict[kind]) + 1)
    
    # 모든 의상을 선택하지 않는 경우는 제외
    return answer - 1
