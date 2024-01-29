def solution(priorities, location):
    # 작업의 우선순위, 현재 작업의 위치 입력 받음
    queue =  [(i,p) for i,p in enumerate(priorities)]
    # 인덱스, 우선순위 튜플을 담는 리스트
    # enumerate를 통해 priorities 리스트의 각 원소에 대해 인덱스와 함꼐 튜플을 생성하여 queue 리스트 저장
    answer = 0
    # 최종 반환할 결과 값인 answer을 0으로 초기화
    while True:
        # 무한루프 시작
        cur = queue.pop(0)
        # queue 리스트의 맨 앞에서 작업을 꺼내서 cur 변수에 저장
        if any(cur[1] < q[1] for q in queue):
            # 현재 작업의 우선순위와 큐에 남아있는 작업들의 우선순위 비교
            queue.append(cur)
            # 현재 작업의 우선순위보다 더 높은 우선순위를 가진 작업이 있는 큐의 경우 현재 작업을 다시 큐의 맨 뒤에 추가
        else:
            # 그게 아니라면
            answer += 1
            # 작업처리 가능하기 때문에 누적하여 1을 더함
            if cur[0] == location:
                # 현재 작업의 인덱스가 원하는 위치와 일치하다면
                return answer
