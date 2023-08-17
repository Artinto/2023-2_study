def solution(priorities, location):
    answer = 0  # 실행 순서를 저장할 변수 초기화
    queue = [(i, p) for i, p in enumerate(priorities)]  # 프로세스의 위치와 우선순위를 함께 저장하는 새로운 큐 생성

    # 큐가 빌 때까지 반복
    while queue:
        current = queue.pop(0)  # 현재 프로세스를 큐에서 꺼냄
        
        # 꺼낸 프로세스보다 우선순위가 높은 프로세스가 있다면
        if any(current[1] < item[1] for item in queue):
            queue.append(current)  # 꺼낸 프로세스를 다시 큐에 넣음
        else:
            answer += 1  # 프로세스를 실행하고 answer 값을 1 증가시킴
            
            # 실행한 프로세스의 위치가 location과 같다면 반복문 종료
            if current[0] == location:
                break

    return answer  # 실행 순서를 반환
