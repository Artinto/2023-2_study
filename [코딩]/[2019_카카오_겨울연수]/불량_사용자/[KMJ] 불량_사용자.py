from itertools import permutations

def check(user, banned_id):
    for u, b in zip(user, banned_id):
        if len(u) != len(b): # 유저와 밴 아이디의 길이가 다르면 제제 대상이 아님
            return False

        for i in range(len(u)):
            if u[i] != b[i] and b[i] != '*': # *이 아닌 단어가 다르면 제제 대상이 아님
                return False
    return True # 둘을 제외한 경우는 제제대상이 될 수 있음

def solution(user_id, banned_id):
    answer = []
    candidates = list(permutations(user_id, len(banned_id))) # 모든 조합 list

    for candidate in candidates:
        if check(candidate, banned_id): # check를 통과했는데 True면
            candidate = sorted(candidate) # 중복제거
            if candidate not in answer: # 정답에 없으면
                answer.append(candidate) # 정답에 추가

    return len(answer)
