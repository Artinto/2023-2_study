def solution(priorities, location):
    answer = 0

    while True:
        high = max(priorities) # 헌재 우선순위가 가장 높은 수
        first = priorities.pop(0)
        if high == first: #우선순위가 높은 숫자가 가장 앞으로 정렬되어 있다면
            answer += 1 # 프로세스 실행
            if location == 0: # 원하는 숫자 = 현재 우선순위가 가장 높은 숫자 중 왼쪽에 있는 숫자
                break # 코드 종료
            else:
                location -= 1 
        else: # 프로세스를 실행할 수 없는 상황 -> 우선순위가 높은 숫자를 앞으로 정렬
            priorities.append(first) # 가장 앞에 있는 숫자를 가장 뒤로 정렬
            # 맨앞에 있던 숫자가 뒤로 갔으므로, 원하는 숫자는 위치가 하나 앞으로 당겨짐
            if location == 0: # lacation이 0이면 location -= 1 하면 음수가 되므로
                location = len(priorities)-1
            else:
                location -= 1
    return answer
