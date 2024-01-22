from itertools import permutations #순열 라이브러리
    
def check(user, ban):
    if len(user) != len(ban): # 우선 길이 비교
        return False
    else: # 길이가 같은 단어라면
        for i, j in zip(user, ban): # 단어 내 철자 비교
            if j == '*': # 암호화 된 철자는 지나감
                continue
            if i != j: # 나머지 철자들 중 다른 글자가 있다면 다른 아이디
                return False
        return True
        
def solution(user_id, banned_id):
    answer = []
    
    for i in permutations(user_id, len(banned_id)): 
        count = 0
        for a, b in zip(i, banned_id): 
            if check(a, b): # check 함수 결과 불량사용자면
                count += 1 # count +1
                
        if count == len(banned_id): # count 된 숫자가 불량사용자 수와 같고
            if set(i) not in answer: # 그 조합이 답에 아직 없다면
                answer.append(set(i)) # 답 추가
    
    return len(answer)
