def solution(word):
    answer = 0
    word_list = []
    words = 'AEIOU'
    
    def dfs(cnt, w):
        if cnt == 5:
            # 현재까지 생성한 문자의 개수, 5가 되면 탐색 종료
            return 
        for i in range(len(words)):
            # 단어의 길이만큼 반복
            word_list.append(w + words[i])
            # w에 문자를 추가한 후 다음 문자를 생성
            dfs(cnt+1, w + words[i])
            # 생성된 단어를 word_list에 추가하고 cnt를 1 증가시켜 재귀 호출
            
    dfs(0,"")
    # 빈 문자열 ""과 0을 인수로 전달
    
    return word_list.index(word)+1
# word_list에서 몇 번째로 나타나는지 찾기 위해 index 사용
# 해당 단어의 순설르 1부터 시작하는 인덱스로 반환
