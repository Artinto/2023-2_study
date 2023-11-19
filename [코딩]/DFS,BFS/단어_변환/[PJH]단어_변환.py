def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer

    words.append(begin) # words에 begin추가
    queue = [(begin, 0)] # begin을 기준으로 한 튜플을 큐로 저장
    while queue:
        current, level = queue.pop(0) # 큐에 저장된 단어와 단계를 꺼냄
        if current == target: # 현재단어와 target을 비교
            answer = level
            return answer
        for i in range(len(words)-1):
            if len([j for j in range(len(words[i])) if words[i][j]!=current[j]]) == 1: # 한 글자만 다른 경우
                queue.append((words[i], level+1)) # 현재단어와 한글자만 다른 단어를 다시 큐에 넣고 단계를 1 올림
    answer = 0
    return answer
