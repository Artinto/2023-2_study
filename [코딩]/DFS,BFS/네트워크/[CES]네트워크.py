def solution(n, computers):
    answer = 0  
    visited = [0 for _ in range(n)] 
    # 방문 상태를 변수 visited에 저장
    for i in range(n):
    # n-1만큼 반복문 실행
        if visited[i] == 0:
        # visited의 값이 0이라면 아직 방문하지 않았다는 뜻
            stack = [i] 
            # 방문할 컴퓨터들을 stack에 넣어줌
            while stack: 
            # stack이 남아있다면 while 루프를 통해 계속 반복
                computer = stack.pop()
                # pop함수를 사용해 뒤에서부터 방문한 컴퓨터 제거해주고 computer에 저장
                visited[computer] = 1
                # 방문 컴퓨터 방문 표시
                for other_computer in range(n):
                # n-1만큼 other_computer에 넣어주면서 반복문 실행
                    if computers[computer][other_computer] == 1 and visited[other_computer] == 0: 
                        stack.append(other_computer)  
            answer += 1
    return answer
