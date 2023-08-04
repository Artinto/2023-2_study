def solution(clothes):
    answer = 1 
    closet = dict() #해시 생성
    cloth_case = [] # 각 의상 종류 별 개수를 저장할 리스트
    for name, case in clothes: # ex) ["yellowhat", "headgear"] 
        if case in closet: # 이전에 나온 종류면
            closet[case].append(name) #리스트에 추가
        else: # 처음 나온 종류면
            closet[case] = [name] # 새로운 리스트 생성
    for key in closet.keys(): #각 의상 종류마다
        cloth_case.append(len(closet[key])) # 해당 종류의 개수를 cloth_case에 추가
    for i in cloth_case: # 각 의상 종류마다
        answer *= (i+1) # (해당 종류의 옷을 입을지 안입을지 + 아무것도 안입는 경우의 수)를 경우의 수에 곱해줌
    answer -= 1 # 아무도 안입는 경우는 빼줘야 하므로 -1
    return answer
