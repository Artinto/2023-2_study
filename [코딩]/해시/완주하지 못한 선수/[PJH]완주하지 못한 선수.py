def solution(participant, completion):
    # 각각의 배열 정렬
    participant.sort()
    completion.sort()

    # 완주한 선수명단의 크기만큼 for문을 돌려 확인
    for i in range(len(completion)):
        if participant[i] != completion[i] :
            return participant[i] # 완주한 선수 명 개수 만큼 안에서 일치 하지 않는 경우 그 사람을 미완주자로 선별
    
    return participant[-1] # 완주한 선수 명단 수 만큼 돌려도 없다면 이는 마지막 선수가 완주하지 못한 것으로 참가자 명단 마지막 선수를 반환
