def solution(n, computers):
    answer = 0  
    visited = [0 for _ in range(n)]  # 각 컴퓨터가 방문된 상태를 저장
    for i in range(n):
        if visited[i] == 0: # 아직 방문하지 않았다면
            stack = [i]  # 방문할 컴퓨터들을 저장
            while stack: # 아직 방문하지 않은 컴퓨터가 있으면 계속 반복
                computer = stack.pop()  # 방문한 컴퓨터는 제거. 이 때 순간적으로 반복문 종료
                visited[computer] = 1  # 해당 컴퓨터를 방문했다고 표시
                for other_computer in range(n):
                    if computers[computer][other_computer] == 1 and visited[other_computer] == 0: # 현재 컴퓨터와 연결되어 있고, 아직 방문하지 않은 컴퓨터가 있으면
                        stack.append(other_computer)  # 스택에 추가-> 다시 while 문이 돌게 됨
            answer += 1
    return answer
