def solution(gems):
    answer = []
    all_gems = len(set(gems)) # 보석의 종류수
    start, end = 0, 0 # 시작 진열대 번호, 끝 진열대 번호
    gemdict = {} # 보석 종류별로 개수를 셀 딕셔너리

    result = len(gems)+1 # 정답에 해당하는 구간

    while end < len(gems): # 진열대 안에 있을 때까지만 검사 진행

        if gems[end] not in gemdict: # 새로 발견한 보석
            gemdict[gems[end]] = 1
        else: # 기존에 존재하는 보석
            gemdict[gems[end]] += 1

        end += 1 #보석을 새로 추가했으니 end칸 한 칸 뒤로

        if len(gemdict) == all_gems: # 범위안에 모든 보석이 존재할 때
            while start < end:
                if gemdict[gems[start]] > 1:  # 하나 이상 존재하면 뒤에도 더 존재한다는 뜻이므로
                    gemdict[gems[start]] -= 1  # 하나를 제거해주고
                    start += 1  # start칸을 뒤로 한칸 이동
                elif end-start < result: # 지정한 구간보다 현재 구간이 짧으면
                    result = end-start # 지정한 구간 바꿔주기
                    answer = [start+1, end]
                    break
                else:
                    break

    return answer
