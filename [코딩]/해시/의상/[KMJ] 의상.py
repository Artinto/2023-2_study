def solution(clothes):
    answer = 1 # 나중에 곱해야하기 때문에 1로 초기화
    
    dict = {}
    # [["의상이름", "종류"],["의상이름","종류"]]로 clothes가 존재
    # {"종류":"의상이름"}형태의 딕셔너리로 저장
    
    # 딕셔너리 형태로 저장
    for dress in clothes:
        key = dress[1] # 종류를 key값으로 저장
        value = dress[0] # 의상이름을 value로 저장
        if key in dict: # 딕셔너리에 이미 있는 종류면
            dict[key].append(value) # 그 종류가 있는 곳에 value값으로 저장
        else: # 새로운 종류면
            dict[key] = [value] # key값을 추가하고 value값으로 저장
            
    # 조합 계산
    # (첫 번째 종류 의상 개수 + 1) * ... * (마지막 종류 의상 개수 +1) - 1
    for key in dict.keys(): #의상 종류를 하나씩 불러오기
        answer = answer*(len(dict[key])+1)
        # len(dict[key]) == 해당 의상 종류의 개수 (해당 key값 안에 있는 value의 개수)
    answer -= 1
    # 곱셈이 끝나고 - 1

    return answer
