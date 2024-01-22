def solution(s):
    answer = []
    s = s[2:-2] # 맨 앞 대괄호 2개와, 맨 뒤 대괄호 2개 제거
    s = s.split("},{") # 대괄호 제외하여 문자 나누기
    s.sort(key = len) # 길이가 짧은 순서대로 정렬
    for i in s:
        num = i.split(',') # 한 튜플 내 여러 숫자 제거
        for j in num:
            if int(j) not in answer: # answer에 없는 숫자 추가
                answer.append(int(j))
    return answer
