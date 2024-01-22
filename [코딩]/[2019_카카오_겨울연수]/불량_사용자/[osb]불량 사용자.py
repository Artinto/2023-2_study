from itertools import permutations, combinations

def match(user, ban):
    if len(user) != len(ban): # 길이가 다르다면
        return False
    for i in range(len(user)):
        if ban[i] == '*': 
            continue
        elif ban[i] != user[i]: # 문자가 다르다면
            return False
    return True

def solution(user_id, banned_id):
    possible_names = [] # 경우의 수를 구하기 위해서 저장하는 이름들
    for ban_id in banned_id:
        possible_name = [] # 해당 밴 아이뒤에서 가능한 이름들 저장.
        for id in user_id:
            if match(id, ban_id):
                possible_name.append(id)
        possible_names.append(possible_name) # 이름 추가.
    permuts = list(permutations(user_id, len(banned_id))) # 4개를 뽑을 수 있는 모든 경우의 수
    answer = set() # 중복 제거를 위해 집합으로 선언
    
    # 각 4개 뽑은 것으로 가능한지 불가능 한지 판단 후 중복 제거.
    for permut in permuts:
        temp = True
        for idx, val in enumerate(permut):
            if val not in possible_names[idx]: # 만약 없으면, 다음 순열로 이동
                temp = False
                break
        if temp:
            answer.add(tuple(sorted(permut))) # 중복 제거를 위해서 sort 후 추가
    print(answer)
    return len(answer)