def solution(n, lost, reserve):
    answer = 0
    set_reserve = set(reserve) - set(lost) 
    set_lost = set(lost) - set(reserve)
# ㄴ여벌 체육복을 가져온 사람이 도난 당한 경우를 적용
    for i in list(set_reserve): # 여벌 체육복이 있는 사람의
        if i-1 in set_lost: # 앞 사람이 체육복을 도난당했다면
            set_lost.remove(i-1) # 체육복을 빌려줌
        elif i+1 in set_lost: # 해당 학생이 이미 체육복이 있고 뒷 사람이 체유복을 도난당했다면
            set_lost.remove(i+1) # 뒷 사람에게 빌려줌
    answer = n - len(set_lost) # 총 인원 중 끝까지 체육복 없는 인원 제외
    return answer
