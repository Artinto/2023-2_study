def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    # 여벌의 체육복이 있는 학생도 도난 당했을 수도 있다!
    new_reserve = set(reserve) - set(lost)
    # 여벌의 체육복이 있는 학생이 도난당했으면 빌려줄 수 있는 리스트에서 제외
    for i in new_reserve:
        # new_reserve의 원소들을 하나씩 i에 대입하면서 반복
        if i-1 in new_lost:
            # new_lost안에 i-1한 값이 있으면
            new_lost.remove(i-1)
            # new_lost(i-1)원소 제거 (중복 방지)
        elif i+1 in new_lost:
            # new_lost안에 i-1한 값이 있으면
            new_lost.remove(i+1)
            # new_lost(i+1)원소 제거 (중복 방지)
    return n - len(new_lost)
    # 전체 인원수에서 남은 체육복 없는 사람 제거
