from collections import deque
# 덱 자료구조를 사용하기 위해 모듈을 가져온다.

def solution(begin, target, words):
    answer = 0
    q = deque()
    # 큐를 생성
    q.append([begin, 0])
    # 큐에 시작 단어와 0 (변환 횟수)를 포함하는 리스트 추가
    V = [ 0 for i in range(len(words))]
    # 방문 여부를 확인하는 V에 차례로 words안에 있는 단어의 개수를 i에 대입
    while q:
        # 큐가 비어있지 않으면
        word, cnt = q.popleft()
        # 큐에서 단어와 현재까지의 변환 횟수를 추출
        if word == target:
            answer = cnt
            break        
        for i in range(len(words)):
        # 각 단어에 대해 반복
            temp_cnt = 0
            if not V[i]:
            # 해당 단어가 아직 방문되지 않으면
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                    # 현재 비교 중인 위치에서 두 단어의 문자가 다르다면
                        temp_cnt += 1
                        # 차이가 발생한 횟수 1씩 증가
                if temp_cnt == 1:
                # 차이가 1이라면
                    q.append([words[i], cnt+1])
                    # 해당 단어와 변환 횟수를 큐에 추가
                    V[i] = 1
                    # 해당 단어를 방문했음을 표기
                    
    return answer
