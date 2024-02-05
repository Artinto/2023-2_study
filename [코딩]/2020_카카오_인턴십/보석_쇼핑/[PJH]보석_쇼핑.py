def solution(gems):
    size = len(set(gems))  # 보석의 종류 수
    dic = {gems[0]: 1}  # 첫 번째 보석
    temp = [0, len(gems) - 1]  # 현재의 보석 범위
    start, end = 0, 0

    while end < len(gems) and start < len(gems):
        if len(dic) == size:  # 모든 종류의 보석이 포함된 경우
            if end - start < temp[1] - temp[0]:  # 현재 범위가 더 짧은 경우
                temp = [start, end]
            if dic[gems[start]] == 1:  # start에 위치한 보석이 한 개라면 삭제
                del dic[gems[start]]
            else:  # 그렇지 않다면 보석 수를 하나 감소
                dic[gems[start]] -= 1
            start += 1  # start를 오른쪽으로 한 칸 이동

        else:  # 모든 종류의 보석이 포함되지 않은 경우
            end += 1  # end를 오른쪽으로 한 칸 이동
            if end == len(gems):  # 범위를 벗어나면 종료
                break
            if gems[end] in dic.keys():  # 이미 포함된 보석이라면 수를 하나 증가
                dic[gems[end]] += 1
            else:  # 새로운 종류의 보석이라면 딕셔너리에 추가
                dic[gems[end]] = 1

    return [temp[0] + 1, temp[1] + 1]  # 진열대 번호는 1부터 시작하므로 1을 더해줌
