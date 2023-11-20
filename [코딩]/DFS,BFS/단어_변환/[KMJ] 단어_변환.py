from collections import deque

def solution(begin, target, words):
    if target not in words: # target으로 갈 수 없다면
        return 0
    
    queue = deque()
    queue.append([begin, 0]) # 초기값 세팅 (바뀐 단어, 변환 횟수)
    
    while queue:
        now, step = queue.popleft() # 단어와 횟수 가져오기
        # while문 처음에는 begin, 0
        # 이후에는 바뀐 단어, 변환 횟수
        
        if now == target: # 최종 단어로 바뀌면
            return step # 변환한 횟수 반환
        
        for word in words: # words 안에 있는 차례로 가져오기
            count = 0 # 알파벳 하나만 바뀌어야 하므로 count로 now와 word가 얼마나 차이나는지 체크하는 용도
            for i in range(len(now)): # 3글자 단어라면 3번 체크 (단어의 길이만큼 체크)
                if now[i] != word[i]: # now와 words에서 가져온 단어를 알파벳끼리 대조
                    count += 1 
                    
            if count == 1: # 한번 바뀌었다면(바꿀 수 있는 조건)
                queue.append([word, step+1]) # queue에 바뀐 단어를 넣고 변환 횟수 증가
