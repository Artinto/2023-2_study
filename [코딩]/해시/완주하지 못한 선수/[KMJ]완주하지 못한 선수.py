# 해쉬 함수 사용 -> 효율성테스트 초과
def solution(participant, completion):
    dic = {} # 딕셔너리 사용
    sum = 0
    for i in participant:
        dic[hash(i)] = i #해쉬함수를 사용해서 참여자 추가
        sum += hash(i)
    for j in completion:
        sum -= hash(j) #해쉬함수를 사용해서 완주자 제거
    answer = dic[sum]
    return answer


# 리스트 사용 -> 시간 초과
def solution(participant, completion):
    name_list = [] # 명단 리스트
    for i in participant:
        name_list.append(i) # 참여자 추가
    for j in completion:
        name_list.remove(j) # 완주자 제거
    answer = name_list[0] # name_list 안에 있는 사람이 완주하지 못한 사람
    return answer
