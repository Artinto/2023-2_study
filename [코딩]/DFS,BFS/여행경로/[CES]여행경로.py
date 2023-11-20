# DFS를 사용
def solution(tickets):
    answer = []
    # 빈 리스트를 answer변수로 생성
    visited = [False]*len(tickets)
    # tickets의 길이만큼 모두 False로 채워진 visited변수 생성
    
    def dfs(airport, path):
        if len(path) == len(tickets)+1:
        # path의 길이와 tickets의 길이 +1이 같으면
            answer.append(path)
            # answer에 path를 추가
            return
        
        for idx, ticket in enumerate(tickets):
        # tickets의 값을 idex와 ticket값에 각각 대입
            if airport == ticket[0] and visited[idx] == False:
            # airport와 ticket의 첫번째 index값이 같고 idx가 아직 방문되지 않았다면
                visited[idx] = True
                # idx 방문 표시
                dfs(ticket[1], path+[ticket[1]])
                # 다음 경우
                visited[idx] = False
                # 아직 방문하지 않았기 때문에 False로 고정
        
        
    dfs("ICN", ["ICN"])
    # 무조건 처음 airport는 ICN이기 때문에 고정
    
    answer.sort()
    # 알파벳 순으로 정렬해야하기 때문에 sort를 이용해 오름차순 정렬

    return answer[0]
